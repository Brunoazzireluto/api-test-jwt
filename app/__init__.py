from crypt import methods
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object('config')
db  = SQLAlchemy(app)
ma = Marshmallow(app)


from .routes import routes
from .models import users
