# -*- coding: utf-8 -*-

from flask_apscheduler import APScheduler

scheduler_job = APScheduler()
flask_app = None
init = False





def init_app(app):
    """
    init from app
    """

    global scheduler_job, flask_app, init
    flask_app = app

    if not init:
        scheduler_job.init_app(app)
        scheduler_job.start()
        init = True
