# -*- coding:utf-8 -*-
import urllib.parse
from http import HTTPStatus

import requests
from flask import request, jsonify
from sqlalchemy import func, Text

from config import ConfigDefine
from frame.extension.database import db
from frame.extension.postgrest.util import get_args_delete_prefix
from frame.http.response import JsonResult, Response
from frame.util import com_tool, sql_tool, param_tool
from module.auth.extension.oauth2 import require_oauth
from module.user.model import User, UserRole
from . import blueprint
from .service import get_user_extend_info, append_permission, append_permission_scope
from .. import get_user_pattern
from ..role.model import Role

from authlib.integrations.flask_oauth2 import current_token


@blueprint.route('', methods=['GET'])
def user_get():
    """
    用户列表
    :return:
    """

    id = request.args.get("id")
    if id:
        obj = User.query.get(id)
        return JsonResult.queryResult(obj)

    q = db.session.query(
        User.id, User.department_key,
        func.max(User.name).label("name"),
        func.max(User.loginid).label("loginid"),
        func.max(User.telephone).label("telephone"),
        func.max(User.address).label("address"),
        User.token, User.expires_in, User.login_at, User.login_ip, User.login_count, User.remark, User.opr_by,
        User.opr_at, User.del_fg, User.external_id, User.source, User.email, User.mobile_phone, User.enable,
        func.string_agg(func.cast(Role.id, Text),
                        ',').label("roles")).outerjoin(
        UserRole, UserRole.user_id == User.id).outerjoin(
        Role,
        Role.id == UserRole.role_id).group_by(User.id)

    name = request.args.get("name")
    if name is not None:
        q = q.filter(User.name.like("%" + name.split(".")[-1].replace("*", "") + "%"))

    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    sort = request.args.get('sort')
    if sort is None:
        sort = "-id"
    res, total = sql_tool.model_page(q, limit, offset, sort)
    return JsonResult.res_page(res, total)


@blueprint.route('', methods=['POST'])
def add_user():
    """
    增加用户
    :return:
    """
    obj = User()
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
        return JsonResult.error("创建失败，用户名重复！", {"loginid": obj.loginid})

    return JsonResult.success("创建成功！", {"userid": obj.id})


@blueprint.route('/password', methods=['PATCH'])
def update_user_password():
    """
    # 修改密码
    :return:
    """
    user = current_user().json
    id = user['id']
    obj = User.query.get(id)
    if obj is None:
        return JsonResult.error("对象不存在，id=%s" % id)
    args = request.get_json()
    if "old_password" in args and obj.password == com_tool.get_MD5_code(
            args["old_password"]):
        if "new_password" in args:
            new_passwd = com_tool.get_MD5_code(args["new_password"])
            obj.password = new_passwd
            db.session.commit()
            return JsonResult.success("修改密码成功！", {"id": obj.id})
        else:
            return JsonResult.error("修改密码失败，请输入新密码！")
    else:
        return JsonResult.error("修改密码失败，旧密码错误！")


@blueprint.route('/password/reset', methods=['POST'])
def admin_update_user_password():
    """
    # 修改密码(管理员使用不需要输入用户旧密码)
    :param id:
    :return:
    """

    args = request.get_json()
    id = args["id"]

    obj = User.query.get(id)

    if obj is None:
        return JsonResult.error("对象不存在，id=%s" % id)
    if "new_password" in args:
        new_passwd = com_tool.get_MD5_code(args["new_password"])
        obj.password = new_passwd
        db.session.commit()
        response = Response(message="修改密码成功！")
    else:
        response = Response(result=False, message="修改密码失败，请输入新密码！")

    return response.get_response()


@blueprint.route('/role', methods=['PUT'])
def update_user_roles():
    data = request.get_json()
    user_id_list = get_args_delete_prefix(request.args.get("id", "")).split(",")
    role_ids = data.get("role_ids")

    for user_id in user_id_list:
        user_roles = UserRole.query.filter(UserRole.user_id == user_id).all()
        for role_id in role_ids:
            # 判断数据库中是否已经存在该用户
            selected = [ur for ur in user_roles if ur.role_id == role_id]
            if len(selected) == 0:
                user_role = UserRole(user_id=user_id, role_id=role_id)
                db.session.add(user_role)
            else:  # 已存在的角色，从user_roles中删掉，剩下的是要删除的用户
                user_roles.remove(selected[0])

        # 删除已经不存在的数据
        [db.session.delete(user_role) for user_role in user_roles]

    db.session.commit()
    return JsonResult.success("更新用户角色成功！")


@blueprint.route('/role', methods=['GET'])
def user_roles_list():
    user_id = request.args.get("user_id")

    list = Role.query.join(
        UserRole,
        UserRole.role_id == Role.id).filter(UserRole.user_id == user_id).all()
    return JsonResult.queryResult(list)


# 鹏华
if get_user_pattern() == ConfigDefine.UserPattern.phfund:

    @blueprint.route('/current', methods=['GET'])
    def current_user():
        from flask import current_app, request
        from ..phfund.schema import PhfundUserSchema

        # 调用服务器获取当前数据
        try:

            url = urllib.parse.urljoin(
                current_app.config.get(ConfigDefine.USER_SERVER_URL),
                "/user/operation/detail_info")
            response = requests.get(url, headers=request.headers)

            data = response.json()
            data = PhfundUserSchema().load(data)

            # 查询本地数据
            user_record = User.query.filter_by(loginid=data.get("loginid")).first()
            if not user_record.enable:
                return {'message': "当前用户被禁用"}, HTTPStatus.UNAUTHORIZED

            data["id"] = user_record.id

            # 附加权限
            append_permission(data)
            append_permission_scope(data)

            # 返回
            return jsonify(data)
        except Exception as e:
            return {'message': "查找不到用户"}, HTTPStatus.UNAUTHORIZED

# 默认
else:

    @blueprint.route('/current', methods=['GET'])
    def current_user():

        if current_token:
            db.session.merge(current_token)
            user = current_token.user
            user_extend = {"client_id": current_token.client_id}
            if user:
                if not user.enable:
                    return {'message': "当前用户被禁用"}, HTTPStatus.UNAUTHORIZED
                user_extend = {**user_extend, **get_user_extend_info(user)}
            return jsonify(user_extend)
        else:
            return JsonResult.error()
