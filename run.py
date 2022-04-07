# encoding: utf-8
import os

from extension import celery
from extension import marshmallow

from frame.app import create_app
import argparse
import module

if "gaussdb" in os.environ.get("SQLALCHEMY_DATABASE_URI", ""):
    from sqlalchemy.dialects.postgresql.base import PGDialect

    PGDialect._get_server_version_info = lambda *args: (9, 2)

parser = argparse.ArgumentParser(description="manual to this script")
parser.add_argument("--celery", action="store_true")
parser.add_argument("--beat", action="store_true")

# 初始化
app = create_app()
marshmallow.init_app(app)
celery.init_app(app)

module.init_app(app)

print(app.url_map)


if __name__ == "__main__":

    args = parser.parse_args()
    if args.celery:
        from extension.celery import celery

        if args.beat:
            celery.start(argv=["beat", "-S", "redbeat.RedBeatScheduler"])
        else:
            celery.worker_main(["worker"])
    else:
        app.run("0.0.0.0", port=app.config.get("RUN_PORT"), threaded=False)
