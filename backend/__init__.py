import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin


db = SQLAlchemy()

def create_app(test_config=None):

    app = Flask(__name__)
    app.secret_key = 'test'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/socialmedia'
    app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'
    cors = CORS(app)
    db.init_app(app)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import post
    app.register_blueprint(post.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    return app







                

