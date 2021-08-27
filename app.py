from flask import Flask

from util.db import Db

app = Flask(__name__)


@app.route('/')
def hello_world():
    db = Db()
    row = db.single('select * from ba_default_template where id = %(id)s', {'id': 1, 'lang': 'Javas'})
    print(row)

    db.delete('delete from ba_default_template where id = 2')
    model = {
        'id': 2,
        'lang': 'Java',
        'name': 'mapper',
        'content': 'bbb',
        'type': None
    }
    db.insert_model('ba_default_template', model)

    model['content'] = 'ccc'
    db.update_model('ba_default_template', model)

    return 'Hello World!'


if __name__ == '__main__':
    app.run()
