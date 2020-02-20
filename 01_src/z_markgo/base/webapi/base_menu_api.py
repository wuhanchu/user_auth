from flask import request
from ..dao.base_model import *
from dao.models import db
from ..lib.JsonResult import JsonResult
from ..lib import param_tool
from ..lib.oauth2 import require_oauth
from . import baseRoute


# 菜单列表
@baseRoute.route('/menus', methods=['GET'])
@require_oauth("profile")
def menu_list():
    q = SysMenu.query
    name = request.args.get("name")
    if name is not None:
        q = q.filter(SysMenu.name.like("%" + name + "%"))
    q = q.order_by(SysMenu.name.desc())
    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    page = int(offset / limit)
    if page == 0 : page = 1
    page = q.paginate(page=page, per_page=limit)
    return JsonResult.page(page)

# 详细菜单信息
@baseRoute.route('/menus/<id>', methods=['GET'])
@require_oauth("profile")
def get_menu(id):
    menu = SysMenu.query.get(id)
    return JsonResult.queryResult(menu)

@baseRoute.route('/menus', methods=['POST'])
@require_oauth("profile")
def add_menu():
    obj = SysMenu()
    args = request.get_json()
    # 将参数加载进去
    param_tool.set_dict_parm(obj, args)
    db.session.add(obj)
    db.session.commit()
    return JsonResult.success("创建成功！", {"menu_id": obj.id})

@baseRoute.route('/menus/<id>', methods=['PUT','PATCH'])
@require_oauth("profile")
def update_menu(id):
    menu = SysMenu.query.get(id)
    if menu is None :
        return JsonResult.error("对象不存在，id=%s"%id)
    args = request.get_json()
    #将参数加载进去
    param_tool.set_dict_parm(menu, args)
    db.session.commit()
    return JsonResult.success("更新成功！",{"id": menu.id})

@baseRoute.route('/menus/<id>', methods=['DELETE'])
@require_oauth("profile")
def del_menu(id):
    "删除菜单"
    menu = SysMenu.query.get(id)
    db.session.delete(menu)
    # sql = """ delete from ts_meetasr_log where meetid='%s' """ % meetid
    # db.session.execute(sql)
    db.session.commit()
    return JsonResult.success("删除成功！", {"id": id})

@baseRoute.route('/user_menus/<id>', methods=['GET'])
@require_oauth("profile")
def search_users_menu(id):
    "查找用户拥有的菜单"
    # q = db.session.query(*SysUser.__table__.columns._all_columns,
    #                      SysPermissionMenu.menu_id.label("menu_id")).\
    #     join(SysUserRole, SysUser.id == SysUserRole.user_id).\
    #     join(SysPermissionRole, SysUserRole.role_id == SysPermissionRole.role_id).\
    #     join(SysPermissionMenu, SysPermissionRole.permission_id == SysPermissionMenu.permission_id).\
    #     filter(SysUser.id == id)
    # result = q.all()
    # db.session.commit()
    return JsonResult.queryResult("未实现")
