import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'z_markgo'
    OAUTH2_REFRESH_TOKEN_GENERATOR: True
    SSL_DISABLE = False

    # database
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    # log
    LOG_PATH = os.path.join(basedir, 'logs')
    LOG_PATH_INFO = os.path.join(LOG_PATH, 'user_auth.log')
    LOG_FILE_MAX_BYTES = 100 * 1024 * 1024
    LOG_FILE_BACKUP_COUNT = 10  # 轮转数量是 10 个

    # file
    ITEM_FILE_SAVE_PATH = "./items"  # 音频文件存放路径

    # module
    ENABLED_MODULES = (
        'auth',
        'permission',
        'user',
    )

    # schedule jobs
    JOBS = [
        {
            'id': 'job_check_item',
            'func': 'extensions.scheduler:job_check_project_item',
            # 'trigger': 'interval',
            # 'seconds': 60,
            'trigger': 'cron',
            'hour': 0,
            'minute': 0,
            'second': 0

        }
    ]
    # SCHEDULER_API_ENABLED = FALSE


class DevelopmentConfig(Config):
    DEBUG = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:whcxhwyz@asus.uglyxu.cn:40011/dataknown'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
