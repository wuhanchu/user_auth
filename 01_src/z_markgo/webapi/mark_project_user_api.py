# -*- coding:utf-8 -*-
from flask import request, send_file,make_response,render_template
from lib.models import *
from lib.JsonResult import JsonResult
from lib import param_tool,com_tool,sql_tool
from webapi import markRoute

@markRoute.route('/projects/addusers', methods=['POST'])
def projects_addusers():
    args = request.get_json()
    project_id = args.get("project_id")
    users_id = args.get("users_id")
    project_users = []
    for user_id in users_id :
        puser =  MarkProjectUser(project_id=project_id,user_id=user_id)
        db.session.add(puser)
        #project_users.append(param_tool.model_to_dict(puser))
    db.session.commit()
    return JsonResult.success("添加项目用户成功！")

@markRoute.route('/project_users/<project_id>', methods=['GET'])
def projects_user_list(project_id):
    sql =r"""select u.name ,'质检员' as role ,pi.* from sys_user u join
    (select user_id ,count(pi.id) mark_sum,sum(case when to_days(pi.mark_time) = to_days(CURDATE()) then 1 else 0 end) mark_today
        ,sum(case when  pi.inspection_type is not NULL then 1 else 0 end) inspection_sum, sum(case when  pi.inspection_type =-1 then 1 else 0 end) inspection_fail_sum
    from mark_project_items pi where project_id = %s group by user_id) pi  on pi.user_id = u.id  where 1=1 """%project_id

    name = request.args.get("user_name")
    if name is not None and name != '':
        sql = sql + "and u.name like '%" + name + "%'"
    sql = sql + " order by u.name "

    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    res,total = sql_tool.mysql_page(db,sql,limit,offset)
    return JsonResult.sql_pag(res,total)
