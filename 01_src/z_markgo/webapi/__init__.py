from flask import Flask,Blueprint
import os
app = Flask(__name__,root_path=os.getcwd())

#定义蓝图
baseRoute = Blueprint('base', __name__, url_prefix='/api/v1')
markRoute = Blueprint('base', __name__, url_prefix='/api/v1/mark')
DEFAULT_MODULES = [baseRoute,markRoute]

