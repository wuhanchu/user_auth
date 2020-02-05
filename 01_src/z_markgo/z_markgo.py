import os
from config import config
from flask import request
from base.lib.busi_exception import BusiError
from webapi import mark_project_api, tools_api, ai_service_api, \
    mark_project_item_api, mark_project_user_api, mark_user_items_api
from base.webapi import app, DEFAULT_MODULES,base_user_api,base_menu_api,base_permission_api,base_permission_menu_api,\
    base_role_api,oauth2_server_api,register_api,permission_group_api
from dao.models import db
from base.lib.oauth2 import config_oauth
from flask_apscheduler import APScheduler
from authlib.flask.error import _HTTPException
import logging,traceback,json
logger = logging.getLogger('flask.app')
# 加载配置文件
os.environ['AUTHLIB_INSECURE_TRANSPORT'] = '1'

def init_config(config_name):
    # 加载config参数
    config[config_name].init_app(app)
    return app

@app.errorhandler(404)
def page_not_found(error):
    logger.error("url:%s,%s"%(request.base_url,error.description))
    return "url:%s,%s"%(request.base_url,error.description)

# 全局异常处理
@app.errorhandler(Exception)
def exception_handle(error):
    logger.exception(error)
    if isinstance(error,BusiError):
        return error
    else:
        if isinstance(error,_HTTPException):
            if error.code == 401 or error.code == 403:
                body = json.loads(error.body)
                return BusiError(body["error"], code=error.code)
            else:
                return BusiError(error.body, code=error.code)
        else:
            return BusiError(error.__str__(),traceback=traceback.format_exc())

@app.route('/', methods=['GET'])
def index():
    return "markgo is running"


# @app.errorhandler(404)
# def page_not_found(error):
#     return app.send_static_file('index.html')


if __name__ == '__main__':
    # 初始化log

    # 初始化app
    init_config("development")
    # 初始化sqlalchemy--begin
    db.init_app(app)
    # 初始化sqlalchemy--end

    # 注册蓝图
    for module in DEFAULT_MODULES:
        print("Blueprint regist %s !" % module.name)
        app.register_blueprint(module)

    # 加载oauth2认证模块
    config_oauth(app)

    #添加定时任务模块 -- begin
    # scheduler = APScheduler()
    # scheduler.init_app(app=app)
    # scheduler.start()
    # scheduler.add_job(id="tem1",func=busi_init, args=('一次性任务',), next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=15))
    #添加定时任务模块 -- end

    # 启动web服务

    app.run('0.0.0.0',use_reloader=False, port=5002)
