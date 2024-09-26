# -*- coding: utf-8 -*-
from flask import Blueprint, request

from .playground.code_snippet import code_snippet

api = Blueprint('api', __name__)
api.register_blueprint(code_snippet)


@api.before_request
def before_request():
    # print(request.url)
    pass


@api.route('/')
def hello_world():
    return 'Hello World 123!'
