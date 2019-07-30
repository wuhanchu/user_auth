# -*- coding:utf-8 -*-
from flask import request, send_file,make_response,render_template
from lib.models import *
from lib.JsonResult import JsonResult
from lib import param_tool
from webapi import markRoute

# 列表
@markRoute.route('/projects', methods=['GET'])
def list():
    q = MarkProject.query
    name = request.args.get("name")
    type = request.args.get("type")
    if name is not None:
        q = q.filter(MarkProject.name.like("%" + name + "%"))
    if type is not None:
        q = q.filter_by(type = type)
    q = q.order_by(MarkProject.name.desc())

    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    page = int(offset / limit) + 1
    if page == 0 : page = 1
    page = q.paginate(page=page, per_page=limit)
    return JsonResult.page(page)

# 详细信息
@markRoute.route('/projects/<id>', methods=['GET'])
def get_info(id):
    obj = MarkProject.query.get(id)
    return JsonResult.queryResult(obj)

#添加
@markRoute.route('/projects', methods=['POST'])
def add():
    obj = MarkProject()
    args = request.form
    # 将参数加载进去
    param_tool.set_dict_parm(obj, args)
    db.session.add(obj)
    db.session.commit()
    return JsonResult.success("创建成功！", {"userid": obj.id})

# 更新
@markRoute.route('/projects/<id>', methods=['PUT','PATCH'])
def update(id):
    obj = MarkProject.query.get(id)
    if obj is None :
        return JsonResult.error("对象不存在，id=%s"%id)
    args = request.form
    #将参数加载进去
    param_tool.set_dict_parm(obj,args)
    db.session.commit()
    return JsonResult.success("更新成功！",{"id": obj.id})

#删除
@markRoute.route('/users/<id>', methods=['DELETE'])
def delete(id):
    obj = MarkProject.query.get(id)
    db.session.delete(obj)
    # sql = """ delete from ts_meetasr_log where meetid='%s' """ % meetid
    # db.session.execute(sql)
    db.session.commit()
    return JsonResult.success("删除成功！", {"id": id})