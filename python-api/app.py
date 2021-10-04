from werkzeug.exceptions import HTTPException
from flask import Flask, render_template, redirect
import os

from controllers.bookmark import bookmark_list, bookmark_add, bookmark_remove, bookmark_update
from mytools import fail

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


"""书签列表"""


@app.route('/api/bookmark', methods=['GET'])
def get_bookmark():
    return bookmark_list()


"""添加书签"""


@app.route('/api/bookmark', methods=['POST'])
def add_bookmark():
    return bookmark_add()


"""修改书签"""


@app.route('/api/bookmark', methods=['PUT'])
def update_bookmark():
    return bookmark_update()


"""删除书签"""


@app.route('/api/bookmark', methods=['DELETE'])
def remove_bookmark():
    return bookmark_remove()


"""路由404"""


@app.errorhandler(404)
def page_not_found(error):
    return redirect('/')


@app.errorhandler(HTTPException)
def error_handler(error):
    return fail(error.to_json())


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
