import json

from celery_once import QueueOnce

from extension.celery import celery
# from celery_once import QueueOnce
from extension.ldap import LadpServer


@celery.task(base=QueueOnce)
def job_sync_ldap():
    """
    同步鹏华 ldap 的用户信息
    """
    from extension.celery import flask_app

    from config import ConfigDefine

    operation = LadpServer(flask_app.config.get(ConfigDefine.USER_SERVER_LDAP),
                           flask_app.config.get(ConfigDefine.USER_SERVER_ACCOUNT),
                           flask_app.config.get(ConfigDefine.USER_SERVER_PASSWORD))

    department_list = operation.get_all_group_info()
    user_list = operation.get_all_user_info(department_list)
    sync_data(department_list, user_list)


def sync_data(department_list, user_list):
    """"""
    from extension.celery import flask_app

    from module.phfund.schema import UserSchema
    from module.phfund.schema import DepartmentSchema
    from frame.extension.database import db
    from module.user.model import User
    from module.user.model import Department

    department_list = DepartmentSchema(many=True).load(department_list)
    department_list = [item for item in department_list if "user" not in
                       json.loads(item.remark).get("objectClass")]
    user_list = UserSchema(many=True).load([item for item in user_list if len(item.get("name")) <= 32])

    # 使用
    department_map = {}
    for item in department_list:
        data = json.loads(item.remark)
        if data.get("distinguishedName").startswith("CN="):
            department_map[data.get("distinguishedName")] = item
        else:
            department_map[f'CN={data.get("name")},{data.get("distinguishedName")}'] = item

    # 循环生成 key
    for item in department_list:
        try:
            item.key = create_key(item, department_map)
            record = Department.query.filter_by(source='phfund', external_id=item.external_id).first()
            if record:
                item.id = record.id
                db.session.merge(item)
            else:
                db.session.add(item)

            db.session.commit()
        except Exception as e:
            db.session.rollback()
            flask_app.logger.error(e)

    # 处理用户
    for item in user_list:
        try:
            data = json.loads(item.remark)
            if data.get("memberOf") and len(data.get("memberOf")) >= 1:
                item.department_key = [department_map[item].key for item in data.get("memberOf") if
                                       department_map.get(item)]
            else:
                continue

            # 没有所属机构不处理
            if not item.loginid or (
                    not item.loginid.startswith("x_") and (not item.department_key or len(item.department_key) < 1)):
                continue

            record = User.query.filter_by(source='phfund', external_id=item.external_id).first()
            if record:
                item.id = record.id
                db.session.merge(item)
            elif item.enable:
                db.session.add(item)

            db.session.commit()
        except Exception as e:
            db.session.rollback()
            flask_app.logger.error(e)


def get_members(item, department_map):
    result = [item]

    if not item:
        return result

    data = json.loads(item.remark)
    if not data.get("member"):
        return result

    for member_key in data.get("member"):
        member = department_map.get(member_key)
        if member:
            result = result + get_members(member, department_map)

    return result


def create_key(item, department_map):
    """生成部门 key"""
    if not item:
        return ""

    data = json.loads(item.remark)
    return "_".join(data.get("distinguishedName").split(",")[::-1]).replace(",OU=", "_OU=")
