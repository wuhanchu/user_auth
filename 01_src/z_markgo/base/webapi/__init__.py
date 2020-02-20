from flask import Flask,Blueprint
import os
app = Flask(__name__,root_path=os.getcwd())

#定义蓝图
baseRoute = Blueprint('base', __name__, url_prefix='/api/v1')
oauth_server = Blueprint('oauth_server',__name__,url_prefix='/oauth' )

DEFAULT_MODULES = [baseRoute,oauth_server]

