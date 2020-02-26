# -*- coding:utf-8 -*-
import time

from flask import request

from frame import sql_tool, permission_context, param_tool
from frame.JsonResult import JsonResult
from module.auth.extension.oauth2 import require_oauth
from .. import blueprint
from ..model import *


# 角色列表
@blueprint.route('/role', methods=['GET'])
@require_oauth('profile')
def role_list():
    q = Role.query
    name = request.args.get("name")
    if name is not None:
        q = q.filter(Role.name.like("%" + name + "%"))
    q = q.order_by(Role.name.desc())
    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    sort = request.args.get('sort')
    if sort == None:
        sort = "-id"
    res, total = sql_tool.model_page(q, limit, offset, sort)
    return JsonResult.res_page(res, total)


# 详细角色信息
@blueprint.route('/role/<id>', methods=['GET'])
@require_oauth('profile')
def get_role(id):
    obj = Role.query.get(id)
    return JsonResult.queryResult(obj)


@blueprint.route('/role', methods=['POST'])
@require_oauth('profile')
def add_role():
    obj = Role()
    args = request.get_json()
    # 将参数加载进去
    param_tool.set_dict_parm(obj, args)
    obj.opr_at = int(time.time())
    db.session.add(obj)
    db.session.commit()
    return JsonResult.success("创建成功！", {"id": obj.id})


# PUT:全部字段 ；PATCH:部分字段
@blueprint.route('/role/<id>', methods=['PUT'])
@require_oauth('profile')
def update_role(id):
    obj = Role.query.get(id)
    if obj is None:
        return JsonResult.error("对象不存在，id=%s" % id)
    args = request.get_json()
    if "password" in args:
        args.pop("password")
    # 将参数加载进去
    param_tool.set_dict_parm(obj, args)
    db.session.commit()
    return JsonResult.success("更新成功！", {"id": obj.id})


@blueprint.route('/role/<id>', methods=['DELETE'])
@require_oauth('profile')
def del_role(id):
    "删除角色"
    obj = Role.query.get(id)
    db.session.delete(obj)
    # sql = """ delete from ts_meetasr_log where meetid='%s' """ % meetid
    # db.session.execute(sql)
    db.session.commit()
    return JsonResult.success("删除成功！", {"id": id})


@blueprint.route('/user_roles/<user_id>', methods=['GET'])
@require_oauth('profile')
def user_roles_list(user_id):
    list = Role.query.join(SysUserRole, SysUserRole.role_id == Role.id).filter(
        SysUserRole.user_id == user_id).all()
    return JsonResult.queryResult(list)





@blueprint.route('/role_permissions/<role_id>', methods=['GET'])
@require_oauth('profile')
def role_permissions_list(role_id):
    q = Permission.query.join(PermissionScopeRetail, PermissionScopeRetail.permission_id == Permission.id) \
        .join(PermissionScopeRole,
              PermissionScopeRole.permission_group_id == PermissionScopeRetail.permission_group_id) \
        .filter(PermissionScopeRole.role_id == role_id)
    list = q.all()
    return JsonResult.queryResult(list)


@blueprint.route('/role_permission_groups/<role_id>', methods=['GET'])
@require_oauth('profile')
def role_permission_groups_list(role_id):
    q = PermissionScope.query.join(PermissionScopeRole,
                                   PermissionScopeRole.permission_group_id == PermissionScope.id) \
        .filter(PermissionScopeRole.role_id == role_id)
    list = q.all()
    return JsonResult.queryResult(list)


@blueprint.route('/role_permission_groups/<role_id>', methods=['PUT'])
# @require_oauth('profile')
def update_role_permission_groups(role_id):
    args = request.get_json()
    role_permission_group_ids = args.get("role_permission_group_ids")
    role_permission_groups = PermissionScopeRole.query.filter(PermissionScopeRole.role_id == role_id).all()
    for permission_group_id in role_permission_group_ids:
        # 判断数据库中是否已经存在该用户
        selected = [pr for pr in role_permission_groups if pr.permission_group_id == permission_group_id]
        if len(selected) == 0:
            role_permission_group = PermissionScopeRole(role_id=role_id, permission_group_id=permission_group_id)
            db.session.add(role_permission_group)
        else:  # 已存在的角色，从user_roles中删掉，剩下的是要删除的用户
            role_permission_groups.remove(selected[0])
    # 删除已经不存在的数据
    [db.session.delete(role_permission_group) for role_permission_group in role_permission_groups]
    db.session.commit()
    permission_context.load_permission()
    return JsonResult.success("更新角色权限成功！")
