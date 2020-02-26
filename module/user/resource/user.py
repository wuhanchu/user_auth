# -*- coding:utf-8 -*-
from flask import request
from sqlalchemy import func

from frame import sql_tool, com_tool, param_tool
from frame.JsonResult import JsonResult
from module.auth.extension.oauth2 import require_oauth
from .. import blueprint
from ..model import *


@blueprint.route('', methods=['GET'])
@require_oauth('profile')
def user_list():
    """
    用户列表
    :return:
    """
    q = db.session.query(SysUser.id, func.max(SysUser.name).label("name"),
                         func.max(SysUser.loginid).label("loginid"), func.max(SysUser.telephone) \
                         .label("telephone"), func.max(SysUser.address).label("address"),
                         func.string_agg(Role.name, ',').label("roles")) \
        .outerjoin(SysUserRole, SysUserRole.user_id == SysUser.id) \
        .outerjoin(Role, Role.id == SysUserRole.role_id).group_by(SysUser.id)
    name = request.args.get("name")
    if name is not None:
        q = q.filter(SysUser.name.like("%" + name + "%"))
    # q = q.order_by(SysUser.name.desc())
    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    sort = request.args.get('sort')
    if sort == None:
        sort = "-id"
    res, total = sql_tool.model_page(q, limit, offset, sort)
    return JsonResult.res_page(res, total)


@blueprint.route('/<id>', methods=['GET'])
@require_oauth('profile')
def get_user(id):
    """
    详细用户信息
    :param id:
    :return:
    """
    obj = SysUser.query.get(id)
    return JsonResult.queryResult(obj)


@blueprint.route('', methods=['POST'])
@require_oauth('profile')
def add_user():
    """
    增加用户
    :return:
    """
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
    except Exception as e:
        return JsonResult.error("创建失败，用户名重复！", {"loginid": obj.loginid})

    return JsonResult.success("创建成功！", {"userid": obj.id})


@blueprint.route('/<id>', methods=['PUT', 'PATCH'])
@require_oauth('profile')
def update_user(id):
    """
     PUT:全部字段 ；PATCH:部分字段
    :param id:
    :return:
    """
    obj = SysUser.query.get(id)
    if obj is None:
        return JsonResult.error("对象不存在，id=%s" % id)
    args = request.get_json()
    if "password" in args:
        args.pop("password")
    # 将参数加载进去
    param_tool.set_dict_parm(obj, args)
    db.session.commit()
    return JsonResult.success("更新成功！", {"id": obj.id})


@blueprint.route('/<id>/password', methods=['PUT', 'PATCH'])
@require_oauth('profile')
def update_user_password(id):
    """
    # 修改密码
    :param id:
    :return:
    """
    obj = SysUser.query.get(id)
    if obj is None:
        return JsonResult.error("对象不存在，id=%s" % id)
    args = request.get_json()
    if "old_password" in args and obj.password == com_tool.get_MD5_code(args["old_password"]):
        if "new_password" in args:
            new_passwd = com_tool.get_MD5_code(args["new_password"])
            obj.password = new_passwd
            db.session.commit()
            return JsonResult.success("修改密码成功！", {"id": obj.id})
        else:
            return JsonResult.error("修改密码失败，请输入新密码！")
    else:
        return JsonResult.error("修改密码失败，旧密码错误！")


@blueprint.route('/user_roles', methods=['PUT'])
@require_oauth('profile')
def update_user_roles():
    data = request.get_json()
    user_id = request.args.get("id")
    role_ids = data.get("role_ids")
    user_roles = SysUserRole.query.filter(SysUserRole.user_id == user_id).all()
    for role_id in role_ids:
        # 判断数据库中是否已经存在该用户
        selected = [ur for ur in user_roles if ur.role_id == role_id]
        if len(selected) == 0:
            user_role = SysUserRole(user_id=user_id, role_id=role_id)
            db.session.add(user_role)
        else:  # 已存在的角色，从user_roles中删掉，剩下的是要删除的用户
            user_roles.remove(selected[0])
    # 删除已经不存在的数据
    [db.session.delete(user_role) for user_role in user_roles]
    db.session.commit()
    return JsonResult.success("更新用户角色成功！")
