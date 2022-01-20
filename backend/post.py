from flask import Blueprint, request, flash, jsonify
from backend import db
from . import data_class

bp = Blueprint('post', __name__, url_prefix='/post')

@bp.route('/', methods = ['POST'])
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
def delete_post():
    data = request.get_json()
    if data["post_id"] == None or data['user_id'] == None:
            return jsonify({'error': f'Missing post id / user id. {data}'})
    else: 
        post_id = data['post_id']
        user_id = data['user_id']
        try:
            db.session.query().\
                filter(data_class.Post.user_id == data['user_id']).\
                filter(data_class.Post.post_id == data['post_id']).\
                delete()
            db.session.commit()
            return jsonify({'message': f'Post {post_id} successfully deleted'})
        except:
            return jsonify({'error': f'Unable to find post made by user {user_id} - check if post {post_id} is made by user'})