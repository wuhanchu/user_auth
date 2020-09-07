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

    from module.phfund.schema import UserSchema
    from module.phfund.schema import DepartmentSchema
    from frame.extension.database import db
    from module.user.model import User
    from config import ConfigDefine
    from module.user.model import Department

    operation = LadpServer(flask_app.config.get(ConfigDefine.USER_SERVER_LDAP),
                           flask_app.config.get(ConfigDefine.USER_SERVER_ACCOUNT),
                           flask_app.config.get(ConfigDefine.USER_SERVER_PASSWORD))

    department_list = operation.get_all_group_info()
    user_list = operation.get_all_user_info()

    # with open("test/data/group.json") as file_obj:
    #     department_list = json.load(file_obj)
    # with open("test/data/user.json") as file_obj:
    #     user_list = json.load(file_obj)

    department_list = DepartmentSchema(many=True).load(department_list)
    user_list = UserSchema(many=True).load([item for item in user_list if len(item.get("name")) <= 32])

    # 使用
    department_map = {}
    for item in department_list:
        data = json.loads(item.remark)
        department_map[data.get("distinguishedName")] = item

    department_list = get_members(department_map.get("CN=鹏华基金管理有限公司,OU=邮件群组,OU=鹏华基金,DC=ad,DC=phfund,DC=com,DC=cn"),
                                  department_map)

    department_map = {}
    for item in department_list:
        data = json.loads(item.remark)
        department_map[data.get("distinguishedName")] = item

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

            record = User.query.filter_by(source='phfund', external_id=item.external_id).first()
            if record:
                item.id = record.id
                db.session.merge(item)
            else:
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
    if not data.get("memberOf") or len(data.get("memberOf")) < 1:
        return item.external_id

    elif len(data.get("memberOf")) >= 1:
        member_key_real = None
        for member_key in data.get("memberOf"):
            if department_map.get(member_key):
                member_key_real = member_key
                break

        key_father = create_key(department_map.get(member_key_real), department_map)
        return (key_father + "_" if key_father else "") + item.external_id
