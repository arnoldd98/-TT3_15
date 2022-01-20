import email
from flask import Flask, request, flash, jsonify
from flask_restful import abort
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

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

# create user
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    print(data)
    if db.session.query(User).filter_by(name=data['name']).all():
        abort(404, message="name already exists")
    #hashed_password = generate_password_hash(data['password'],method ='sha256')
    hashed_password = data['password']
    new_user = User(user_id=data['user_id'],name=data['name'],password=hashed_password,age=data['age'],
                    birthday=data['birthday'],email=data['email'], phone=data['phone'],city=data['city'], 
                    country=data['country'])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message':'New user created'}), 200

# login
@app.route('/user/<emailid>/<passwd>', methods=['GET'])
def get_one_user(emailid,passwd):
    user = db.session.query(User).filter_by(email=emailid).first()
    if not user:
        abort(404, message="email/password does not match!")
    print(user.name)
    print(passwd)
    if passwd != user.password:
        return jsonify({'message':'WRONG PASSWORD!!!'}), 401 
    
    elif passwd == user.password:
        return jsonify({'message':'Welcome!'+user.name+'! :)'}), 200


class LikedPost(db.Model):
    user_id = db.Column('User_ID',db.Integer,primary_key = True)
    post_id = db.Column('Post_ID',db.Integer,primary_key = True)

    def __init__(self, user_id, post_id):
        self.user_id = user_id
        self.post_id = post_id


class Post(db.Model):
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

class PostComment(db.Model):
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

class User(db.Model):
    user_id = db.Column('User_ID',db.Integer,primary_key = True)
    password = db.Column('Password',db.String(50))
    name = db.Column('Name',db.String(50))
    age = db.Column('Age',db.Integer,nullable=True)
    # date will be DDMMYYYY
    birthday = db.Column('Birthday',db.String(8),nullable=True)
    email = db.Column('Email',db.String(50),nullable=True)
    phone = db.Column('Phone',db.String(50),nullable=True)
    city = db.Column('City',db.String(50),nullable=True)
    country = db.Column('Country',db.String(50),nullable=True)

    def __init__(self, user_id,password, name, age, birthday, email,phone,city,country):
        self.user_id = user_id
        self.password = password
        self.name = name
        self.age = age
        self.birthday = birthday
        self.email = email
        self.phone = phone
        self.city = city
        self.country = country

if __name__ == '__main__':
    app.run(debug=True)