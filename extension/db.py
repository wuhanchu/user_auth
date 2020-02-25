from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import force_auto_coercion, force_instant_defaults

db = SQLAlchemy()
Base = db.Model


force_auto_coercion()
force_instant_defaults()

