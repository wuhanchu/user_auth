# -*- coding: UTF-8 -*-

import os

from flask import Blueprint

from frame.util.py_utils import import_dir

blueprint = Blueprint('role', __name__, url_prefix='/role')


def init_app(app, **kwargs):
    import_dir(os.path.dirname(__file__), __name__)
    app.register_blueprint(blueprint)
