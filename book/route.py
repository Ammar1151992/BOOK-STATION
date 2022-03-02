from select import select
from flask import render_template, redirect, url_for, flash, request
from book import app, db, bcrypt
from book.models import user, book, shop
from book.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flask_login import login_required, login_user, current_user, logout_user

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title='Home')

@app.before_first_request
def create_db():
    db.create_all()



@app.route("/cart")
def cart():
    return render_template("cart.html", title='cart')



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


@app.route("/english_book")
def english_book():
    return render_template('english_book.html', title='english_book')


@app.route("/arabic_book")
def arabic_book():
    if not current_user.is_authenticated:
        return redirect(url_for('regist'))
    return render_template('arabic_book.html', title='arabic_book')

@app.route("/selected/<string:type>", methods=['GET'])
def selected(type):
    if not current_user.is_authenticated:
        return redirect(url_for('regist'))
    type_book = book.query.filter_by(type=type).all()
    if not type_book:
        return redirect('/home')
    # books = select(book).where(book.type=="?",type_book)
    return render_template('selected.html', title='selected', books=type_book)




# if session.get("user_id", None):
    #     return redirect("/home")

    # if request.method == 'POST':
    #     email = request.form.get("email", None)
    #     password = request.form.get("password", None) 
        
    #     if not email or not password:
    #         return redirect("/login")
        
    #     rows = db.execute("SELECT * FROM User where email=?", email)
    #     if len(rows) < 1:
    #         return redirect("/login")
        
    #     if not password == rows[0]['password']:
    #         return redirect("/login")
        
    #     session['user_id'] = rows[0]['id']
    #     return redirect("/home")
        
    # return render_template("login.html", title='Login')
    
    
    
    
    #  if session.get("user_id", None):
    #     return redirect("/home")
    
    # if request.method == 'POST':
    #     email = request.form.get("email", None)
    #     password = request.form.get("password", None) 
    #     username = request.form.get("username", None)

    #     if not email or not password or not username:
    #         return redirect("/regist")
        
    #     rows = db.execute("SELECT * FROM User where email=?",email)
    #     if len(rows) > 0:
    #         return redirect("/login")
        
    #     rows = db.execute("INSERT INTO User(username,email,password) VALUES(?,?,?)",username,email,password )
    #     session['user_id'] = rows
    #     return redirect("/home")
        
    # return render_template("regist.html", title='Register')


     