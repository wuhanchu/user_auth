from distutils.util import strtobool
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

    LDAP_INTERVAL_MINUTE = "LDAP_INTERVAL_MINUTE"  # 定时任务

    class UserPattern:
        standard = "standard"  # 标准
        phfund = "phfund"  # 鹏华

    # celery
    CELERYBEAT_SCHEDULE = "CELERYBEAT_SCHEDULE"  # 定时任务
    CELERY_BROKER = "CELERY_BROKER"


class Config:
    CHECK_API = bool(strtobool(os.environ.get("CHECK_API", "False")))
    CHECK_PASSWORD = bool(strtobool(os.environ.get("CHECK_PASSWORD", "True")))
    CORE_NUM = os.environ.get("CORE_NUM", 5)

    # project
    PRODUCT_KEY = "user_auth"
    SECRET_KEY = "user_auth"
    OAUTH2_REFRESH_TOKEN_GENERATOR: True
    SSL_DISABLE = False
    RUN_PORT = os.environ.get("RUN_PORT", 5000)

    # set enable
    ENABLED_EXTENSION = [
        "loguru",
        "marshmallow",
        "lock",
        "redis",
        "database",
        "postgrest",
        "celery",
    ]

    # sentry
    SENTRY_DS = "https://5b16ef46c2194f74822702c15375331f@asus.uglyxu.cn:31001/10"
    SENTRY_ENVIRONMENT = os.environ.get("SENTRY_ENVIRONMENT", "production")

    # auth
    LICENSE_CHECK = False

    # module
    ENABLED_MODULE = ["user", "role", "auth", "license"]

    # posrgrest
    PROXY_SERVER_URL = os.environ.get("PROXY_SERVER_URL")
    DB_POOL_SIZE = (
        int(os.environ.get("DB_POOL_SIZE")) if os.environ.get("DB_POOL_SIZE") else None
    )
    DB_MAX_OVERFLOW = (
        int(os.environ.get("DB_MAX_OVERFLOW"))
        if os.environ.get("DB_MAX_OVERFLOW")
        else None
    )

    # database
    DB_SCHEMA = "user_auth"
    DB_VERSION = os.environ.get("DB_VERSION")
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    AUTO_UPDATE = os.environ.get("AUTO_UPDATE", False)  # 自动更新数据库
    DB_INIT_FILE = [
        "sql/init/table.sql",
        "sql/init/data/department.sql",
        "sql/init/data/user.sql",
        "sql/init/data/oauth2_client.sql",
        "sql/init/data/param.sql",
    ]
    DB_UPDATE_FILE = [
        "sql/init/data/permission_scope.sql",
        "sql/init/data/role.sql",
        "sql/init/data/user_role.sql",
        "sql/init/data/role_permission_scope.sql",
        "sql/init/view.sql",
        "sql/init/data/config.sql",
    ]

    DB_UPDATE_SWITCH = os.environ.get("DB_UPDATE_SWITCH", False)  # 自动运行更新文件开开关

    # 用户服务模式
    USER_PATTERN = os.environ.get(
        ConfigDefine.USER_PATTERN, ConfigDefine.UserPattern.standard
    )

    # reids
    REDIS_URL = os.environ.get("REDIS_URL")
    REDIS_MASTER_NAME = os.environ.get("REDIS_MASTER_NAME")

    # celery
    CELERY_DEFAULT_QUEUE = PRODUCT_KEY
    PROXY_LOCAL = bool(strtobool(os.environ.get("PROXY_LOCAL", "False")))


class DevelopmentConfig(Config):
    DEBUG = False

    RUN_PORT = os.environ.get("RUN_PORT", 31502)
    PROXY_SERVER_URL = os.environ.get("PROXY_SERVER_URL", "http://192.168.1.152:36023")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI",
        "postgresql://postgres:dataknown1234@192.168.1.152:36021/dataknown",
    )

    REDIS_URL = os.environ.get(
        "REDIS_URL", "redis://:dataknown1234@192 .168.1.152:36061"
    )
    REDIS_MASTER_NAME = os.environ.get("REDIS_MASTER_NAME", "mymaster")


class TestingConfig(Config):
    TESTING = True
    AUTO_UPDATE = True  # 自动更新数据库
    ENABLED_EXTENSION = Config.ENABLED_EXTENSION + ["sentry"]
    SENTRY_ENVIRONMENT = os.environ.get("SENTRY_ENVIRONMENT", "testing")

    DB_UPDATE_SWITCH = bool(
        strtobool(os.environ.get("DB_UPDATE_SWITCH", "True"))
    )  # 自动运行更新文件开开关


class ProductionConfig(Config):
    AUTO_UPDATE = True  # 自动更新数据库
    DB_UPDATE_SWITCH = os.environ.get("DB_UPDATE_SWITCH", True)  # 自动运行更新文件开开关


class DevelopmentPhfundConfig(DevelopmentConfig):
    """鹏华的运行配置"""

    USER_PATTERN = os.environ.get(
        ConfigDefine.USER_PATTERN, ConfigDefine.UserPattern.phfund
    )  # 用户服务模式
    USER_SERVER_URL = os.environ.get(
        ConfigDefine.USER_SERVER_URL, "http://passport.dev.phfund.com.cn"
    )  # 独立用户服务地址
    USER_SERVER_LDAP = os.environ.get(ConfigDefine.USER_SERVER_LDAP, "ad.phfund.com.cn")
    USER_SERVER_ACCOUNT = os.environ.get(ConfigDefine.USER_SERVER_ACCOUNT, "x_wuhanchu")
    USER_SERVER_PASSWORD = os.environ.get(
        ConfigDefine.USER_SERVER_PASSWORD, "DATAknown1234"
    )

    FETCH_USER = False

    # module
    ENABLED_MODULE = ["user", "role", "auth", "license", "phfund"]

    # schedule jobs
    minutes = int(os.environ.get(ConfigDefine.LDAP_INTERVAL_MINUTE, 1))
    CELERYBEAT_SCHEDULE = {
        "user_job_sync_ldap": {
            "task": "module.phfund.task.job_sync_ldap",
            "schedule": timedelta(minutes=minutes),
        },
    }


class ProductionPhfundConfig(DevelopmentPhfundConfig):
    """鹏华的运行配置"""

    USER_PATTERN = os.environ.get(
        ConfigDefine.USER_PATTERN, ConfigDefine.UserPattern.phfund
    )  # 用户服务模式
    USER_SERVER_URL = os.environ.get(
        ConfigDefine.USER_SERVER_URL, "https://auth.phfund.com.cn"
    )  # 独立用户服务地址


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
    "development_phfund": DevelopmentPhfundConfig,
    "production_phfund": ProductionPhfundConfig,
    "default": DevelopmentConfig,
}
