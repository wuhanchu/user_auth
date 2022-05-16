# -*- coding:utf-8 -*-
import time

from flask import request

from flask_frame import permission_context
from flask_frame.extension.database import db
from flask_frame.extension.postgrest.util import get_args_delete_prefix
from flask_frame.api.response import JsonResult
from flask_frame.util import sql_tool, param_tool
from module.auth.extension.oauth2 import require_oauth
from module.permission.model import Permission, PermissionScopeRetail, PermissionScope
from module.role.model import Role, RolePermissionScope
from . import blueprint


# 角色列表
@blueprint.route("", methods=["GET"])
@require_oauth()
def role_list():
    id = request.args.get("id")
    if id:
        return get_role(id)

    q = Role.query
    name = request.args.get("name")
    if name is not None:
        q = q.filter(Role.name.like("%" + name + "%"))
    q = q.order_by(Role.name.desc())
    offset = int(request.args.get("offset"))
    limit = int(request.args.get("limit"))
    sort = request.args.get("sort")
    if sort == None:
        sort = "-id"
    res, total = sql_tool.model_page(q, limit, offset, sort)
    return JsonResult.res_page(res, total)


def get_role(id):
    """
    # 详细角色信息
    :param id:
    :return:
    """
    obj = Role.query.get(id)
    return JsonResult.queryResult(obj)


@blueprint.route("/permission", methods=["GET"])
@require_oauth()
def role_permissions_list():
    role_id = request.args.get("role_id")
    q = (
        Permission.query.join(
            PermissionScopeRetail,
            PermissionScopeRetail.permission_key == Permission.key,
        )
        .join(
            RolePermissionScope,
            RolePermissionScope.permission_scope_key
            == PermissionScopeRetail.permission_scope_key,
        )
        .filter(RolePermissionScope.role_id == role_id)
    )
    list = q.all()
    return JsonResult.queryResult(list)


@blueprint.route("/permission_scope", methods=["GET"])
@require_oauth()
def role_permission_scopes_list():
    role_id = get_args_delete_prefix(request.args.get("role_id"))

    q = PermissionScope.query.join(
        RolePermissionScope,
        RolePermissionScope.permission_scope_key == PermissionScope.key,
    ).filter(RolePermissionScope.role_id == role_id)
    list = q.all()
    return JsonResult.queryResult(list)


@blueprint.route("/permission_scope", methods=["PUT"])
@require_oauth()
def update_role_permission_scopes():
    id = get_args_delete_prefix(request.args.get("id"))

    args = request.get_json()

    # delete before
    db.session.execute(
        RolePermissionScope.__table__.delete().where(RolePermissionScope.role_id == id)
    )

    # add new
    role_permission_scope = args.get("role_permission_scope")
    for permission_scope in role_permission_scope:
        role_permission_scope = RolePermissionScope(
            role_id=id,
            permission_scope_key=permission_scope.get("key"),
            product_key=permission_scope.get("product_key"),
        )
        db.session.add(role_permission_scope)

    db.session.commit()

    # reload
    permission_context.load_permission()
    return JsonResult.success("更新角色权限成功！")


def init_app(app, **kwargs):
    app.register_blueprint(blueprint)
