from flask import Flask,Blueprint
import os
app = Flask(__name__,root_path=os.getcwd())

#定义蓝图
baseRoute = Blueprint('base', __name__, url_prefix='/api/v1')
markRoute = Blueprint('mark', __name__, url_prefix='/api/v1/mark')
oauth_server = Blueprint('oauth_server',__name__,url_prefix='/oauth' )
DEFAULT_MODULES = [baseRoute,markRoute,oauth_server]

