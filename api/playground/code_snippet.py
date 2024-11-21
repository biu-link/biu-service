# -*- coding: utf-8 -*-

from flask import Blueprint, request

code_snippet = Blueprint('code_snippet', __name__)


@code_snippet.route('/code_snippet', methods=['GET'])
def add_code_snippet():
    return 'code_snippet'
