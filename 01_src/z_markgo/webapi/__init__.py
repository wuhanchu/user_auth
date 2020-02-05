from flask import Blueprint
from base.webapi import DEFAULT_MODULES

#定义蓝图
markRoute = Blueprint('mark', __name__, url_prefix='/api/v1/mark')
DEFAULT_MODULES.append(markRoute)

