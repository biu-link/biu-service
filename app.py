# -*- coding: utf-8 -*-

import json

from flask import Flask, request
from util.json_encoder import JsonEncoder
from util.web_exception import WebException

from service.template_service import TemplateService

app = Flask(__name__)


def response(data=None, error_code=0, http_code=500, message=''):
    if error_code == 0:
        response_data = {
            'code': error_code,
            'data': data,
            'message': message
        }
        return json.dumps(response_data, ensure_ascii=True, cls=JsonEncoder)

    raise WebException(code=http_code, msg=message, error_code=error_code)


def error_response(http_code, message, error_code=-1):
    if error_code == 0:
        response_data = {
            'code': error_code,
            'message': message
        }
        return json.dumps(response_data, ensure_ascii=True, cls=JsonEncoder)

    raise WebException(code=http_code, msg=message, error_code=error_code)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/get-template')
def get_template():
    lang = request.args.get('lang')
    name = request.args.get('name')
    ts = TemplateService()
    template = ts.get_template(lang, name)
    if not template:
        return error_response(400, 'template not exist!')

    return response(
        {
            'template': template['content']
        }
    )


if __name__ == '__main__':
    app.run()
