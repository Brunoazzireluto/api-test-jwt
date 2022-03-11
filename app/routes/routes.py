from crypt import methods
from app import app 
from flask import jsonify
from ..views import users
from ..views.users import Users

@app.route('/users', methods=['GET'])
def get_users():
    return users.get_users()

@app.route('/users', methods=['POST'])
def post_user():
    return users.post_user()

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    return users.update_user(id)

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    return users.get_user(id)

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    return users.delete_user(id)