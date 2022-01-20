from flask import Flask, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password123@localhost/socialmedia'

db = SQLAlchemy(app)

@app.route('/post', methods = ['GET', 'POST', 'DELETE'])
def update_post():
    if request.method == 'POST':
        if not request.form['post_id'] or not request.form['user_id']:
            flash('Missing post id / user id')
        else:
            post_id = request.form['post_id']
            user_id = request.form['user_id']
            try:
                db.session.query().\
                    filter(Post.user_id == request.form['user_id'] and Post.post_id == request.form['post_id']).\
                    update({'post_title': request.form['post_title'],
                            'post_description': request.form['post_description'],
                            'post_image': request.form['post_image']})
                
                db.session.commit()
                flash(f'Successfully modified post {post_id}')
            except:
                flash(f'Unable to find post made by user {user_id} - check if post {post_id} is made by user')
    elif request.method == 'DELETE':
        if not request.form['post_id'] or not request.form['user_id']:
            flash('Missing post id / user id')
        else: 
            post_id = request.form['post_id']
            user_id = request.form['user_id']
            try:
                db.session.query().\
                    filter(Post.user_id == request.form['user_id'] and Post.post_id == request.form['post_id']).\
                    delete()
                db.session.commit()
                flash(f'Successfuly deleted post')
            except:
                flash(f'Unable to find post made by user {user_id} - check if post {post_id} is made by user')

class LikedPost(db.model):
    user_id = db.Column('User_ID',db.Integer,primary_key = True,required= True)
    post_id = db.Column('Post_ID',db.Integer,primary_key = True,required = True)

    def __init__(self, user_id, post_id):
        self.user_id = user_id
        self.post_id = post_id


class Post(db.model):
    post_id = db.Column('Post_ID',db.Integer,primary_key = True)
    user_id = db.Column('User_ID', db.Integer, nullable=False)
    post_title = db.Column('Post_Title',db.String(50))
    post_description = db.Column('Post_Description',db.String(200),nullable=True)
    post_image = db.Column('Post_image',db.String(300),nullable=True)

    def __init__(self, post_id, user_id, post_title, post_description, post_image):
        self.post_id = post_id
        self.user_id = user_id
        self.post_title = post_title
        self.post_description = post_description
        self.post_image = post_image

class PostComment(db.model):
    comment_id = db.Column('Comment_ID',db.Integer,primary_key = True)
    user_id = db.Column('User_ID',db.Integer)
    post_id = db.Column('Post_ID',db.Integer)
    # consensus to set 280 char limit
    comment = db.Column('Comment',db.String(280),nullable=True)

    def __init__(self, comment_id, user_id, post_id, comment):
        self.comment_id = comment_id
        self.user_id = user_id
        self.post_id = post_id
        self.comment = comment

class User(db.model):
    user_id = db.Column('User_ID',db.Integer,primary_key = True)
    name = db.Column('Name',db.String(50))
    age = db.Column('Age',db.Integer,nullable=True)
    # date will be DDMMYYYY
    birthday = db.Column('Birthday',db.String(8),nullable=True)

    def __init__(self, user_id, name, age, birthday):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.birthday = birthday
