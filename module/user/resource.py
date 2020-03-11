# -*- coding:utf-8 -*-
from authlib.integrations.flask_oauth2 import current_token
from flask import request, jsonify
from sqlalchemy import func, Text

from frame.http.JsonResult import JsonResult, queryToDict
from frame.util import com_tool, sql_tool, param_tool
from module.auth.extension.oauth2 import require_oauth
from module.user.model import *
from . import blueprint


@blueprint.route('', methods=['GET'])
@require_oauth('profile')
def user_list():
    """
    用户列表
    :return:
    """
    id = request.args.get("id")
    if id:
        return get_user(id)

    q = db.session.query(User.id, func.max(User.name).label("name"),
                         func.max(User.loginid).label("loginid"), func.max(User.telephone) \
                         .label("telephone"), func.max(User.address).label("address"),
                         func.string_agg(func.cast(Role.id, Text), ',').label("roles")) \
        .outerjoin(UserRole, UserRole.user_id == User.id) \
        .outerjoin(Role, Role.id == UserRole.role_id).group_by(User.id)

    name = request.args.get("name")
    if name is not None:
        q = q.filter(User.name.like("%" + name + "%"))
    # q = q.order_by(User.name.desc())
    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    sort = request.args.get('sort')
    if sort == None:
        sort = "-id"
    res, total = sql_tool.model_page(q, limit, offset, sort)
    return JsonResult.res_page(res, total)


def get_user(id):
    """
    详细用户信息
    :param id:
    :return:
    """
    obj = User.query.get(id)
    return JsonResult.queryResult(obj)


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
    except Exception as e:
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


@blueprint.route('/role', methods=['PUT'])
@require_oauth('profile')
def update_user_roles():
    data = request.get_json()
    user_id = request.args.get("id")
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

    list = Role.query.join(UserRole, UserRole.role_id == Role.id).filter(
        UserRole.user_id == user_id).all()
    return JsonResult.queryResult(list)


@blueprint.route('/current', methods=['GET'])
@require_oauth('profile')
def current_user():
    if current_token:
        user = current_token.user
        user = queryToDict(user)
        user.pop("password")
        user.pop("del_fg")
        user.pop("token")
        sql = f"""
            SET search_path to {db_schema};
            select p.name,
                   p.url,
                   p.method,
                   p.key,
                   string_agg(cast(r.id as text), ',') as role_id,
                   string_agg(r.name, ',')             as role_name
            from permission p
                     join permission_scope_detail rel on rel.permission_key = p.key
                     join role_permission_scope gr on gr.permission_scope_key = rel.permission_scope_key
                     join role r on r.id = gr.role_id
                     join user_role ur on r.id = ur.role_id
            where ur.user_id = '%s'
            group by p.name, p.url, p.method, p.key;
        """ % user["id"]

        res = db.session.execute(sql).fetchall()
        user["permissions"] = queryToDict(res)
        sql_group = f"""
                SET search_path to {db_schema};                    
                select grp.name, grp.key
                from permission_scope grp
                         join role_permission_scope grole on grp.key = grole.permission_scope_key
                         join role r on r.id = grole.role_id
                         join user_role ur on r.id = ur.role_id
                where ur.user_id = '%s'
                """ % user["id"]

        res_group = db.session.execute(sql_group).fetchall()
        user["permission_scopes"] = queryToDict(res_group)
        return jsonify(user)
    else:
        return JsonResult.error()
