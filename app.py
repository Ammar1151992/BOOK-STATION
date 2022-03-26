from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from flask_login import current_user, LoginManager
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import UserMixin, login_user, logout_user
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '8699cbd6a17b478370a6f05d29ec1d25'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookdatabase.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Ammarh1151992@localhost/db_books'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
migrate = Migrate(app, db)


# @app.route('/card/<int:id>',methods = ['POST', 'GET'])
# def post(id):
#    if request.method == 'POST':
#       result = request.json
#       user_name = user.query.filter_by(email=form.email.data).first()

 
@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    type_book = book.query.filter_by(type='novels').all()
    if not type_book:
        return redirect('/home')
    # books = select(book).where(book.type=="?",type_book)
    return render_template('home.html', title='Home', books=type_book)
 

@app.before_first_request
def create_db():
    db.create_all()



@app.route("/cart")
def cart():
    return render_template("cart.html", title='cart')


@app.route("/buy")
def buy():
    return render_template("buy.html", title='Buy')





@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user_name = user.query.filter_by(email=form.email.data).first()
        if user_name and bcrypt.check_password_hash(user_name.password, form.password.data):
            login_user(user_name, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('يرجى التحقق من الايميل او الرقم السري', 'error')
    return render_template('login.html', title='Login', form=form)
 
 
@app.context_processor
def base():
    form = SearchForm()
    return dict(form = form )

 
@app.route('/search', methods=['POST'])
def search():
    form = SearchForm()
    posts = book.query
    if form.validate_on_submit():
        books = form.searched.data
        posts = posts.filter(book.name_of_book.like('%' + books + '%')) 
        posts = posts.filter_by().first()  
        return render_template("search.html",
        form = form,
        searched = books,
        posts = posts) 

@app.route("/regist", methods=['GET','POST'])
def regist():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user_name = user(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data, password=hashed_password)
        db.session.add(user_name)
        db.session.commit()
        flash(f'{form.firstname.data}  تم انشاء الحساب بنجاح، من فضلك قم بتسجيل حسابك الان' , 'success')
        return redirect(url_for('login'))
    return render_template('regist.html', title='Register', form=form)
 
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/English_book/<string:type>", methods=['GET'])
def English_book(type):
    if not current_user.is_authenticated:
        return redirect(url_for('regist'))
    type_book = book.query.filter_by(type=type).all()
    if not type_book:
        return redirect('/home')
    return render_template('english_book.html', title='english_book', books=type_book)




@app.route("/Arabic_book/<string:type>", methods=['GET'])
def Arabic_book(type):
    if not current_user.is_authenticated:
        return redirect(url_for('regist'))
    type_book = book.query.filter_by(type=type).all()
    if not type_book:
        return redirect('/home')
    # books = select(book).where(book.type=="?",type_book)
    return render_template('arabic-book.html', title='Arabic-book', books=type_book)


@app.route("/vew_product/<int:id>", methods=['GET'])
def vew_product(id):
    if not current_user.is_authenticated:
        return redirect(url_for('regist'))
    id_book = book.query.filter_by(id=id).first()
    if not id_book:
        return redirect('/home')
    # books = select(book).where(book.type=="?",type_book)
    return render_template('vew_product.html', title='selected', book=id_book)




@app.route("/get_free/<string:type>")
def get_free(type):
    if not current_user.is_authenticated:
        return redirect(url_for('regist'))
    type_book = book.query.filter_by(type=type).all()
    if not type_book:
        return redirect('/home')
    # books = select(book).where(book.type=="?",type_book)
    return render_template("get_free.html", title='get_free', books=type_book)


@app.route("/last_released/<string:type>")
def last_released(type):
    if not current_user.is_authenticated:
        return redirect(url_for('regist'))
    type_book = book.query.filter_by(type=type).all()
    if not type_book:
        return redirect('/home')
    # books = select(book).where(book.type=="?",type_book)
    return render_template("last_released.html", title='last_released', books=type_book)



@app.route("/free_delivery/<string:type>")
def free_delivery(type):
    if not current_user.is_authenticated:
        return redirect(url_for('regist'))
    type_book = book.query.filter_by(type=type).all()
    if not type_book:
        return redirect('/home')
    # books = select(book).where(book.type=="?",type_book)
    return render_template("free_delivery.html", title='free_delivery', books=type_book)



@app.route("/kids/<string:type>")
def kids(type):
    if not current_user.is_authenticated:
        return redirect(url_for('regist'))
    type_book = book.query.filter_by(type=type).all()
    if not type_book:
        return redirect('/home')
    # books = select(book).where(book.type=="?",type_book)
    return render_template("kids.html", title='kids', books=type_book)


@app.route("/discount/<string:type>")
def discount(type):
    if not current_user.is_authenticated:
        return redirect(url_for('regist'))
    type_book = book.query.filter_by(type=type).all()
    if not type_book:
        return redirect('/home')
    # books = select(book).where(book.type=="?",type_book)
    return render_template("discount.html", title='discount', books=type_book)



@app.route("/school/<string:type>")
def school(type):
    if not current_user.is_authenticated:
        return redirect(url_for('regist'))
    type_book = book.query.filter_by(type=type).all()
    if not type_book:
        return redirect('/home')
    # books = select(book).where(book.type=="?",type_book)
    return render_template("school.html", title='school', books=type_book)


@app.route("/business/<string:type>")
def business(type):
    if not current_user.is_authenticated:
        return redirect(url_for('regist'))
    type_book = book.query.filter_by(type=type).all()
    if not type_book:
        return redirect('/home')
    # books = select(book).where(book.type=="?",type_book)
    return render_template("business.html", title='business', books=type_book)



@app.route("/checkout", methods=['GET','POST'])
def checkout():
    # form = RegistrationForm()
    # if form.validate_on_submit():
    #     hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    #     user_name = user(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data, password=hashed_password)
    #     db.session.add(user_name)
    #     db.session.commit()
    #     flash(f'{form.firstname.data}  تم انشاء الحساب بنجاح، من فضلك قم بتسجيل حسابك الان' , 'success')
    #     return redirect(url_for('login'))
    return render_template('checkout.html', title='checkout')







class RegistrationForm(FlaskForm):
    firstname = StringField('الاسم الاول', validators=[DataRequired(), Length(min=2, max=10)], render_kw={"placeholder": "الاسم الاول"})
    lastname = StringField('اسم العائلة', validators=[DataRequired(), Length(min=2, max=10)], render_kw={"placeholder": "اسم العائلة"})
    email = StringField('الايميل', validators=[DataRequired(), Email()], render_kw={"placeholder": "الايميل"})
    password = PasswordField('الرقم السري', validators=[DataRequired()], render_kw={"placeholder": "الرقم السري"}) 
    confirm_password = PasswordField('نأكيد الرقم السري', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "تأكيد الرقم السري"})
     
    submit =SubmitField('انشاء حساب')
    
    def validate_email(self, email):
        user_name = user.query.filter_by(email=email.data).first()
        if user_name:
            raise ValidationError('هذا الحساب مسجل سابقا، يرجى تسجيل حساب اخر')
   
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "الايميل"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "الرقم السري"}) 
    remember = BooleanField('تذكرني')
    submit =SubmitField('تسجيل دخول')
    
    
