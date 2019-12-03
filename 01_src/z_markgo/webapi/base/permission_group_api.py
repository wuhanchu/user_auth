
from flask import request, send_file,make_response,render_template
from dao.base_model import *
from lib.JsonResult import JsonResult
from lib import param_tool,permission_context,sql_tool
from webapi import baseRoute,app
from lib.oauth2 import require_oauth

# 权限分组列表
@baseRoute.route('/permission_group', methods=['GET'])
@require_oauth('profile')
def permission_group_list():
    q = SysPermissionGroup.query
    name = request.args.get("name")
    if name is not None:
        q = q.filter(SysPermissionGroup.name.like("%" + name + "%"))
    q = q.order_by(SysPermissionGroup.name.desc())
    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    sort = request.args.get('sort')
    if sort == None:
        sort = "-id"
    res, total = sql_tool.model_page(q, limit, offset, sort)
    return JsonResult.res_page(res, total)


# 详细信息
@baseRoute.route('/permission_group/<id>', methods=['GET'])
@require_oauth('profile')
def get_permission_group(id):
    obj = SysPermissionGroup.query.get(id)
    return JsonResult.queryResult(obj)

# 添加
@baseRoute.route('/permission_group', methods=['POST'])
@require_oauth('profile')
def add_permission_group():
    obj = SysPermissionGroup()
    args = request.get_json()
    # 将参数加载进去
    param_tool.set_dict_parm(obj, args)
    db.session.add(obj)
    db.session.commit()
    return JsonResult.success("创建成功！", {"id": obj.id})

# 更新， PUT:全部字段 ；PATCH:部分字段
@baseRoute.route('/permission_group/<id>', methods=['PUT','PATCH'])
@require_oauth('profile')
def update_permission_group(id):
    obj = SysPermissionGroup.query.get(id)
    if obj is None :
        return JsonResult.error("对象不存在，id=%s"%id)
    args = request.get_json()
    #将参数加载进去
    param_tool.set_dict_parm(obj,args)
    db.session.commit()
    return JsonResult.success("更新成功！",{"id": obj.id})

@baseRoute.route('/permission_group/<id>', methods=['DELETE'])
@require_oauth('profile')
def del_permission_group(id):
    "删除"
    obj = SysPermissionGroup.query.get(id)
    db.session.delete(obj)
    # sql = "delete from ts_meetasr_log where meetid='%s' " % meetid
    # db.session.execute(sql)
    db.session.commit()
    return JsonResult.success("删除成功！", {"id": id})



@baseRoute.route('/group_permissions/<permission_group_id>', methods=['PUT'])
@require_oauth('profile')
def update_group_permissions(permission_group_id):
    args = request.get_json()
    permission_ids = args.get("permission_ids")
    group_permissions = SysPerssionGroupRel.query.filter(SysPerssionGroupRel.permission_group_id == permission_group_id).all()
    for permission_id in permission_ids:
        # 判断数据库中是否已经存在该用户
        selected = [pr for pr in group_permissions if  pr.permission_id == permission_id]
        if len(selected) == 0:
            role_permission = SysPerssionGroupRel(permission_group_id=permission_group_id, permission_id=permission_id)
            db.session.add(role_permission)
        else:  # 已存在的角色，从user_roles中删掉，剩下的是要删除的用户
            group_permissions.remove(selected[0])
    # 删除已经不存在的数据
    [db.session.delete(group_permission) for group_permission in group_permissions]
    db.session.commit()
    permission_context.load_permission()
    return JsonResult.success("更新权限分组成功！")
