# -*- coding: UTF-8 -*-
import time
import json

from authlib.integrations.sqla_oauth2 import (
    OAuth2ClientMixin,
    OAuth2AuthorizationCodeMixin,
    OAuth2TokenMixin,
)
from sqlalchemy.orm import foreign
from werkzeug.utils import cached_property

from flask_frame.extension.database import db, BaseModel, db_schema
from module.user.model import User

from sqlalchemy import event


class OAuth2ClientModel(db.Model, BaseModel):
    __tablename__ = "oauth2_client"
    id = db.Column(db.Integer, primary_key=True)


class OAuth2Client(db.Model, BaseModel, OAuth2ClientMixin):
    __tablename__ = "oauth2_client"
    id = db.Column(db.Integer, primary_key=True)

    @cached_property
    def client_metadata(self):
        if self._client_metadata:
            return self._client_metadata
        return {
            "grant_types": json.loads(self.grant_type),
            "response_types": self.response_type,
            "scope": self.scope,
        }


class OAuth2AuthorizationCode(db.Model, BaseModel, OAuth2AuthorizationCodeMixin):
    __tablename__ = "oauth2_code"

    id = db.Column(db.Integer, primary_key=True)


class OAuth2Token(db.Model, BaseModel, OAuth2TokenMixin):
    __tablename__ = "oauth2_token"
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer, db.ForeignKey(db_schema + ".user.id", ondelete="CASCADE")
    )
    user = db.relationship(User, primaryjoin=User.id == foreign(user_id))

    def is_refresh_token_expired(self):
        expires_at = self.issued_at + self.expires_in * 2
        return expires_at < time.time()


@event.listens_for(OAuth2Token, "after_delete")
def token_delete(mapper, connection, target):
    """删除token时，删除缓存

    Args:
        mapper (_type_): _description_
        connection (_type_): _description_
        target (_type_): _description_
    """

    from .util import generate_user_cache_key, generate_token_cache_key
    from flask_frame.extension.redis import redis_client

    if redis_client and target.access_token:
        token_cache_key = generate_token_cache_key(target.access_token)
        user_cache_key = generate_user_cache_key(target.access_token)
        redis_client.expire(token_cache_key)
        redis_client.expire(user_cache_key)
