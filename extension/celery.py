from celery import Celery

celery = None


def init_app(app):
    global celery

    celery = Celery('tasks', backend=app.config.get("CELERY_BROKER"), broker=app.config.get("CELERY_BROKER"))
