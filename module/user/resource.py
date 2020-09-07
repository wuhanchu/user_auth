# -*- coding:utf-8 -*-
import urllib.parse

import requests
from authlib.integrations.flask_oauth2 import current_token
from flask import request, jsonify
from flask_restplus._http import HTTPStatus
from sqlalchemy import func, Text

from config import ConfigDefine
from frame.extension.database import db
from frame.extension.postgrest.util import get_args_delete_prefix
from frame.http.response import JsonResult
from frame.util import com_tool, sql_tool, param_tool
from module.auth.extension.oauth2 import require_oauth
from module.user.model import User, UserRole
from . import blueprint
from .schema import PhfundUserSchema
from .service import get_user_extend_info, append_permission, append_permission_scope
from .. import get_user_pattern
from ..role.model import Role


@blueprint.route('', methods=['POST'])
@require_oauth('profile')
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


@blueprint.route('/password', methods=['PUT'])
@require_oauth('profile')
def update_user_password():
    """
    # 修改密码
    :param id:
    :return:
    """
    id = request.args.get("id")

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


@blueprint.route('/role', methods=['PUT'])
@require_oauth('profile')
def update_user_roles():
    data = request.get_json()
    user_id = get_args_delete_prefix(request.args.get("id", ""))
    role_ids = data.get("role_ids")

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
@require_oauth('profile')
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

        # 调用服务器获取当前数据
        #
        # data = {
        #     "userId": 1341,
        #     "username": "biaozhu",
        #     "realname": "吴汉楚",
        #     "email": "x_wuhanchu@phfund.com.cn",
        #     "mobilePhone": "",
        #     "fixedPhone": "",
        #     "company": "",
        #     "department": "",
        #     "title": "",
        #     "userStatus": "正常",
        #     "sortNumber": "0"
        # }
        try:

            url = urllib.parse.urljoin(
                current_app.config.get(ConfigDefine.USER_SERVER_URL),
                "/user/operation/detail_info")
            response = requests.get(url, headers=request.headers)

            data = response.json()
            data = PhfundUserSchema().load(data)

            # 查询本地数据
            user_record = User.query.filter_by(loginid=data.get("loginid")).first()
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
    @require_oauth('profile')
    def current_user():
        if current_token:
            return jsonify(get_user_extend_info(current_token.user))
        else:
            return JsonResult.error()
