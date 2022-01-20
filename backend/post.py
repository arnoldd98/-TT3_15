from flask import Blueprint, request, flash, jsonify
from backend import db
from flask_restful import abort
from . import data_class
from flask_cors import CORS, cross_origin

bp = Blueprint('post', __name__, url_prefix='/post')

@bp.route('/', methods = ['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def add_post():
    data = request.get_json()
    if data['user_id'] == None:
        return jsonify({'error': f'Missing user id. {data}'})
    else:
        user_id = data['user_id']

        try:
            post = data_class.Post(user_id=user_id, 
                    post_title=data['post_title'], 
                    post_description=data['post_description'], 
                    post_image=data['post_image'])             
            db.session.add(post)
            db.session.commit()
            return jsonify({'message': f'Post successfully added'})
        except:
            return jsonify({'error': f'SQL error'})

@bp.route('/', methods = ['PATCH'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def update_post():
    data = request.get_json()
    if data["post_id"] == None or data['user_id'] == None:
        return jsonify({'error': f'Missing post id / user id. {data}'})
    else:
        post_id = data['post_id']
        user_id = data['user_id']
        try:
            db.session.query(data_class.Post).\
                filter(data_class.Post.user_id == data['user_id']).\
                filter(data_class.Post.post_id == data['post_id']).\
                update({'post_title': data['post_title'],
                        'post_description': data['post_description'],
                        'post_image': data['post_image']})
            
            db.session.commit()
            return jsonify({'message': f'Post {post_id} successfully updated'})
        except:
            return jsonify({'error': f'Unable to find post made by user {user_id} - check if post {post_id} is made by user'})

@bp.route('/', methods = ['DELETE'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def delete_post():
    data = request.get_json()
    if data["post_id"] == None or data['user_id'] == None:
            return jsonify({'error': f'Missing post id / user id. {data}'})
    else: 
        post_id = data['post_id']
        user_id = data['user_id']

        try:
            db.session.query(data_class.Post).\
                filter(data_class.Post.user_id == data['user_id']).\
                filter(data_class.Post.post_id == data['post_id']).\
                delete()
            db.session.commit()
            return jsonify({'message': f'Post {post_id} successfully deleted'})
        except:
            return jsonify({'error': f'Unable to find post made by user {user_id} - check if post {post_id} is made by user'})


@bp.route('/<user_id>', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def get_user_posts(user_id):
    data = request.get_json()
    user = db.session.query(data_class.User).filter_by(user_id=user_id).first()
    if not user:
        abort(404, message=f"cannot find user with id {user_id}!")
    
    try:
        user_posts = db.session.query(data_class.Post).\
            filter(data_class.Post.user_id == data['user_id']).\
            all()
        return jsonify(user_posts)
    except:
        return jsonify({'error': f'SQL Query error when finding posts by userid {user_id}'})

@bp.route('/all', methods = ['GET'])
def get_post():
    try:
        user_posts = db.session.query(data_class.Post).all()
        return jsonify(user_posts)
    except:
        return jsonify({'error': f'SQL Query error when finding posts'})

    # for i in range(len(user_id)):

    #     try:
    #         post = data_class.Post(user_id=user_id,
    #                 post_title=data['post_title'],
    #                 post_description=data['post_description'],
    #                 post_image=data['post_image'])            
    #         db.session.get(post)        
    #         db.session.commit()
    #         return jsonify({'message': f'All post shown'})

    #     except:
    #         return jsonify({'error': f'SQL error'})


        
