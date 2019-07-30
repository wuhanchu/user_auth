# -*- coding:utf-8 -*-
from flask import request, send_file,make_response,render_template
from lib.models import *
from lib.JsonResult import JsonResult
from lib import param_tool
from webapi import baseRoute,markRoute

# 列表
@markRoute.route('/projects', methods=['GET'])
def list():
    q = SysUser.query
    name = request.args.get("name")
    if name is not None:
        q = q.filter(SysUser.name.like("%" + name + "%"))
    q = q.order_by(SysUser.name.desc())
    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    page = int(offset / limit)
    if page == 0 : page = 1
    page = q.paginate(page=page, per_page=limit)
    return JsonResult.page(page)

# 详细信息
@markRoute.route('/projects/<id>', methods=['GET'])
def get_info(id):
    user = SysUser.query.get(id)
    return JsonResult.queryResult(user)

@baseRoute.route('/projects', methods=['POST'])
def add():
    user = SysUser()
    args = request.form
    # 将参数加载进去
    param_tool.set_dict_parm(user, args)
    db.session.add(user)
    db.session.commit()
    return JsonResult.success("创建成功！", {"userid": user.id})

# PUT:全部字段 ；PATCH:部分字段
@baseRoute.route('/projects/<id>', methods=['PUT','PATCH'])
def update(id):
    user = SysUser.query.get(id)
    if user is None :
        return JsonResult.error("对象不存在，id=%s"%id)
    args = request.form
    #将参数加载进去
    param_tool.set_dict_parm(user,args)
    db.session.commit()
    return JsonResult.success("更新成功！",{"id": user.id})

@baseRoute.route('/users/<id>', methods=['DELETE'])
def del_users(id):
    "删除用户"
    user = SysUser.query.get(id)
    db.session.delete(user)
    # sql = """ delete from ts_meetasr_log where meetid='%s' """ % meetid
    # db.session.execute(sql)
    db.session.commit()
    return JsonResult.success("删除成功！", {"id": id})