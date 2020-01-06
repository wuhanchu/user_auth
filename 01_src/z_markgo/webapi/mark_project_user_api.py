# -*- coding:utf-8 -*-
from flask import request
from dao.models import *
from lib.JsonResult import JsonResult
from lib import sql_tool, param_tool
from webapi import markRoute, app
from dao import mark_dao
from lib.oauth2 import require_oauth


# 批量添加员工，支持直接把项目中的人员名单覆盖


@markRoute.route('/project_users', methods=['PUT'])
@require_oauth('profile')
def projects_update_users():
    args = request.get_json()
    project_id = args.get("project_id")
    users_id = args.get("users_id")
    mark_role = args.get("mark_role")
    project_users = mark_dao.get_project_users(project_id)
    for user_id in users_id:
        # 判断数据库中是否已经存在该用户
        selected = [x for x in project_users if x[0] == user_id]
        if len(selected) == 0:
            puser = MarkProjectUser(
                project_id=project_id, user_id=user_id, mark_role=mark_role)
            db.session.add(puser)
        elif selected[0][1] != mark_role:  # 用户存在，并且是不同角色，报错
            return JsonResult.error("项目中同一个用户不能同时做质检和标注：id=%s" % user_id)
        else:  # 已存在的用户，从project_users中删掉，剩下的是要删除的用户
            project_users.remove(selected[0])
        # project_users.append(param_tool.model_to_dict(puser))
    # 将mark_role下，没有提交的用户从数据库中删除
    to_del_users = [x[0] for x in project_users if x[1] == mark_role]

    app.logger.info("to_del_users" + str(to_del_users))

    if len(to_del_users) > 0:
        users = db.session.query(MarkProjectUser).filter(MarkProjectUser.project_id == project_id).filter(
            MarkProjectUser.user_id.in_(to_del_users)).all()
        [db.session.delete(u) for u in users]

    db.session.commit()
    return JsonResult.success("更新项目用户成功！")


@markRoute.route('/project_users', methods=['GET'])
@require_oauth('profile')
def projects_user_list():
    project_id = request.args.get("project_id")
    name = request.args.get("user_name")
    sql = r"""SELECT *
FROM (
         SELECT u.id,
                u.name,
                origin_role                             AS origin_role,
                pi_count.mark_role,
                ifnull(pi_count.mark_sum, 0)            AS mark_sum,
                ifnull(pi_count.mark_today, 0)          AS mark_today,
                ifnull(pi_count.inspection_sum, 0)      AS inspection_sum,
                ifnull(pi_count.inspection_fail_sum, 0) AS inspection_fail_sum
         FROM sys_user u
                  JOIN (
             SELECT pi.user_id,
                    pu.mark_role AS                                                   origin_role,
                    0            AS                                                   mark_role,
                    sum(CASE WHEN STATUS = 2 THEN 1 ELSE 0 END)                       mark_sum,
                    sum(CASE
                            WHEN to_days(pi.mark_time) = to_days(CURDATE()) AND STATUS = 2 THEN 1
                            ELSE 0 END)                                               mark_today,
                    sum(CASE WHEN pi.inspection_status = 2 or pi.inspection_status=3 THEN 1 ELSE 0 END) inspection_sum,
                    sum(CASE WHEN pi.inspection_status = 3 THEN 1 ELSE 0 END)         inspection_fail_sum
             FROM mark_project_items pi
                      left JOIN mark_project_user pu ON pi.user_id = pu.user_id
                 AND pu.project_id = {project_id}
             WHERE pi.project_id = {project_id}
             GROUP BY user_id
             UNION ALL
             SELECT inspection_person AS                                                              user_id,
                    pu.mark_role      AS                                                              origin_role,
                    1                 AS                                                              mark_role,
                    count(pi.id)                                                                      mark_sum,-- 质检总数
                    sum(CASE WHEN to_days(pi.inspection_time) = to_days(CURDATE()) THEN 1 ELSE 0 END) mark_today,
                    0                                                                                 inspection_sum,
                    sum(CASE WHEN pi.inspection_status = 3 THEN 1 ELSE 0 END)                         inspection_fail_sum
             FROM mark_project_items pi
                      left JOIN mark_project_user pu ON pi.inspection_person = pu.user_id
                 AND pu.project_id = {project_id}
             WHERE pi.project_id = {project_id}
             GROUP BY inspection_person
         ) AS pi_count ON u.id = pi_count.user_id
         UNION ALL
         SELECT u.id,
                u.name,
                pu.mark_role AS origin_role,
								pu.mark_role,
                0            AS mark_sum,
                0            AS mark_today,
                0            AS inspection_sum,
                0            AS inspection_fail_sum
         FROM sys_user u
                  JOIN mark_project_user pu ON u.id = pu.user_id
             AND pu.project_id = {project_id}
         WHERE u.id NOT IN (
             SELECT ifnull(user_id, "is_null") user_id
             FROM mark_project_items
             WHERE  project_id = pu.project_id
             UNION
             SELECT ifnull(inspection_person, "is_null") user_id
             FROM mark_project_items
             WHERE project_id = pu.project_id
         )
     ) t
WHERE 1 = 1""".format(project_id=project_id)

    if name is not None and name != '':
        sql = sql + "and name like '%" + name + "%'"
    sql = sql + " order by name "

    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    sort = request.args.get('sort')
    if param_tool.str_is_empty(sort):
        store = "-id"
    res, total = sql_tool.mysql_page(db, sql, offset, limit, sort)
    return JsonResult.res_page(res, total)


@markRoute.route('/user_projects/<user_id>', methods=['GET'])
@require_oauth('profile')
def user_projects_list(user_id):
    q = db.session.query(MarkProjectUser.project_id, MarkProject.name.label("project_name"), MarkProjectUser.user_id, MarkProjectUser.mark_role)\
        .join(MarkProject, MarkProject.id == MarkProjectUser.project_id).filter(MarkProjectUser.user_id == user_id)
    sort = request.args.get('sort')

    if sort == None:
        sort = "-project_id"
    q = sql_tool.set_model_sort(q, sort)
    list = q.all()
    return JsonResult.queryResult(list)

# 删除


@markRoute.route('/project_users/<project_id>/<user_id>', methods=['DELETE'])
@require_oauth('profile')
def project_users_delete(project_id, user_id):
    q = MarkProjectUser.query
    obj = q.get((project_id, user_id))

    if obj is None:
        return JsonResult.error("对象不存在！project_id=%s,user_id=%s" % (project_id, user_id))
    # 判断是否有标注数据
    if mark_dao.user_mark_count(project_id) > 0:
        return JsonResult.error("该项目已经上传标注数据！请先删除标注数据！")

    # 删除项目用户分配信息
    users = MarkProjectUser.query.filter_by(project_id=project_id).delete()

    db.session.delete(obj)
    db.session.commit()
    return JsonResult.success("删除成功！")
