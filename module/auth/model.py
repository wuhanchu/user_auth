# -*- coding: UTF-8 -*-

import time

from authlib.flask.oauth2.sqla import OAuth2AuthorizationCodeMixin, OAuth2ClientMixin, OAuth2TokenMixin

from extension.db import db


class OAuth2Client(db.Model, OAuth2ClientMixin):
    __tablename__ = 'oauth2_client'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey('sys_user.id', ondelete='CASCADE'))
    user = db.relationship('SysUser')


class OAuth2AuthorizationCode(db.Model, OAuth2AuthorizationCodeMixin):
    __tablename__ = 'oauth2_code'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey('sys_user.id', ondelete='CASCADE'))
    user = db.relationship('SysUser')


class OAuth2Token(db.Model, OAuth2TokenMixin):
    __tablename__ = 'oauth2_token'
    __table_args__ = {'extend_existing': True}
