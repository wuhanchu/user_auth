# -*- coding: UTF-8 -*-
import time

from authlib.integrations.sqla_oauth2 import OAuth2ClientMixin, OAuth2AuthorizationCodeMixin, OAuth2TokenMixin
from jsonpickle import json
from sqlalchemy.orm import foreign
from werkzeug.utils import cached_property

from frame.extension.database import db, BaseModel, db_schema
from module.user.model import User


class OAuth2ClientModel(db.Model, BaseModel):
    __tablename__ = 'oauth2_client'
    id = db.Column(db.Integer, primary_key=True)


class OAuth2Client(db.Model, BaseModel, OAuth2ClientMixin):
    __tablename__ = 'oauth2_client'
    id = db.Column(db.Integer, primary_key=True)

    @cached_property
    def client_metadata(self):
        if self._client_metadata:
            return self._client_metadata
        return {
            "grant_types": json.loads(self.grant_type),
            "response_types": self.response_type,
            "scope": self.scope
        }


class OAuth2AuthorizationCode(db.Model, BaseModel, OAuth2AuthorizationCodeMixin):
    __tablename__ = 'oauth2_code'

    id = db.Column(db.Integer, primary_key=True)


class OAuth2Token(db.Model, BaseModel, OAuth2TokenMixin):
    __tablename__ = 'oauth2_token'
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer, db.ForeignKey(db_schema + '.user.id', ondelete='CASCADE'))
    user = db.relationship(User,
                           primaryjoin=User.id == foreign(user_id))

    def is_refresh_token_expired(self):
        expires_at = self.issued_at + self.expires_in * 2
        return expires_at < time.time()
