from celery import Celery

from config import ConfigDefine

celery = None
flask_app = None


def init_app(app):
    global celery
    global flask_app
    flask_app = app

    celery = Celery('tasks', backend=app.config.get("CELERY_BROKER"), broker=app.config.get("CELERY_BROKER"))
    celery.conf.ONCE = {
        'backend': 'celery_once.backends.Redis',
        'settings': {
            'url': app.config.get("CELERY_BROKER") + '/0'
        }
    }


def load_periodic_tasks():
    """加载定时任务"""
    if flask_app.config.get(ConfigDefine.CELERY_SCHEDULE):
        celery.conf.update(timezone='Asia/Shanghai',
                           enable_utc=True, beat_schedule=flask_app.config.get(ConfigDefine.CELERY_SCHEDULE))
