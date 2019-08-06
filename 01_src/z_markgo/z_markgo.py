from config import config
from flask import render_template
from webapi import app,DEFAULT_MODULES,base_user_api,mark_project_api,ai_service_api,mark_project_item_api,mark_project_user_api,mark_user_items_api
from lib.models import db
from dao import mark_dao
from lib import asr_thread_pool
from flask_apscheduler import APScheduler

# 加载配置文件
def init_config(config_name):
    # 加载config参数
    config[config_name].init_app(app)
    return app

# 初始化任务
def busi_init():
    projects = mark_dao.get_all_asr_items()
    for proj in projects.keys():
        asr_thread_pool.batch_add_items(proj,projects[proj])

@app.route('/', methods=['GET'])
def index():
    app.logger.info("my first logging")
    return render_template('index.html')


if __name__ == '__main__':
    #初始化app
    init_config("development")
    # 初始化sqlalchemy--begin
    db.init_app(app)
    # 初始化sqlalchemy--end

    #添加定时任务模块 -- begin
    # scheduler = APScheduler()
    # scheduler.init_app(app=app)
    # scheduler.start()
    #添加定时任务模块 -- end

    # 注册蓝图
    for module in DEFAULT_MODULES:
        print("Blueprint regist %s !" % module.name)
        app.register_blueprint(module)

    #启动web服务
    app.run('0.0.0.0', port=5000)
