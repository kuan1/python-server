from flask import Flask, render_template, request, redirect
import os

from controller.bookmark import bookmark_list, bookmark_add, bookmark_remove, bookmark_update

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

# 书签路由
@app.route('/api/bookmark', methods=['GET', 'POST', 'DELETE', 'PUT'])
def bookmark():
  # 书签列表
  if request.method == 'GET':
    return bookmark_list()
  # 新增书签
  elif request.method == 'POST':
    return bookmark_add()
  # 删除书签
  elif request.method == 'DELETE':
    return bookmark_remove()
  # 更新书签
  elif request.method == 'PUT':
    return bookmark_update()



# 路由404
@app.errorhandler(404)
def page_not_found(error):
  return redirect('/')

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(debug=True, host='0.0.0.0', port=port)
