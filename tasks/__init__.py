# -*- coding: utf-8 -*-
from invoke import task

from frame.app import create_app
from frame.tasks import database


@task
def api_init(c):
    app = create_app()

    import module
    module.init_app(app)

    print(app.url_map)

    database.api_init(app, [{"name": "角色", "key": "role"}, {"name": "用户", "key": "user"},
                            {"name": "客户端", "key": "oauth2_client"}, {"name": "接口", "key": "permission"},
                            {"name": "功能", "key": "permission_scope"}])
