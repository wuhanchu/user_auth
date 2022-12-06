# -*- coding:utf-8 -*-
import urllib.parse
from http import HTTPStatus

import requests
from authlib.integrations.flask_oauth2 import current_token
from flask import jsonify, request
from flask_frame.api.response import JsonResult, Response
from flask_frame.extension.database import db
from flask_frame.extension.postgrest.util import get_args_delete_prefix
from flask_frame.util import com_tool, param_tool, sql_tool
from sqlalchemy import Text, func

from config import ConfigDefine
from module.auth.extension.oauth2 import require_oauth
from module.user.model import User, UserRole

from .. import get_user_pattern
from ..role.model import Role
from . import blueprint


@blueprint.route("", methods=["POST"])
@require_oauth()
def add_user():
    """
    增加用户
    :return:
    """
    obj = User()
    args = request.get_json()

    try:
        # 将参数加载进去
        param_tool.set_dict_parm(obj, args)
        password = args.get("password")
        password = com_tool.get_md5_code(password)
        obj.password = password
        db.session.add(obj)

        db.session.commit()
    except Exception:
        db.session.rollback()
        return Response(
            result=False, message="创建失败，账户重复！", data={"loginid": obj.loginid}
        ).mark_flask_response()

    return Response(data={"id": obj.id}).mark_flask_response()


@blueprint.route("/register", methods=["POST"])
def user_register():
    """
    用户注册
    :return:
    """
    from flask_frame.api.exception import ResourceError

    from module.config.model import Config

    register_switch = Config.query.filter_by(key=Config.KEY.register_switch).first()
    if not register_switch or register_switch.value.strip() != "true":
        raise ResourceError("注册功能已关闭")

    try:
        obj = User()
        args = request.get_json()

        # 将参数加载进去
        param_tool.set_dict_parm(obj, args)
        password = args.get("password")
        password = com_tool.get_md5_code(password)
        obj.password = password
        db.session.add(obj)

        db.session.commit()
    except Exception:
        db.session.rollback()

        return Response(
            result=False, message="创建失败，账户重复！", data={"loginid": obj.loginid}
        ).mark_flask_response()

    return Response(data={"id": obj.id}).mark_flask_response()


@blueprint.route("/password", methods=["PATCH"])
@require_oauth()
def update_user_password():
    """
    # 修改密码
    :return:
    """
    user = current_user().json
    id = user["id"]
    obj = User.query.get(id)
    if obj is None:
        return JsonResult.error("对象不存在，id=%s" % id)
    args = request.get_json()
    if "old_password" in args and obj.password == com_tool.get_md5_code(
        args["old_password"]
    ):
        if "new_password" in args:
            new_passwd = com_tool.get_md5_code(args["new_password"])
            obj.password = new_passwd
            db.session.commit()
            return JsonResult.success("修改密码成功！", {"id": obj.id})
        else:
            return JsonResult.error("修改密码失败，请输入新密码！")
    else:
        return JsonResult.error("修改密码失败，旧密码错误！")


@blueprint.route("/password/reset", methods=["POST"])
@require_oauth()
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
        new_passwd = com_tool.get_md5_code(args["new_password"])
        obj.password = new_passwd
        db.session.commit()
        response = Response(message="修改密码成功！")
    else:
        response = Response(result=False, message="修改密码失败，请输入新密码！")

    return response.get_response()


@blueprint.route("/role", methods=["PUT"])
@require_oauth()
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


@blueprint.route("/role", methods=["GET"])
@require_oauth()
def user_roles_list():
    user_id = request.args.get("user_id")

    list = (
        Role.query.join(UserRole, UserRole.role_id == Role.id)
        .filter(UserRole.user_id == user_id)
        .all()
    )
    return JsonResult.queryResult(list)


@blueprint.route("/current", methods=["GET"])
@require_oauth()
def current_user():

    if current_token:
        if current_token.user and not current_token.user.enable:
            return {"message": "当前用户被禁用"}, HTTPStatus.UNAUTHORIZED
        return jsonify(current_token.user_info)
    else:
        return JsonResult.error()
