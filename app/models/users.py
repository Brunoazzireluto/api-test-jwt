import datetime
from email.policy import default
from app import db, ma

"""Definicição da tabela de usuários e seus campos"""


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)


"""Definindo o Schema da Marshmallow para facilitar a utilização do JSON"""


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'uid', 'name', 'email')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
