from marshmallow import fields

from extension.marshmallow import ma
from module.auth.model import OAuth2ClientModel


class OAuth2ClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OAuth2ClientModel
        include_fk = False


client_param = OAuth2ClientSchema(only=("client_name", "client_uri", "grant_type", "scope", "response_type"))
client_res = OAuth2ClientSchema(only=("id",))
