import requests

from extension.celery import celery
from module.user.schema import PhfundUserSchema


@celery.task()
def user_sync():
    """ 用户同步 """
    from frame.extension.database import db

    response = requests.get("http://passport.dev.phfund.com.cn/user/operation/detail_info")
    data = response.json()

    user_record_list = PhfundUserSchema(many=True).load(data)
    db.session.bulk_save_objects(user_record_list)
    db.session.commit()

    pass
