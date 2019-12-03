# -*- coding:utf-8 -*-
from flask import request
from dao.base_model import *
from lib.JsonResult import JsonResult
from lib import sql_tool, com_tool, param_tool
from webapi import baseRoute
from lib.oauth2 import require_oauth
from sqlalchemy import func

# 用户列表
@baseRoute.route('/users', methods=['GET'])
@require_oauth('profile')
def user_list():
    q = db.session.query(SysUser.id,func.max(SysUser.name).label("name"),func.max(SysUser.loginid).label("loginid"),func.max(SysUser.telephone)\
        .label("telephone"),func.max(SysUser.address).label("address"),func.group_concat(SysRole.name).label("roles"))\
        .outerjoin(SysUserRole,SysUserRole.user_id == SysUser.id).outerjoin(SysRole,SysRole.id == SysUserRole.role_id).group_by(SysUser.id)
    name = request.args.get("name")
    if name is not None:
        q = q.filter(SysUser.name.like("%" + name + "%"))
    # q = q.order_by(SysUser.name.desc())
    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    sort = request.args.get('sort')
    if sort == None:
        sort = "-id"
    res,total = sql_tool.model_page(q,limit,offset,sort)
    return JsonResult.res_page(res,total)

# 详细用户信息
@baseRoute.route('/users/<id>', methods=['GET'])
@require_oauth('profile')
def get_user(id):
    obj = SysUser.query.get(id)
    return JsonResult.queryResult(obj)

@baseRoute.route('/users', methods=['POST'])
@require_oauth('profile')
def add_user():
    obj = SysUser()
    args = request.get_json()
    # 将参数加载进去
    param_tool.set_dict_parm(obj, args)
    password = args.get("password")
    password = com_tool.get_MD5_code(password)
    obj.password = password
    db.session.add(obj)
    try:
        db.session.commit()
    except Exception:
        print("hi")
        return JsonResult.error("创建失败，用户名重复！", {"loginid": loginid})

    return JsonResult.success("创建成功！", {"userid": obj.id})

# PUT:全部字段 ；PATCH:部分字段
@baseRoute.route('/users/<id>', methods=['PUT','PATCH'])
@require_oauth('profile')
def update_user(id):
    obj = SysUser.query.get(id)
    if obj is None :
        return JsonResult.error("对象不存在，id=%s"%id)
    args = request.get_json()
    if "password" in args:
        args.pop("password")
    #将参数加载进去
    param_tool.set_dict_parm(obj, args)
    db.session.commit()
    return JsonResult.success("更新成功！",{"id": obj.id})

# 修改密码
@baseRoute.route('/users/<id>/password', methods=['PUT','PATCH'])
@require_oauth('profile')
def update_user_password(id):
    obj = SysUser.query.get(id)
    if obj is None :
        return JsonResult.error("对象不存在，id=%s"%id)
    args = request.get_json()
    if "old_password" in args and obj.password == com_tool.get_MD5_code(args["old_password"]) :
        if "new_password" in args:
            new_passwd = com_tool.get_MD5_code(args["new_password"])
            obj.password = new_passwd
            db.session.commit()
            return JsonResult.success("修改密码成功！", {"id": obj.id})
        else:
            return JsonResult.error("修改密码失败，请输入新密码！")
    else:
        return JsonResult.error("修改密码失败，旧密码错误！")

@baseRoute.route('/users/<id>', methods=['DELETE'])
@require_oauth('profile')
def del_users(id):
    "删除用户"
    obj = SysUser.query.get(id)
    db.session.delete(obj)
    # sql = """ delete from ts_meetasr_log where meetid='%s' """ % meetid
    # db.session.execute(sql)
    db.session.commit()
    return JsonResult.success("删除成功！", {"id": id})

