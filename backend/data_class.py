import dbm
from re import S
from this import d
from backend import db
from dataclasses import dataclass

@dataclass
class LikedPost(db.Model):
    user_id: int
    post_id: int

    user_id = db.Column('User_ID',db.Integer,primary_key = True)
    post_id = db.Column('Post_ID',db.Integer,primary_key = True)

    def __init__(self, user_id, post_id):
        self.user_id = user_id
        self.post_id = post_id

@dataclass
class Post(db.Model):
    post_id: int
    user_id: int
    post_title: str
    post_description: str
    post_image: str

    post_id = db.Column('Post_ID',db.Integer,primary_key = True)
    user_id = db.Column('User_ID', db.Integer, nullable=False)
    post_title = db.Column('Post_Title',db.String(50))
    post_description = db.Column('Post_Description',db.String(200),nullable=True)
    post_image = db.Column('Post_image',db.String(300),nullable=True)

    def __init__(self, user_id, post_title, post_description, post_image, post_id=None):
        self.post_id = post_id
        self.user_id = user_id
        self.post_title = post_title
        self.post_description = post_description
        self.post_image = post_image

@dataclass
class PostComment(db.Model):
    comment_id: int
    user_id: int
    post_id: int

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

@dataclass
class User(db.Model):
    user_id: int
    password: str
    name: str
    age: int
    birthday: str
    email: str
    phone: str
    city: str
    country: str

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

