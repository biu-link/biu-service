# -*- coding: utf-8 -*-

from flask import request
import json

from werkzeug.exceptions import HTTPException


class WebException(HTTPException):
    code = 500
    msg = ''
    error_code = -1

    def __init__(self, msg=None, code=None, error_code=None, headers=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        super(WebException, self).__init__(msg, None)

    def get_body(self, environ=None, scope=None):
        body = dict(
            message=self.msg,
            code=self.error_code,
            request=request.method + ' ' + request.full_path
        )
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None, scope=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]
