from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '8699cbd6a17b478370a6f05d29ec1d25'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookdatabase.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Ammarh1151992@localhost/db_books'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# app.config['SESSION_PERMANENT'] = False
# app.config['SESSION_TYPE'] = "fileseystem"
from book import route
from book import forms



