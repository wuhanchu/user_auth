from config import config
from flask import render_template
from webapi import app,DEFAULT_MODULES,base_user_api,mark_project_api
from lib.models import db


def init_config(config_name):
    # 加载config参数
    config[config_name].init_app(app)
    return app


@app.route('/', methods=['GET'])
def index():
    app.logger.info("my first logging")
    return render_template('index.html')


if __name__ == '__main__':
    #初始化app
    init_config("development")
    # 初始化sqlalchemy
    db.init_app(app)
    # 注册蓝图
    for module in DEFAULT_MODULES:
        print("Blueprint regist %s !" % module.name)
        app.register_blueprint(module)
    app.run('0.0.0.0', port=5000)
