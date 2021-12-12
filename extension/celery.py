from celery import Celery

from config import ConfigDefine

celery = None
flask_app = None


def init_app(app):
    global celery
    global flask_app
    flask_app = app

    # 增加work
    celery = Celery(
        "tasks",
        backend=app.config.get("CELERY_BROKER"),
        broker=app.config.get("CELERY_BROKER"),
    )

    # 增加定时任务
    celery.config_from_object(
        {
            "CELERY_TIMEZONE": "Asia/Shanghai",
            "ENABLE_UTC": True,
            "redbeat_key_prefix": app.config.get("PRODUCT_KEY"),
            "redbeat_redis_url": app.config.get("CELERY_BROKER"),
            **app.config,
        }
    )
