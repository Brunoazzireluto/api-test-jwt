from app import db
from flask import request, jsonify
from werkzeug.security import generate_password_hash
from ..models.users import Users, user_schema, users_schema
from firebase_admin import auth


class UsersClass:

    def post_user():
        password = request.json['password']
        name = request.json['name']
        email = request.json['email']
        # user = Users(username=username, password=password, name=name, email=email)
        user = auth.create_user(email=email, password=password)
        info_user = Users(uid=user.uid, name=name, email=user.email)
        try:
            db.session.add(info_user)
            db.session.commit()
            result = user_schema.dump(user)
            return jsonify({'Message': 'Successfully registered'}), 201
        except:
            return jsonify({'message': 'unable to create', 'data': user}), 500

    def update_user(id):
        password = request.json['password']
        name = request.json['name']
        email = request.json['email']

        user = Users.query.get(id)
        # user = Users.query.filter_by(id=id).first()
        if not user:
            return jsonify({'message': "user don't exist", 'data': {}}), 404


        try:
            auth.update_user(user.uid, email=email, password=password)
            user.name = name,
            user.email = email
            db.session.commit()
            result = user_schema.dump(user)
            return jsonify({'Message': 'Successfuly updated', 'data': result}), 201
        except:
            return jsonify({'message': 'unable to create', 'data': user}), 500

    def delete_user(id):
        user = Users.query.get(id)
        if not user:
            return jsonify({'message': "user don't exist", 'data': {}}), 404
        if user:
            try:
                db.session.delete(user)
                db.session.commit()
                result = user_schema.dump(user)
                return jsonify({'message': 'Successfully deleted', 'data': result}), 200
            except:
                return jsonify({'message': 'unable to delete', 'data': {}}), 500

    def get_users():
        users = Users.query.all()
        if users:
            result = users_schema.dump(users)
            return jsonify({'message': 'Successfully fetched', 'data': result}), 201
        return jsonify({'Message': 'Nothing Found', 'data': {}}), 404

    def get_user(id):
        user_flask = Users.query.get(id)
        user_fire = auth.get_user(user_flask.uid)
        if user_fire:
            result = user_schema.dump(user_fire)
            return jsonify({'Message': 'Successfully fetched', 'data': result}), 201
        return jsonify({'message': "user don't exists", 'data': {}}), 404

    def search_by_username(username):
        try:
            return Users.query.filter_by(email=username).first()
        except:
            return None
