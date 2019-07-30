import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SSL_DISABLE = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    LOG_PATH = os.path.join(basedir, 'logs')
    LOG_PATH_INFO = os.path.join(LOG_PATH, 'python_demo.log')
    LOG_FILE_MAX_BYTES = 100 * 1024 * 1024
    # 轮转数量是 10 个
    LOG_FILE_BACKUP_COUNT = 10

    @staticmethod
    def init_app(cls,app):
        app.config.from_object(cls)
        # pass

class DevelopmentConfig(Config):
    DEBUG = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@192.168.1.150:3306/python_demo?charset=utf8'

    @classmethod
    def init_app(cls, app):
        Config.init_app(cls, app)

        # email errors to the administrators
        import logging
        from logging.handlers import RotatingFileHandler
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s %(levelname)s %(process)d '
            '%(pathname)s %(lineno)s : %(message)s')

        # FileHandler
        file_handler_info = RotatingFileHandler(filename=cls.LOG_PATH_INFO)
        file_handler_info.setFormatter(formatter)
        # file_handler_info.setLevel(logging.INFO)
        app.logger.addHandler(file_handler_info)





class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    WTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}