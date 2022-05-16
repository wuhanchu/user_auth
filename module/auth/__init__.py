# -*- coding: UTF-8 -*-

import os

from flask import Blueprint

from flask_frame.util.py_utils import import_dir

blueprint = Blueprint('auth', __name__, url_prefix='/auth')


def init_app(app, **kwargs):
    import_dir(os.path.dirname(__file__), __name__)

    # 加载oauth2认证模块
    from .extension.oauth2 import init_app
    init_app(app)

    app.register_blueprint(blueprint)
