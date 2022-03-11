from app import db
from flask import request, jsonify
from werkzeug.security import generate_password_hash
from ..models.users import Users, user_schema, users_schema


def post_user():
    username = request.json['username']
    password = generate_password_hash(request.json['password'])
    name = request.json['name']
    email = request.json['email']
    user = Users(username=username, password=password, name=name, email=email)
    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'Message':'Successfuly registred', 'data':result}), 201
    except:
        return jsonify({'message':'unable to create', 'data':user}), 500

def update_user(id):
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']

    user = Users.query.get(id)
    # user = Users.query.filter_by(id=id).first()
    if not user:
        return jsonify({'message': "user don't exist", 'data':{}}),404

    pass_hash = generate_password_hash(password)
    

    try:
        user.username = username
        user.password = pass_hash
        user.name = name,
        user.email = email
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'Message':'Successfuly updated', 'data':result}), 201
    except:
        return jsonify({'message':'unable to create', 'data':user}), 500


def get_users():
    users = Users.query.all()
    if users:
        result = users_schema.dump(users)
        return jsonify({'message':'Successfully fetched', 'data': result}),201
    return jsonify({'Message':'Nothing Found', 'data':{}}), 404

def get_user(id):
    user  = Users.query.get(id)
    if user:
        result = user_schema.dump(user)
        return jsonify({'Message':'Successfully fectched', 'data':result}), 201
    return jsonify({'message':"user don't exists", 'data':{}}), 404

def delete_user(id):
    user = Users.query.get(id)
    if not user:
        return jsonify({'message': "user don't exist", 'data':{}}), 404
    if user:
        try:
            db.session.delete(user)
            db.session.commit()
            result = user_schema.dump(user)
            return jsonify({'message':'Successfully deleted', 'data':result}), 200
        except:
            return jsonify({'message':'unable to delete', 'data':{}}),500