class UpdateAccountForm(FlaskForm):
    firstname = StringField('الاسم الاول', validators=[DataRequired(), Length(min=2, max=10)], render_kw={"placeholder": "الاسم الاول"})
    lastname = StringField('اسم العائلة', validators=[DataRequired(), Length(min=2, max=10)], render_kw={"placeholder": "اسم العائلة"})
    email = StringField('الايميل', validators=[DataRequired(), Email()], render_kw={"placeholder": "الايميل"})
     
    submit =SubmitField('تحديث الحساب')
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user_name = user.query.filter_by(email=email.data).first()
            if user_name:
                raise ValidationError('هذا الحساب مسجل سابقا، يرجى تسجيل حساب اخر')

class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[DataRequired()])
    submit =SubmitField('بحث')






@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))

class user(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    user_shop = db.relationship('shop',backref='user')
    user_card = db.relationship('card',backref='user')
    def __repr__(self):
        return f"user('{self.firstname}','{self.lastname}','{self.email}')"
    
class book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_book = db.Column(db.String(50), nullable=False)
    date_of_copyright = db.Column(db.String(50))
    author = db.Column(db.String(50))
    price = db.Column(db.String(50), nullable=False)
    des_of_book = db.Column(db.Text)
    type = db.Column(db.String(50), nullable=False)
    image_file = db.Column(db.String(100))
    image_file_1 = db.Column(db.String(100))
    image_file_2 = db.Column(db.String(100))
    image_file_3 = db.Column(db.String(100))
    image_file_4 = db.Column(db.String(100))
    book_shop = db.relationship('shop',backref='book')
    book_card = db.relationship('card',backref='book')
    def __repr__(self):
        return f"book('{self.name_of_book}','{self.date_of_copyright}','{self.author}','{self.price}','{self.des_of_book}','{self.image_file}')"
    
class shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_of_shop = db.Column(db.String(50), nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    def __repr__(self):
        return f"shop('{self.date_of_shop}')"
    
class card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    def __repr__(self):
        return f"card('{self.quantity}','{self.discount}')"



if __name__ == '__main__':
  app.run(debug=True)
  
    
# if __name__ == '__main__':
#   manager.run()