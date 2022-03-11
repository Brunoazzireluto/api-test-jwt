import datetime
from email.policy import default
from app import db, ma 

"""Definicição da tabela de usuários e seus campos"""
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

"""Definindo o Schema da Marshmallow para facilitar a utilização do JSON"""
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password', 'name', 'email', 'created_on')

user_schema = UserSchema()
users_schema = UserSchema(many=True)