from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from book.models import user

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