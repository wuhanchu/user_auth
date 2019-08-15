# -*- coding:utf-8 -*-
from flask import request, send_file,make_response,render_template
from lib.models import *
from lib.JsonResult import JsonResult
from lib import param_tool,com_tool,sql_tool
from webapi import markRoute
from dao import mark_dao

# 批量添加员工，支持直接把项目中的人员名单覆盖
@markRoute.route('/project_users', methods=['PUT'])
def projects_update_users():
    args = request.get_json()
    project_id = args.get("project_id")
    users_id = args.get("users_id")
    mark_role = args.get("mark_role")
    project_users = mark_dao.get_project_users(project_id)
    for user_id in users_id :
        # 判断数据库中是否已经存在该用户
        selected = [x for x in project_users if x[0] == user_id ]
        if len(selected) == 0:
            puser =  MarkProjectUser(project_id=project_id,user_id=user_id,mark_role=mark_role)
            db.session.add(puser)
        elif selected[0][1] != mark_role : #用户存在，并且是不同角色，报错
            return JsonResult.error("项目中同一个用户不能同时做质检和标注：id=%s"%user_id)
        else:   #已存在的用户，从project_users中删掉，剩下的是要删除的用户
            project_users.remove(selected[0])
        #project_users.append(param_tool.model_to_dict(puser))
    # 将mark_role下，没有提交的用户从数据库中删除
    to_del_users = [x[0] for x in project_users if x[1] == mark_role]
    if len(to_del_users)>0:
        users = db.session.query(MarkProjectUser).filter(MarkProjectUser.project_id == project_id).filter(MarkProjectUser.user_id.in_(to_del_users)).all()
        [db.session.delete(u) for u in users]

    db.session.commit()
    return JsonResult.success("更新项目用户成功！")

@markRoute.route('/project_users', methods=['GET'])
def projects_user_list():
    project_id = request.args.get("project_id")
    name = request.args.get("user_name")
    sql =r"""select * from (SELECT u.id,u.name, pi_count.mark_role, ifnull(pi_count.mark_sum,0) as mark_sum,ifnull(pi_count.mark_today,0) as mark_today
        ,ifnull(pi_count.inspection_sum,0) as inspection_sum,ifnull(pi_count.inspection_fail_sum,0) as inspection_fail_sum 
        FROM sys_user u join (
            SELECT user_id,0 as mark_role ,sum(CASE WHEN status = 2 THEN 1 ELSE 0 END) mark_sum,
            sum( CASE WHEN to_days( pi.mark_time ) = to_days( CURDATE( ) ) and  status = 2 THEN 1 ELSE 0 END ) mark_today,
            sum( CASE WHEN pi.inspection_status IS NOT NULL THEN 1 ELSE 0 END ) inspection_sum,
            sum( CASE WHEN pi.inspection_status =2 THEN 1 ELSE 0 END ) inspection_fail_sum 
            FROM mark_project_items pi WHERE project_id = %s GROUP BY user_id 
        union all SELECT inspection_person as user_id,1 as mark_role, count( pi.id ) mark_sum,  -- 质检总数
            sum( CASE WHEN to_days( pi.inspection_time ) = to_days( CURDATE( ) ) THEN 1 ELSE 0 END ) mark_today,
            0 inspection_sum,
            sum( CASE WHEN pi.inspection_status =2 THEN 1 ELSE 0 END ) inspection_fail_sum 
        FROM mark_project_items pi WHERE project_id = %s GROUP BY inspection_person) 
            as pi_count on u.id = pi_count.user_id 
    union all 
        select u.id,u.name, pu.mark_role, 0 as mark_sum, 0 as mark_today,0 as inspection_sum,0 as inspection_fail_sum 
        FROM sys_user u join mark_project_user pu on u.id = pu.user_id and pu.project_id = %s
        where u.id not in 
        (select ifnull(user_id,"is_null") user_id from mark_project_items where status = 2 and project_id = pu.project_id
        union select ifnull(inspection_person,"is_null") user_id from mark_project_items where project_id = pu.project_id )  
        ) t where 1=1 """%(project_id,project_id,project_id)


    if name is not None and name != '':
        sql = sql + "and name like '%" + name + "%'"
    sql = sql + " order by name "

    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    sort = request.args.get('sort')
    if param_tool.str_is_empty(sort):
        store = "-id"
    res,total = sql_tool.mysql_page(db,sql,offset,limit,sort)
    return JsonResult.res_page(res,total)

#删除
@markRoute.route('/project_users/<project_id>/<user_id>', methods=['DELETE'])
def project_users_delete(project_id,user_id):
    q = MarkProjectUser.query
    obj = q.get((project_id,user_id))

    if obj is None:
        return JsonResult.error("对象不存在！project_id=%s,user_id=%s"%(project_id,user_id))
    # 判断是否有标注数据
    if mark_dao.user_mark_count(project_id) >0 :
        return JsonResult.error("该项目已经上传标注数据！请先删除标注数据！" )

    #删除项目用户分配信息
    users = MarkProjectUser.query.filter_by(project_id = project_id).delete()

    db.session.delete(obj)
    db.session.commit()
    return JsonResult.success("删除成功！")

