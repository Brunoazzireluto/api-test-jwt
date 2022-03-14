import datetime
import jwt
from werkzeug.security import check_password_hash
from flask import request, jsonify
from functools import wraps
from .users import UsersClass
from app import app

class Auth():


    def auth():
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return jsonify({'message':'Could not Verify', 'WWW-Authenticate':'Basic auth ="Login required"'}), 401

        user = UsersClass.search_by_username(auth.username)
        if not user:
            return jsonify({'Message':'User not found', 'data':'{}'}), 401

        if user and check_password_hash(user.password, auth.password):
            token = jwt.encode({
                'username':user.username, 
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }, app.config['SECRET_KEY'])
            return jsonify({
                'message':'Validated Successfully',
                'token':token,
                'exp': datetime.datetime.now() + datetime.timedelta(hours=1)
            })
        return jsonify({'message':'Could not Verify', 'WWW-Authenticate':'Basic auth ="Login required"'}), 401

    def token_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.args.get('token')
            if not token:
                return jsonify({'message': 'token is missing', 'data':{}}), 401
            try:
                data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=['HS256'])
                current_user = UsersClass.search_by_username(username=data['username'])
            except:
                return jsonify({'message':'token is invalid or expired', 'data':{}}), 401
            return f(current_user, *args, **kwargs)
        return decorated




        
