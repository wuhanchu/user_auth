# -*- coding: UTF-8 -*-

import os

from frame.util.py_utils import import_dir


def init_app(app, **kwargs):
    import_dir(os.path.dirname(__file__), __name__)
