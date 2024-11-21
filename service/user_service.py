# -*- coding: utf-8 -*-

"""
需要安装模块
pip install authing
"""
import json
import util.tools as tools

from common.singleton import Singleton
# from authing.v2.authentication import AuthenticationClient, AuthenticationClientOptions

from model.user import User
from util.web_exception import WebException
from util.redis_db import RedisDB
from util.mongo_db import MongoDB


class UserService(metaclass=Singleton):

    def __init__(self):
        super(UserService, self).__init__()

    def get_user_by_email(self, email):
        user = None
        row = MongoDB().select_one('user', {'email': email})
        if row:
            user = User()
            user.deserialize(row)
        return user

    def exchange_user_info(self, code):
        user_info = self.get_user_info(code)
        if user_info:
            token = user_info['token']
            email = user_info['email']
            if token and email:
                key = 'auth_token_' + email
                RedisDB().set(key, token)

                user = self.get_user_by_email(email)
                if not user:
                    MongoDB().insert('user', {
                        'email': email
                    })

        return user_info

    def get_user_info(self, code):
        cfg = tools.get_config_section('authing')
        authentication_client = AuthenticationClient(
            options=AuthenticationClientOptions(
                app_id=cfg.get('app_id'),
                secret=cfg.get('secret'),
                app_host=cfg.get('app_host'),
                redirect_uri=cfg.get('redirect_uri'),
                token_endpoint_auth_method='client_secret_post',
                protocol='oidc'
            ))
        response = authentication_client.get_access_token_by_code(code)
        print(response)

        access_token = response['access_token']
        id_token = response['id_token']

        authentication_client = AuthenticationClient(
            options=AuthenticationClientOptions(
                app_id=cfg.get('app_id'),
                app_host=cfg.get('app_host'),
                token=id_token
            ))
        user = authentication_client.get_current_user()
        print(user)

        return {
            'token': access_token,
            'email': user['email']
        }

    def check_token(self, authorization):
        if not authorization:
            raise WebException(code=401, msg='need login', error_code=-1)

        arr = authorization.split(',')
        if len(arr) < 2:
            raise WebException(code=401, msg='need login', error_code=-1)

        email = arr[0]
        token = arr[1]
        right_token = RedisDB().get('auth_token_' + email)
        if right_token != token:
            raise WebException(code=401, msg='need login', error_code=-1)

        return {
            'email': email,
            'token': token
        }

    def logout(self, authorization):
        if authorization:
            arr = authorization.split(',')
            if len(arr) >= 2:
                email = arr[0]
                token = arr[1]
                key = 'auth_token_' + email
                right_token = RedisDB().get(key)
                if right_token == token:
                    RedisDB().delete(key)
