# -*- coding:utf-8 -*-
from flask import request, send_file,make_response,render_template
from lib.models import *
from lib.JsonResult import JsonResult
from lib import param_tool,com_tool,sql_tool,busi_tool
from webapi import markRoute
from sqlalchemy import and_
from lib.my_synchronized import synchronized

# 列表
@markRoute.route('/user_items', methods=['GET'])
def user_items_list():
    user_id = request.args.get("user_id")
    filepath = request.args.get("filepath")
    type = request.args.get("type")
    project_id = request.args.get("project_id")

    q = db.session.query(MarkProjectItem.project_id,MarkProjectItem.user_id,MarkProject.name,MarkProjectItem.filepath,
        MarkProjectItem.status,MarkProjectItem.inspection_status,MarkProjectItem.mark_time,SysUser.name.label("inspection_person_name") )\
        .join(MarkProject,MarkProject.id == MarkProjectItem.project_id ) \
        .join(MarkProjectUser, and_(MarkProjectUser.user_id == MarkProjectItem.user_id , MarkProjectUser.project_id == MarkProjectItem.project_id) )\
        .outerjoin(SysUser,MarkProjectItem.sys_user)

    q = q.filter(MarkProjectItem.user_id == user_id)
    if param_tool.str_is_not_empty(project_id):
        q = q.filter(MarkProjectItem.project_id == project_id)

    if param_tool.str_is_not_empty(type):
        q = q.filter(MarkProject.type==type)

    if param_tool.str_is_not_empty(filepath):
        q = q.filter(MarkProjectItem.filepath.like("%" + filepath + "%"))

    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    res, total = sql_tool.model_page(q,limit,offset)
    return JsonResult.res_page(res,total)

#去标注，获取下一个标注数据
@markRoute.route('/user_items/next_item', methods=['GET'])
def next_item():
    project_id = request.args.get("project_id")
    # q = AiService.query.join(MarkProject, MarkProject.ai_service == AiService.id)
    # res = q.filter(project_id).all()
    item = get_next_items(project_id)
    if item :
        return JsonResult.queryResult(item)
    else:
        return JsonResult.error("该项目已经标注完成了！")

    # 情况1，全部转写完  有未标注数据， 没有未标注数据   最后一条数据被占用
    # 情况2，未转写完成  无标注数据

#获取下一个标注数据
#处理并发请求
@synchronized(obj= "static")
def get_next_items(project_id):
    q = MarkProjectItem.query.filter_by(status = 0).filter(MarkProjectItem.asr_txt != None)
    q = q.join(MarkProject, MarkProject.id == MarkProjectItem.project_id).filter(MarkProject.status==0)
    if param_tool.str_is_not_empty(project_id) :
        q = q.filter(MarkProjectItem.project_id == project_id )
    items = q.order_by(MarkProjectItem.id).limit(1).all()
    if len(items) == 0:
        return JsonResult.error("没有可标注项目！")
    else:
        item = items[0]
        return item