# -*- coding: UTF-8 -*-

import os

from flask import Blueprint

from frame.util.py_utils import import_dir

blueprint = Blueprint('permission', __name__, url_prefix='/permission')


def init_app(app, **kwargs):
    import_dir(os.path.dirname(__file__), __name__)
    from . import resource
    app.register_blueprint(blueprint)
