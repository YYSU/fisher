from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

@app.route('/hello')
def hello():
    headers = {
        'content-type': 'text/plain'
    }
    return '<h1> Yo !</h1>', 200, headers


# 通常在生產環境會使用 nginx + uwsgi，不會直接使用 flask sever
# https://www.maxlist.xyz/2020/05/06/flask-wsgi-nginx/
# 因此需要判斷
if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])