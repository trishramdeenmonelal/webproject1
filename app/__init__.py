from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://dsygsoqfwyqhul:70990c4f47b06c82028491d14bca5ec78ab59c5158549754938dfd219b54ad5d@ec2-52-73-247-67.compute-1.amazonaws.com:5432/dd8ngic6cd3b7n"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER']="./app/static/uploads"

db = SQLAlchemy(app)



app.config.from_object(__name__)
from app import views