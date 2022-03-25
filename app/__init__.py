import json
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import firebase_admin
from firebase_admin import credentials
import pyrebase


cred = credentials.Certificate("fire_admin.json")

app = Flask(__name__)
app.config.from_object('config')
db  = SQLAlchemy(app)
ma = Marshmallow(app)
firebase_admin.initialize_app(cred)
pb = pyrebase.initialize_app(json.load(open('fire_config.json')))


from .routes import routes
from .models import users
