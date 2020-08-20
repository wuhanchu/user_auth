# -*- coding: UTF-8 -*-
import requests
from authlib.oauth2 import OAuth2Error
from flask import render_template, redirect, jsonify
from flask import request, session
from werkzeug.security import gen_salt
import urllib.parse

from module.auth.extension.oauth2 import authorization
from . import blueprint
from .model import *
from .model import OAuth2Client
from .. import get_user_pattern
from ..user.model import User
from ..user.resource import current_user
from config import ConfigDefine
from ..user.schema import PhfundUserSchema


@blueprint.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        username = request.form.get('username')
        user = User.query.filter_by(loginid=username).first()
        session['id'] = user.id
        return redirect('/oauth')
    user = current_user()
    if user:
        clients = OAuth2Client.query.filter_by(user_id=user.id).all()
    else:
        clients = []
    return render_template('oauth_index.html', user=user, clients=clients)


@blueprint.route('/client', methods=['POST'])
def create_client():
    user = current_user()
    user = user.json
    if not user:
        return

    client = OAuth2Client(**request.form.to_dict(flat=True))
    client.user_id = user.get("id")
    client.client_id = gen_salt(24)
    if client.token_endpoint_auth_method == 'none':
        client.client_secret = ''
    else:
        client.client_secret = gen_salt(48)
    db.session.add(client)
    db.session.commit()
    return redirect('/')


@blueprint.route('/authorize', methods=['GET', 'POST'])
def authorize():
    user = current_user()
    if request.method == 'GET':
        try:
            grant = authorization.validate_consent_request(end_user=user)
        except OAuth2Error as error:
            return error.error
        return render_template('authorize.html', user=user, grant=grant)
    if not user and 'username' in request.form:
        username = request.form.get('username')
        user = User.query.filter_by(loginid=username).first()
    if request.form['confirm']:
        grant_user = user
    else:
        grant_user = None
    return authorization.create_authorization_response(grant_user=grant_user)


@blueprint.route('/token', methods=['POST'])
def issue_token():
    res = authorization.create_token_response(request)
    return res


@blueprint.route('/revoke', methods=['POST'])
def revoke_token():
    return authorization.create_endpoint_response('revocation', request)


# 鹏华
if get_user_pattern() == ConfigDefine.UserPattern.phfund:

    @blueprint.route('/token', methods=('DELETE',))
    def logout():
        from flask import current_app, request

        url = urllib.parse.urljoin(
            current_app.config.get(ConfigDefine.USER_SERVER_URL),
            "/authentication/revoke_token")
        response = requests.get(url, headers=request.headers)
        result = response.json()
        if result.get("httpcode"):
            return None, result.get("httpcode")

        result = PhfundUserSchema().loads(response.json())
        return jsonify(result)

# 默认
else:

    @blueprint.route('/token', methods=('DELETE',))
    @blueprint.route('/logout')
    def logout():
        del session['id']
        return redirect('/')
