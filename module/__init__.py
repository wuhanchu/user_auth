# encoding: utf-8
"""
Modules
=======

Modules enable logical resource separation.

You may control enabled modules by modifying ``ENABLED_MODULES`` config
variable.
"""
from flask import Blueprint

blueprint_main = Blueprint('main', __name__)


def init_app(app, **kwargs):
    from importlib import import_module

    for module_name in app.config['ENABLED_MODULE']:
        import_module('.%s' % module_name,
                      package=__name__).init_app(app, **kwargs)

    app.register_blueprint(blueprint_main)


def get_user_pattern():
    """当前的用户获取模式"""
    from run import app
    from config import ConfigDefine

    return app.config.get(ConfigDefine.USER_PATTERN)
