from datetime import datetime
from email.policy import default
from book import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))

class user(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    user = db.relationship('shop',backref='user')
    def __repr__(self):
        return f"user('{self.firstname}','{self.lastname}','{self.email}')"
    
class book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_book = db.Column(db.String(50), nullable=False)
    date_of_copyright = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    price = db.Column(db.String(50), nullable=False)
    des_of_book = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    image_file = db.Column(db.String(100), unique=True, nullable=False)
    book = db.relationship('shop',backref='book')
    def __repr__(self):
        return f"book('{self.name_of_book}','{self.date_of_copyright}','{self.author}','{self.price}','{self.des_of_book}','{self.image_file}')"
    
class shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_of_shop = db.Column(db.String(50), nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    def __repr__(self):
        return f"shop('{self.date_of_shop}')"