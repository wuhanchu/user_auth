from authlib.integrations.flask_oauth2 import AuthorizationServer, ResourceProtector
from authlib.integrations.sqla_oauth2 import create_query_client_func, create_save_token_func, \
    create_revocation_endpoint
from authlib.oauth2.rfc6749 import grants
from authlib.oauth2.rfc6750 import BearerTokenValidator
from flask import request as _req
from werkzeug.security import gen_salt

from frame import permission_context
from frame.extension.database import db, db_schema
from frame.http.response import queryToDict
from frame.http.exception import BusiError
from frame.util import com_tool
from module.user.model import User
from ..model import OAuth2Token, OAuth2AuthorizationCode, OAuth2Client


class AuthorizationCodeGrant(grants.AuthorizationCodeGrant):
    def create_authorization_code(self, client, user, request):
        code = gen_salt(48)
        item = OAuth2AuthorizationCode(
            code=code,
            client_id=client.client_id,
            redirect_uri=request.redirect_uri,
            scope=request.scope,
            user_id=user.id,
        )
        db.session.add(item)
        db.session.commit()
        return code

    def parse_authorization_code(self, code, client):
        item = OAuth2AuthorizationCode.query.filter_by(
            code=code, client_id=client.client_id).first()
        if item and not item.is_expired():
            return item

    def delete_authorization_code(self, authorization_code):
        db.session.delete(authorization_code)
        db.session.commit()

    def authenticate_user(self, authorization_code):
        return None
        # return User.query.get(authorization_code.user_id)


class PasswordGrant(grants.ResourceOwnerPasswordCredentialsGrant):
    def authenticate_user(self, username, password):
        user = User.query.filter_by(loginid=username).first()
        # 校验密码
        if user.password == com_tool.get_MD5_code(password):
            return user


class RefreshTokenGrant(grants.RefreshTokenGrant):
    def authenticate_refresh_token(self, refresh_token):
        token = OAuth2Token.query.filter_by(refresh_token=refresh_token).first()
        if token and not token.revoked and not token.is_refresh_token_expired():
            return token

    def authenticate_user(self, credential):
        return User.query.get(credential.user_id)


query_client = create_query_client_func(db.session, OAuth2Client)
save_token = create_save_token_func(db.session, OAuth2Token)
authorization = AuthorizationServer(
    query_client=query_client,
    save_token=save_token,
)
require_oauth = ResourceProtector()


# def require_oauth(profile):
#     def decorate(f):
#         return f
#     return decorate

class _BearerTokenValidator(BearerTokenValidator):
    def __call__(self, *args, **kwargs):
        # 登录验证
        token = BearerTokenValidator.__call__(self, *args, **kwargs)
        token_request = args[2]
        uri = token_request.uri
        method = token_request.method

        # 权限验证
        if _req.url_rule and not permission_context.check_permission(_req.url_rule.rule, method, self.get_usr_roles(token.user_id)):
            raise BusiError("Permission denied!", 'API has not access permission <%s>:%s' % (method, uri), code=403)
        return token

    def get_usr_roles(self, user_id):
        sql = "select role_id from %s.user_role where user_id =%s " % (db_schema, user_id)
        res = db.session.execute(sql).fetchall()
        role_list = queryToDict(res)
        role_list = [str(role['role_id']) for role in role_list]
        return role_list

    def authenticate_token(self, token_string):
        q = db.session.query(OAuth2Token)
        return q.filter_by(access_token=token_string).first()

    def request_invalid(self, request):
        return False

    def token_revoked(self, token):
        return token.revoked


def config_oauth(app):
    authorization.init_app(app)

    # support all grants
    authorization.register_grant(grants.ImplicitGrant)
    authorization.register_grant(grants.ClientCredentialsGrant)
    authorization.register_grant(AuthorizationCodeGrant)
    authorization.register_grant(PasswordGrant)
    authorization.register_grant(RefreshTokenGrant)

    # support revocation
    revocation_cls = create_revocation_endpoint(db.session, OAuth2Token)
    authorization.register_endpoint(revocation_cls)

    # protect resource
    require_oauth.register_token_validator(_BearerTokenValidator())
    # bearer_cls = create_bearer_token_validator(db.session, OAuth2Token)
    # require_oauth.register_token_validator(bearer_cls())
