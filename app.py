from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, World!'

# 另一種路由的實現方式
# app.add_url_rule('/hello', view_func=hello)

app.run(debug=True)