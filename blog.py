from flask import Flask, render_template, flash, redirect, url_for
from flask.helpers import url_for
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)
app.config['SECRET_KEY'] = 'a73f41f2b4c06f9e9d27a325b8479637'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image = db.Column(db.String(20), nullable=False, default='default.png')
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User({self.username}, {self.email}, {self.image})"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Post({self.title}, {self.date_posted})"




@app.route('/')
def home():
    return render_template(
        template_name_or_list='home.html',
        posts=posts
    )


@app.route('/about')
def about():
    return render_template(
        template_name_or_list='about.html',
        title='درباره من'
    )




@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(message=f"حساب کاربری برای {form.username.data} ایجاد شد!", category='success')
        return redirect(url_for('home'))
    return render_template(
        template_name_or_list='register.html',
        title='ثبت نام',
        form=form
    )
    

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(message=f"{{form.first_name.data}}، خوش آمدید!", category='success')
        return redirect(url_for('home'))
    else:
        flash(message=f"ورود شما با خطا همراه بوده است! لطفاً نام کاربری و گذرواژه خود را بررسی نمایید.", category='danger')
    return render_template(
        template_name_or_list='login.html',
        title='ورود',
        form=form
    )


if __name__ == '__main__':
  app.run(
      host='127.0.0.1',
      port=8000,
      debug=True
    )