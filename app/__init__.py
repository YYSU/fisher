from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blue_print(app)
    return app

def register_blue_print(app):
    from app.web.book import web
    app.register_blueprint(web)
