# -*- coding:utf-8 -*-
from flask import request, send_file,make_response,render_template
from lib.models import *
from lib.JsonResult import JsonResult
from lib import param_tool,com_tool,sql_tool,busi_tool
from webapi import markRoute
from sqlalchemy import and_,or_
from lib.my_synchronized import synchronized
from lib.oauth2 import require_oauth
from dao import mark_dao

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
    sort = request.args.get('sort')
    if sort == None:
        sort = "-id"
    res, total = sql_tool.model_page(q,limit,offset,sort)
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
@require_oauth('profile')
def get_next_items(project_id):
    authorization = request.headers.environ["HTTP_AUTHORIZATION"]
    user = mark_dao.get_user_by_token(authorization)
    q = MarkProjectItem.query.filter(MarkProjectItem.asr_txt != None)
    q = q.filter(or_(MarkProjectItem.status == 0,and_(MarkProjectItem.user_id == user["id"], MarkProjectItem.status == 1)))
    q = q.join(MarkProject, MarkProject.id == MarkProjectItem.project_id).filter(MarkProject.status==0)
    if param_tool.str_is_not_empty(project_id) :
        q = q.filter(MarkProjectItem.project_id == project_id )
    item = q.order_by(MarkProjectItem.id).first()
    #更新标注状态
    if item and item.status == 0:
        item.status=1;
        item.user_id = user["id"]
        db.session.commit()
    return item