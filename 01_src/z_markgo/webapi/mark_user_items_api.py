# -*- coding:utf-8 -*-
from flask import request, send_file, make_response, render_template
from lib.models import *
from lib.JsonResult import JsonResult
from lib import param_tool, com_tool, sql_tool, busi_tool
from webapi import markRoute, app
from sqlalchemy import and_, or_
from lib.my_synchronized import synchronized
from lib.oauth2 import require_oauth
from dao import mark_dao
from lib.oauth2 import require_oauth
from authlib.flask.oauth2 import current_token
import logging

logger = logging.getLogger('flask.app')

# 标注列表
@markRoute.route('/user_items', methods=['GET'])
@require_oauth('profile')
def user_items_list():
    user = current_token.user
    filepath = request.args.get("filepath")
    type = request.args.get("type")
    project_id = request.args.get("project_id")

    q = db.session.query(* MarkProjectItem.__table__.columns._all_columns, SysUser.name.label("inspection_person_name"))\
        .join(MarkProject, MarkProject.id == MarkProjectItem.project_id) \
        .join(MarkProjectUser, and_(MarkProjectUser.user_id == MarkProjectItem.user_id, MarkProjectUser.project_id == MarkProjectItem.project_id))\
        .outerjoin(SysUser, MarkProjectItem.sys_user)

    q = q.filter(MarkProjectItem.user_id == user.id)
    if param_tool.str_is_not_empty(project_id):
        q = q.filter(MarkProjectItem.project_id == project_id)

    if param_tool.str_is_not_empty(type):
        q = q.filter(MarkProject.type == type)

    if param_tool.str_is_not_empty(filepath):
        q = q.filter(MarkProjectItem.filepath.like("%" + filepath + "%"))

    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    sort = request.args.get('sort')
    if sort == None:
        sort = "-id"
    res, total = sql_tool.model_page(q, limit, offset, sort)
    return JsonResult.res_page(res, total)


# 质检列表
@markRoute.route('/user_inspections', methods=['GET'])
@require_oauth('profile')
def user_inspections_list():
    user = current_token.user
    filepath = request.args.get("filepath")
    type = request.args.get("type")
    project_id = request.args.get("project_id")

    q = db.session.query(* MarkProjectItem.__table__.columns._all_columns, SysUser.name.label("marker_name"))\
        .join(MarkProject, MarkProject.id == MarkProjectItem.project_id).join(SysUser, MarkProjectItem.user)
    q = q.filter(MarkProjectItem.inspection_person == user.id).filter(
        MarkProjectItem.inspection_status.in_((2, 3)))
    if param_tool.str_is_not_empty(project_id):
        q = q.filter(MarkProjectItem.project_id == project_id)

    if param_tool.str_is_not_empty(type):
        q = q.filter(MarkProject.type == type)

    if param_tool.str_is_not_empty(filepath):
        q = q.filter(MarkProjectItem.filepath.like("%" + filepath + "%"))

    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    sort = request.args.get('sort')
    if sort == None:
        sort = "-id"
    res, total = sql_tool.model_page(q, limit, offset, sort)
    return JsonResult.res_page(res, total)

# 去标注，获取下一个标注数据
@markRoute.route('/user_items/next_item', methods=['GET'])
@require_oauth('profile')
def next_item():
    project_id = request.args.get("project_id")
    type = request.args.get("type")
    print("-----print-----------type:%s" % type)
    logger.debug("------log----------type:%s" % type)

    if type == "1":
        item = get_next_items(project_id)
    else:
        item = get_next_inspection_items(project_id)

    if item:
        return JsonResult.queryResult(item)
    else:
        return JsonResult.error("没有未标注数据了！")

    # 情况1，全部转写完  有未标注数据， 没有未标注数据   最后一条数据被占用
    # 情况2，未转写完成  无标注数据

# 获取下一个标注数据
@synchronized(obj="static_")
def get_next_items(project_id):
    user = current_token.user
    q = MarkProjectItem.query  # .filter(MarkProjectItem.asr_txt != None)
    q = q.join(MarkProjectUser, MarkProjectUser.project_id ==
               MarkProjectItem.project_id).filter(MarkProjectUser.user_id == user.id)
    q = q.filter(or_(MarkProjectItem.status == 0, and_(
        MarkProjectItem.user_id == user.id, MarkProjectItem.status == 1)))
    q = q.join(MarkProject, MarkProject.id ==
               MarkProjectItem.project_id).filter(MarkProject.status == 0)
    if param_tool.str_is_not_empty(project_id):
        q = q.filter(MarkProjectItem.project_id == project_id)
    item = q.order_by(MarkProjectItem.asr_txt.desc()
                      ).order_by(MarkProjectItem.id).first()
    logger.warn("-----------next_item:%s" % str(q))
    # if True:
    #     raise RuntimeError("next_item sql : %s"%str(q) )
    # 更新标注状态
    if item and item.status == 0:
        item.status = 1
        item.assigned_time = param_tool.get_curr_time()
        item.user_id = user.id
        db.session.commit()
    return item


# 获取下一个质检数据
@synchronized(obj="static_inspection")
def get_next_inspection_items(project_id):
    user = current_token.user
    q = MarkProjectItem.query.filter(MarkProjectItem.status == 2).filter(MarkProjectItem.inspection_status.in_((0, 1)))\
        .filter(or_(MarkProjectItem.inspection_person.is_(None), MarkProjectItem.inspection_person == user.id))
    q = q.join(MarkProjectUser, MarkProjectUser.project_id ==
               MarkProjectItem.project_id).filter(MarkProjectUser.user_id == user.id)
    q = q.join(MarkProject, MarkProject.id ==
               MarkProjectItem.project_id).filter(MarkProject.status == 0)
    if param_tool.str_is_not_empty(project_id):
        q = q.filter(MarkProjectItem.project_id == project_id)
    item = q.order_by(MarkProjectItem.id).first()
    logger.warn("-----------next_inspection_items:%s" % str(q))
    # 更新标注状态
    if item and item.status == 0:
        item.inspection_status = 1
        item.inspection_person = user.id
        db.session.commit()
    return item
