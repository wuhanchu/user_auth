# -*- coding: UTF-8 -*-

import os

from flask import Blueprint

from frame.py_utils import import_dir

blueprint = Blueprint('blueprint_oauth', __name__, url_prefix='/auth')


def init_app(app, **kwargs):
    import_dir(os.path.dirname(__file__), __name__)
    app.register_blueprint(blueprint)

    # 加载oauth2认证模块
    from .extension.oauth2 import config_oauth
    config_oauth(app)
