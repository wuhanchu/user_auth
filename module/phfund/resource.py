# -*- coding:utf-8 -*-
from celery_once import AlreadyQueued
from flask import current_app

from . import blueprint
from .task import job_sync_ldap
from frame.http.response import http_response_schema

print("init phfund user resource")


@blueprint.route('/user/sync', methods=['POST'])
def user_sync():
    try:
        # 创建任务
        job_sync_ldap.delay()
    except AlreadyQueued as e:
        current_app.logger.warn("user_sync AlreadyQueued:" + str(e))
    finally:
        # 返回
        return http_response_schema.dumps({"message": "已创建同步任务，请等待几分钟后刷新！"})
