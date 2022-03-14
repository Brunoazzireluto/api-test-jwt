from crypt import methods
from app import app 
from flask import jsonify
from ..views.helper import Auth
from ..views.users import UsersClass

#definindo rota para autenticação
@app.route('/auth', methods=['POST'])
def authenticate():
    return Auth.auth()


@app.route('/v1', methods=["GET"])
@Auth.token_required
def root(current_user):
    return jsonify({'message':f'hello {current_user.name}'})


@app.route('/users', methods=['GET'])
@Auth.token_required
def get_users(current_user):
    return UsersClass.get_users()

@app.route('/users', methods=['POST'])
@Auth.token_required
def post_user(current_user):
    return UsersClass.post_user()

@app.route('/users/<int:id>', methods=['PUT'])
@Auth.token_required
def update_user(current_user, id):
    return UsersClass.update_user(id)

@app.route('/users/<int:id>', methods=['DELETE'])
@Auth.token_required
def delete_user(current_user, id):
    return UsersClass.delete_user(id)

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    return UsersClass.get_user(id)