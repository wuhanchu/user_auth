from flask_marshmallow import Marshmallow

ma = None


def init_app(app):
    global ma
    ma = Marshmallow(app)
