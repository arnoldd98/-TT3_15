from flask import Blueprint, request, flash, jsonify
from flask_restful import abort
from backend import db
from . import data_class
from flask_cors import CORS, cross_origin

bp = Blueprint('auth', __name__, url_prefix='/user')

# create user
@bp.route('/', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def create_user():
    data = request.get_json()
    print(data)
    if db.session.query(data_class.User).filter_by(name=data['name']).all():
        abort(404, message="name already exists")
    #hashed_password = generate_password_hash(data['password'],method ='sha256')
    hashed_password = data['password']
    new_user = data_class.User(user_id=data['user_id'],name=data['name'],password=hashed_password,age=data['age'],
                    birthday=data['birthday'],email=data['email'], phone=data['phone'],city=data['city'], 
                    country=data['country'])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message':'New user created'}), 200

# login
@bp.route('<emailid>/<passwd>', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def get_one_user(emailid,passwd):
    user = db.session.query(data_class.User).filter_by(email=emailid).first()
    if not user:
        abort(404, message="email/password does not match!")
    print(user.name)
    print(passwd)
    if passwd != user.password:
        return jsonify({'message':'WRONG PASSWORD!!!'}), 401 
    
    elif passwd == user.password:
        return jsonify({'message':'Welcome!'+user.name+'! :)'}), 200