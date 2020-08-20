# encoding: utf-8
from extension import celery
from extension import marshmallow

from frame.app import create_app
import argparse
import module

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--celery', action="store_true")

# 初始化
app = create_app()
celery.init_app(app)
marshmallow.init_app(app)
module.init_app(app)

if __name__ == '__main__':

    args = parser.parse_args()
    if args.celery:
        print("celery work")
        from extension.celery import celery
        celery.worker_main(['worker'])
    else:
        app.run('0.0.0.0', port=app.config.get("RUN_PORT"), threaded=False)
