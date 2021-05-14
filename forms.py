from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    first_name = StringField(label='نام')
    last_name = StringField(label='نام خانوادگی')
    username = StringField(label='نام کاربری', validators=[DataRequired(message='این قسمت حتما باید تکمیل گردد.'), Length(min=6, max=20, message='طول نام کاربری باید بین 6 تا 20 کارکتر باشد.')])
    email = StringField(label='ایمیل', validators=[DataRequired(message='این قسمت حتما باید تکمیل گردد.'), Email(message='فرمت ایمیل رعایت نشده است.')])
    password = PasswordField(label='گذرواژه', validators=[DataRequired(message='این قسمت حتما باید تکمیل گردد.'), Length(min=6, max=20, message='طول گذرواژه باید بین 6 تا 20 کارکتر باشد.')])
    confirm_password = PasswordField(label='تایید گذرواژه', validators=[DataRequired(message='این قسمت حتما باید تکمیل گردد.'), Length(min=6, max=20, message='طول گذرواژه باید بین 6 تا 20 کارکتر باشد.'), EqualTo('password', message='گذرواژه‌های وارد شده برابر نیستند.')])
    submit = SubmitField(label='ثبت نام')
    

class LoginForm(FlaskForm):
    username = StringField(label='نام کاربری', validators=[DataRequired(message='این قسمت حتما باید تکمیل گردد.'), Length(min=6, max=20, message='طول نام کاربری باید بین 6 تا 20 کارکتر باشد.')])
    password = PasswordField(label='گذرواژه', validators=[DataRequired(message='این قسمت حتما باید تکمیل گردد.')])
    remember = BooleanField(label='مرا بخاطر بسپار')
    submit = SubmitField(label='ورود')