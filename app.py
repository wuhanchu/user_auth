import logging
import os

from flask import Flask

from config import config

logger = logging.getLogger('mark_go_app')


def create_app(flask_config_name="default", **kwargs):
    """
    create the app
    :param flask_config_name:
    :param kwargs:
    :return:
    """
    flask_app = Flask(__name__, root_path=os.getcwd())

    # 初始化app
    config_name = os.getenv('FLASK_CONFIG', flask_config_name)
    flask_app.config.from_object(config[config_name])

    # 加载配置文件
    os.environ['AUTHLIB_INSECURE_TRANSPORT'] = '1'

    # config log
    import logging
    from logging.handlers import RotatingFileHandler
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s %(process)d '
        '%(pathname)s %(lineno)s : %(message)s')

    log_path = flask_app.config.get("LOG_PATH_INFO")
    if not os.path.exists(os.path.dirname(log_path)):
        os.makedirs(os.path.dirname(log_path))

    file_handler_info = RotatingFileHandler(filename=log_path)
    file_handler_info.setFormatter(formatter)
    flask_app.logger.addHandler(file_handler_info)

    # 数据库初始化
    from extension import db
    db.init_app(flask_app)

    #  init module
    import module
    module.init_app(flask_app)

    return flask_app


app = create_app()

if __name__ == '__main__':
    # 启动web服务
    app.run('0.0.0.0', port=5000, threaded=False)
