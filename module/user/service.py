# -*- coding:utf-8 -*-

from flask_frame.api.response import queryToDict
from flask_frame.extension.database import db, db_schema


def get_user_extend_info(user_record):
    """
    convert user_record to user
    :param user_record: user database record
    :return:
    """

    user = queryToDict(user_record)
    user.pop("password")
    user.pop("del_fg")
    user.pop("token")

    append_permission(user)
    append_permission_scope(user)

    return user


def append_permission(data):
    sql = (
        f"""
            SET search_path to {db_schema};
            select 
                   p.product_key,
                   p.name,
                   p.url,
                   p.method,
                   p.key,
                   string_agg(cast(r.id as text), ',') as role_id,
                   string_agg(r.name, ',')             as role_name
            from permission p
                     join permission_scope_detail rel on rel.permission_key = p.key and rel.product_key = p.product_key
                     join role_permission_scope gr on gr.permission_scope_key = rel.permission_scope_key and rel.product_key_scope = gr.product_key
                     join role r on r.id = gr.role_id
                     join user_role ur on r.id = ur.role_id
            where ur.user_id = '%s'
            group by p.product_key,p.name, p.url, p.method, p.key;
        """
        % data["id"]
    )

    res = db.session.execute(sql).fetchall()
    db.session.close()

    data["permissions"] = queryToDict(res)

    # 增加不存在的权限
    no_sql = (
        f"""
            SET search_path to {db_schema};
            select 
                   permission.product_key,
                   permission.name,
                   permission.url,
                   permission.method,
                   permission.key
            from permission where (product_key, key)  not in (
                select p.product_key,p.key
                from permission p
                        join permission_scope_detail rel on rel.permission_key = p.key and rel.product_key = p.product_key
                        join role_permission_scope gr on gr.permission_scope_key = rel.permission_scope_key and rel.product_key_scope = gr.product_key
                        join role r on r.id = gr.role_id
                        join user_role ur on r.id = ur.role_id
                where ur.user_id = '%s'
                group by p.product_key,p.name, p.url, p.method, p.key);
        """
        % data["id"]
    )

    res = db.session.execute(no_sql).fetchall()
    db.session.close()

    data["no_permissions"] = queryToDict(res)


def append_permission_scope(data):
    sql_group = (
        f"""
                SET search_path to {db_schema};                    
                select grp.product_key, grp.name, grp.key
                from permission_scope grp
                         join role_permission_scope grole on grp.key = grole.permission_scope_key and grp.product_key = grole.product_key
                         join role r on r.id = grole.role_id
                         join user_role ur on r.id = ur.role_id
                where ur.user_id = '%s'
                """
        % data["id"]
    )

    res_group = db.session.execute(sql_group).fetchall()
    db.session.close()
    data["permission_scopes"] = queryToDict(res_group)
