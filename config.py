import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # project
    PRODUCT_KEY = "user_auth"
    SECRET_KEY = 'z_markgo'
    OAUTH2_REFRESH_TOKEN_GENERATOR: True
    SSL_DISABLE = False
    RUN_PORT = os.environ.get('RUN_PORT', 5000)

    # set enable
    ENABLED_EXTENSION = ["loguru", "database", "postgrest", "permission"]

    # module
    ENABLED_MODULE = [
        'permission',
        'user',
        'role',
        'auth',
        'license'
    ]

    # permission config
    USER_AUTH_LOCAL = True

    # posrgrest
    PROXY_SERVER_URL = os.environ.get('PROXY_SERVER_URL')

    # database
    DB_SCHEMA = "user_auth"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

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


class DevelopmentConfig(Config):
    DEBUG = True
    RUN_PORT = 5000
    PROXY_SERVER_URL = "http://asus.uglyxu.cn:40014"
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',
                                             'postgresql://dataknown:dataknown1234@asus.uglyxu.cn:40011/dataknown')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',
                                             'postgresql://dataknown:dataknown1234@asus.uglyxu.cn:40011/dataknown')
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
