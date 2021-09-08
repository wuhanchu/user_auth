import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


class ConfigDefine:
    """配置定义"""

    # 用户服务信息
    USER_PATTERN = "USER_PATTERN"  # 用户服务模式

    USER_SERVER_URL = "USER_SERVER_URL"  # 用户服务地址
    USER_SERVER_LDAP = "USER_SERVER_LDAP"  # LDAP 服务器
    USER_SERVER_ACCOUNT = "USER_SERVER_ACCOUNT"  # LDAP服务账号
    USER_SERVER_PASSWORD = "USER_SERVER_PASSWORD"  # LDAP服务密码

    CELERY_SCHEDULE = "CELERY_SCHEDULE"  # 定时任务
    LDAP_INTERVAL_MINUTE = "LDAP_INTERVAL_MINUTE"  # 定时任务

    class UserPattern:
        standard = "standard"  # 标准
        phfund = "phfund"  # 鹏华

    # celery
    CELERY_BROKER = "CELERY_BROKER"


class Config:
    CHECK_API = False

    # project
    PRODUCT_KEY = "user_auth"
    SECRET_KEY = 'z_markgo'
    OAUTH2_REFRESH_TOKEN_GENERATOR: True
    SSL_DISABLE = False
    RUN_PORT = os.environ.get('RUN_PORT', 5000)

    # set enable
    ENABLED_EXTENSION = ["loguru", "database", "permission", "postgrest", "sentry"]

    # sentry
    SENTRY_DS = "https://c58a597cd1fb4a44b2b719f357325597@server.aiknown.cn:31027/4"

    # auth
    LICENSE_CHECK = False

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
    AUTO_UPDATE = os.environ.get('AUTO_UPDATE', False)  # 自动更新数据库
    DB_INIT_FILE = ["sql/init/table.sql", "sql/init/view.sql",
                    "sql/init/data/permission_scope.sql",
                    "sql/init/data/role.sql",
                    "sql/init/data/user.sql",
                    "sql/init/data/oauth2_client.sql",
                    "sql/init/data/user_role.sql",
                    "sql/init/data/role_permission_scope.sql",
                    "sql/init/data/param.sql"]
    DB_VERSION_FILE = ["sql/migrate/0.8_0.9.sql"]

    # 用户服务模式
    USER_PATTERN = os.environ.get(ConfigDefine.USER_PATTERN, ConfigDefine.UserPattern.standard)
    CELERY_BROKER = os.environ.get('CELERY_BROKER')


class DevelopmentConfig(Config):
    DEBUG = True

    # set enable
    ENABLED_EXTENSION = ["loguru", "database", "permission", "postgrest"]

    RUN_PORT = 5000
    PROXY_SERVER_URL = os.environ.get('PROXY_SERVER_URL', "http://server.aiknown.cn:36023")
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',
                                             'postgresql://postgres:dataknown1234@server.aiknown.cn:36021/dataknown')

    CELERY_BROKER = os.environ.get('CELERY_BROKER', "redis://:dataknown1234@server.aiknown.cn:36061")
    # AUTO_UPDATE = True  # 自动更新数据库
    FETCH_USER = False
    CHECK_API = False


class TestingConfig(Config):
    TESTING = True
    AUTO_UPDATE = True  # 自动更新数据库


class ProductionConfig(Config):
    AUTO_UPDATE = True  # 自动更新数据库


class DevelopmentPhfundConfig(DevelopmentConfig):
    """鹏华的运行配置"""

    USER_PATTERN = os.environ.get(ConfigDefine.USER_PATTERN, ConfigDefine.UserPattern.phfund)  # 用户服务模式
    USER_SERVER_URL = os.environ.get(ConfigDefine.USER_SERVER_URL, "http://passport.dev.phfund.com.cn")  # 独立用户服务地址
    USER_SERVER_LDAP = os.environ.get(ConfigDefine.USER_SERVER_LDAP, "ad.phfund.com.cn")
    USER_SERVER_ACCOUNT = os.environ.get(ConfigDefine.USER_SERVER_ACCOUNT, "x_wuhanchu")
    USER_SERVER_PASSWORD = os.environ.get(ConfigDefine.USER_SERVER_PASSWORD, "DATAknown1234")
    from celery.schedules import crontab
    CHECK_API = False
    FETCH_USER = False

    # module
    ENABLED_MODULE = [
        'permission',
        'user',
        'role',
        'auth',
        'license',
        'phfund'
    ]

    # schedule jobs
    minutes = int(os.environ.get(ConfigDefine.LDAP_INTERVAL_MINUTE, 1))
    CELERY_SCHEDULE = {
        "user_job_sync_ldap": {
            "task": "module.phfund.task.job_sync_ldap",
            "schedule": timedelta(minutes=minutes)
        },
    }


class ProductionPhfundConfig(DevelopmentPhfundConfig):
    """鹏华的运行配置"""
    USER_PATTERN = os.environ.get(ConfigDefine.USER_PATTERN, ConfigDefine.UserPattern.phfund)  # 用户服务模式
    USER_SERVER_URL = os.environ.get(ConfigDefine.USER_SERVER_URL, "https://auth.phfund.com.cn")  # 独立用户服务地址


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'development_phfund': DevelopmentPhfundConfig,
    'production_phfund': ProductionPhfundConfig,
    'default': DevelopmentConfig
}
