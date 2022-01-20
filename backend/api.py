from typing_extensions import Required
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password123@localhost/socialmedia'

db = SQLAlchemy(app)

class LikedPost(db.model):
    user_id = db.Column('User_ID',db.Integer,primary_key = True,required= True)
    post_id = db.Column('Post_ID',db.Integer,primary_key = True,required = True)

class Post(db.model):
    post_id = db.Column('Post_ID',db.Integer,primary_key = True)
    post_title = db.Column('Post_Title',db.String(50))
    post_description = db.Column('Post_Description',db.String(200),nullable=True)
    post_image = db.Column('Post_image',db.String(300),nullable=True)

class PostComment(db.model):
    comment_id = db.Column('Comment_ID',db.Integer,primary_key = True)
    user_id = db.Column('User_ID',db.Integer)
    post_id = db.Column('Post_ID',db.Integer)
    # consensus to set 280 char limit
    comment = db.Column('Comment',db.String(280),nullable=True)

class User(db.model):
    user_id = db.Column('User_ID',db.Integer,primary_key = True)
    name = db.Column('Name',db.String(50))
    age = db.Column('Age',db.Integer,nullable=True)
    # date will be DDMMYYYY
    birthday = db.Column('Birthday',db.String(8),nullable=True)


if __name__ == '__main__':
    app.run(debug=True)