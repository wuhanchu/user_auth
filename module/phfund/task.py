import json

from celery_once import QueueOnce

from extension.celery import celery


# from celery_once import QueueOnce


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

    from module.user.model import Department
    try:

        # operation = LadpServer("ad.phfund.com.cn", "linchengcao", "Qq1612226490@")
        # department_list = operation.get_all_group_info()
        # user_list = operation.get_all_user_info()
        with open("test/data/group.json") as file_obj:
            department_list = json.load(file_obj)
            department_list = DepartmentSchema(many=True).load(department_list)
        with open("test/data/user.json") as file_obj:
            user_list = json.load(file_obj)
            user_list = UserSchema(many=True).load([item for item in user_list if len(item.get("name")) <= 32])

        # 使用
        department_map = {}
        for item in department_list:
            data = json.loads(item.remark)
            department_map[data.get("distinguishedName")] = item

        # 循环生成 key
        for item in department_list:
            item.key = create_key(item, department_map)
            record = Department.query.filter_by(source='phfund', external_id=item.external_id).first()
            if record:
                item.id = record.id
                db.session.merge(item)
            else:
                db.session.add(item)

        # db.session.commit()

        # 处理用户
        cumulative_number = 0  # 累计处理数目
        for item in user_list:

            data = json.loads(item.remark)
            if data.get("memberOf") and len(data.get("memberOf")) >= 1:
                item.department_key = [department_map[item].key for item in data.get("memberOf")]

            record = User.query.filter_by(source='phfund', external_id=item.external_id).first()
            if record:
                item.id = record.id
                db.session.merge(item)
            else:
                db.session.add(item)

            # 定量提交
            cumulative_number += 1
            if cumulative_number % 100 == 0:
                db.session.commit()
                cumulative_number = 0

        db.session.commit()
    except Exception as e:
        flask_app.logger.error(e)
        db.session.rollback()


def create_key(item, department_map):
    """生成部门 key"""
    data = json.loads(item.remark)
    if not data.get("memberOf") or len(data.get("memberOf")) < 1:
        return item.external_id
    elif len(data.get("memberOf")) >= 1:
        key_father = create_key(department_map.get(data.get("memberOf")[0]), department_map)
        return (key_father + "_" if key_father else "") + item.external_id
