# -*- coding: utf-8 -*-
"""
需安装模块
pip install flask-cors
"""

import json
import urllib.parse
import util.tools as tools

from flask import Flask, request

from service.project_service import ProjectService
from service.user_service import UserService
from util.json_encoder import JsonEncoder
from util.web_exception import WebException

from service.template_service import TemplateService
from service.studying_service import StudyingService

app = Flask(__name__)

env = tools.get_config_value('common', 'env')
if not env.__contains__('prod'):
    from flask_cors import CORS

    CORS(app, supports_credentials=True)


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


def check_token():
    authorization = request.headers.get('Authorization')
    return UserService().check_token(urllib.parse.unquote(authorization))


@app.route('/')
def hello_world():
    return 'Hello World!'


# ------------ project 相关接口

@app.route('/project-list')
def get_project_list():
    user_info = check_token()
    email = user_info['email']
    user = UserService().get_user_by_email(email)
    owner_id = user.id
    project_list = ProjectService().get_project_list(owner_id, user.id)
    result_list = []
    for project in project_list:
        result_list.append(project.serialize())
    return response(result_list)


@app.route('/project')
def get_project():
    check_token()
    project_id = request.args.get('id')
    p = ProjectService().get_project(project_id)
    return response(p.serialize())


@app.route('/project', methods=['POST'])
def add_project():
    user_info = check_token()
    email = user_info['email']
    user = UserService().get_user_by_email(email)
    owner_id = user.id
    body = request.data.decode()
    ProjectService().save_project(body, owner_id)
    return response()


@app.route('/project', methods=['PUT'])
def update_project():
    check_token()
    body = request.data.decode()
    ProjectService().update_project(body)
    return response()


# ------------ template 相关接口
@app.route('/template-list')
def get_template_list():
    user_info = check_token()
    email = user_info['email']
    user = UserService().get_user_by_email(email)
    project_ld = request.args.get('project_id')
    if not project_ld:
        return error_response(400, '参数错误')
    template_list = TemplateService().get_template_list(project_ld)
    result_list = []
    for template in template_list:
        result_list.append(template.serialize())
    return response(result_list)


@app.route('/template')
def get_template():
    check_token()
    template_id = request.args.get('id')
    t = TemplateService().get_template(template_id)
    return response(t.serialize())


@app.route('/template', methods=['POST'])
def add_template():
    check_token()
    body = request.data.decode()
    TemplateService().save_template(body)
    return response()


@app.route('/template', methods=['PUT'])
def update_template():
    check_token()
    body = request.data.decode()
    TemplateService().update_template(body)
    return response()


@app.route('/exchange-user-info', methods=['POST'])
def exchange_user_info():
    code = request.form.get('code')
    user_info = UserService().exchange_user_info(code)
    return response(user_info)


@app.route('/logout', methods=['POST'])
def logout():
    authorization = request.headers.get('Authorization')
    UserService().logout(urllib.parse.unquote(authorization))
    return response()


@app.route('/article-list')
def get_article_list():
    user_id = 1001  # request.args.get('user_id')
    article_list = StudyingService().get_article_list(user_id)

    result_list = list(map(lambda x: x.serialize(), article_list))
    return response(result_list)


@app.route('/article', methods=['POST'])
def insert_article():
    user_id = 1001

    body = request.data.decode()
    article = json.loads(body)
    article['user_id'] = user_id

    content = article['content']
    del article['content']

    article_id = StudyingService().insert_article_and_sentence(article, content)
    return response(dict(article_id=article_id))


@app.route('/article', methods=['PUT'])
def update_article():
    user_id = 1001

    body = request.data.decode()
    data = json.loads(body)
    data['user_id'] = user_id

    StudyingService().update_article(data)
    return response()


@app.route('/article/<article_id>', methods=['DELETE'])
def delete_article(article_id):
    user_id = 1001  # request.args.get('user_id')
    StudyingService().delete_article(user_id, article_id)

    return response()


@app.route('/sentence/split', methods=['PUT'])
def split_sentence():
    user_id = 1001

    body = request.data.decode()
    data = json.loads(body)
    sentence_id = data['sentence_id']
    lines = data['lines']

    StudyingService().split_sentence(user_id, sentence_id, lines)
    return response()


@app.route('/article/<article_id>')
def get_article(article_id):
    user_id = 1001  # request.args.get('user_id')
    article = StudyingService().get_article(user_id, article_id)
    sentence_list = StudyingService().get_sentence_list(user_id, article_id)
    result_list = list(map(lambda x: x.serialize(), sentence_list))

    return response(dict(article=article.serialize(), sentence_list=result_list))


@app.route('/word', methods=['POST'])
def insert_word():
    user_id = 1001

    body = request.data.decode()
    data = json.loads(body)

    word = data['word']
    sentence_id = data['sentence_id']
    article_id = data['article_id']

    word_id = StudyingService().insert_word(user_id, word, sentence_id, article_id)
    return response(dict(word_id=word_id))


@app.route('/word', methods=['PUT'])
def update_word():
    user_id = 1001

    body = request.data.decode()
    data = json.loads(body)
    data['user_id'] = user_id

    StudyingService().update_word(data)
    return response()


@app.route('/word-list')
def get_word_list():
    user_id = 1001  # request.args.get('user_id')
    article_id = request.args.get('article_id')
    status = request.args.get('status')
    word_list = StudyingService().get_word_list(user_id, article_id, status)

    result_list = list(map(lambda x: x.serialize(), word_list))
    return response(result_list)


@app.route('/word/<word_id>', methods=['DELETE'])
def delete_word(word_id):
    user_id = 1001  # request.args.get('user_id')
    StudyingService().delete_word(user_id, word_id)

    return response()


if __name__ == '__main__':
    app.run()
