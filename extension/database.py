from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base

# from sqlalchemy_utils import force_auto_coercion, force_instant_defaults

db = None
db_map = automap_base()
db_schema = "public"
# Base = db.Model
BaseModel = None
AutoMapModel = None


def init_app(app):
    global db, db_schema, BaseModel, AutoMapModel
    db_schema = app.config.get("DB_SCHEMA")

    class BaseModel:
        """
        schema base model
        """
        __table_args__ = {'extend_existing': True, 'schema': db_schema}

    db = SQLAlchemy(app)
    # db.init_app(app)
    # db_map.prepare(db.get_engine(app), reflect=True, schema=app.config.get("DB_SCHEMA"))
    # db.reflect(app=app)
    db.Model.metadata.reflect(bind=db.engine, schema=db_schema)

    # AutoMapModel = automap_base(db.Model)

    #
    # force_auto_coercion()
    # force_instant_defaults()
