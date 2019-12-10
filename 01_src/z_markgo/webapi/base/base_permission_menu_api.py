# -*- coding:utf-8 -*-
from flask import request
from dao.base_model import *
from dao.models import db
from lib.JsonResult import JsonResult
from lib import param_tool
from webapi import baseRoute
from lib.oauth2 import require_oauth

#权限菜单列表
@baseRoute.route('/permission_menus',methods=['GET'])
@require_oauth("profile")
def permission_menu_list():
    q = SysPermissionMenu.query
    permission_id = request.args.get("permission_id")
    if permission_id is not None:
        q = q.filter(SysPermissionMenu.permission_id == permission_id)
    q = q.order_by(SysPermissionMenu.permission_id.desc())
    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    page = int(offset / limit)
    if page == 0 : page = 1
    page = q.paginate(page=page, per_page=limit)
    return JsonResult.page(page)

# 详细菜单信息
@baseRoute.route('/permission_menus/<pid>', methods=['GET'])
@require_oauth("profile")
def get_permission_menu(pid):
    permission_menu = db.session.query(SysPermissionMenu).filter(SysPermissionMenu.permission_id == pid).all()
    return JsonResult.queryResult(permission_menu)

@require_oauth("profile")
@baseRoute.route('/permission_menus', methods=['POST'])
def add_permission_menu():
    args = request.get_json()
    permission_id = args.get('permission_id')
    menu_list = args.get('menu_list')
    for i in range(len(menu_list)):
        obj = SysPermissionMenu(permission_id=permission_id,menu_id=menu_list[i])
        db.session.add(obj)
    db.session.commit()
    return JsonResult.success("创建成功！", {"permission_id": permission_id})

@baseRoute.route('/permission_menus/<id>', methods=['PUT','PATCH'])
@require_oauth("profile")
def update_permission_menu(id):
    permission_menu = SysPermissionMenu.query.get(id)
    if permission_menu is None :
        return JsonResult.error("对象不存在，id=%s"%id)
    args = request.get_json()
    #将参数加载进去
    param_tool.set_dict_parm(permission_menu, args)
    db.session.commit()
    return JsonResult.success("更新成功！",{"id": permission_menu.id})

@baseRoute.route('/permission_menus', methods=['DELETE'])
@require_oauth("profile")
def del_permission_menu():
    args = request.get_json()
    permission_id = args.get('permission_id')
    if permission_id is not None:
        db.session.query(SysPermissionMenu).filter(SysPermissionMenu.permission_id == permission_id).delete()
    db.session.commit()
    return JsonResult.success("删除成功！", {"id": permission_id})
