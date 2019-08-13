# -*- coding:utf-8 -*-
from flask import request, send_file,make_response,render_template
from lib.models import *
from lib.model_oauth import OAuth2Token
from lib.JsonResult import JsonResult
from lib import JsonResult as js

from lib import param_tool,sql_tool,com_tool
from webapi import baseRoute,app
from lib.oauth2 import require_oauth

# 用户列表
@baseRoute.route('/users', methods=['GET'])
def user_list():
    q = SysUser.query
    name = request.args.get("name")
    if name is not None:
        q = q.filter(SysUser.name.like("%" + name + "%"))
    q = q.order_by(SysUser.name.desc())
    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    res,total = sql_tool.model_page(q,limit,offset)
    return JsonResult.res_page(res,total)

# 详细用户信息
@baseRoute.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = SysUser.query.get(id)
    return JsonResult.queryResult(user)

@baseRoute.route('/users', methods=['POST'])
def add_user():
    args = request.get_json()
    name = args.get("name")
    username = args.get("username")
    telephone = args.get("telephone")
    #将password转为md5编码
    password = args.get("password")
    password = com_tool.get_MD5_code(password)
    user = SysUser(name=name, username=username, password=password, telephone=telephone)
    db.session.add(user)
    db.session.commit()
    return JsonResult.success("创建成功！", {"userid": user.id})

# PUT:全部字段 ；PATCH:部分字段
@baseRoute.route('/users/<id>', methods=['PUT','PATCH'])
def update_user(id):
    user = SysUser.query.get(id)
    if user is None :
        return JsonResult.error("对象不存在，id=%s"%id)
    args = request.get_json()
    if "password" in args:
        args.pop("password")
    #将参数加载进去
    param_tool.set_dict_parm(user,args)
    db.session.commit()
    return JsonResult.success("更新成功！",{"id": user.id})

# 修改密码
@baseRoute.route('/users/<id>/password', methods=['PUT','PATCH'])
def update_user_password(id):
    user = SysUser.query.get(id)
    if user is None :
        return JsonResult.error("对象不存在，id=%s"%id)
    args = request.get_json()
    if "old_password" in args and user.password == com_tool.get_MD5_code(args["old_password"]) :
        if "new_password" in args:
            new_passwd = com_tool.get_MD5_code(args["new_password"])
            user.password = new_passwd
            db.session.commit()
            return JsonResult.success("修改密码成功！", {"id": user.id})
        else:
            return JsonResult.error("修改密码失败，请输入新密码！")
    else:
        return JsonResult.error("修改密码失败，旧密码错误！")


@require_oauth('profile')
@baseRoute.route('/current_user', methods=['GET'])
def current_user():
    authorization = request.headers.environ["HTTP_AUTHORIZATION"]
    authorization = authorization.split(" ")
    if len(authorization) == 2:
        access_token = authorization[1]
        q = SysUser.query.join(OAuth2Token,OAuth2Token.user_id == SysUser.id).filter(OAuth2Token.access_token==access_token).filter(OAuth2Token.revoked==0)
        user = q.first()
        if user:
            user = js.queryToDict(user)
            print(user)
            user.pop("password")
            user.pop("del_fg")
            user.pop("token")
            return JsonResult.success("查询成功",user)
    return JsonResult.error()


@baseRoute.route('/users/<id>', methods=['DELETE'])
def del_users(id):
    "删除用户"
    user = SysUser.query.get(id)
    db.session.delete(user)
    # sql = """ delete from ts_meetasr_log where meetid='%s' """ % meetid
    # db.session.execute(sql)
    db.session.commit()
    return JsonResult.success("删除成功！", {"id": id})