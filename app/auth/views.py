from . import auth
from flask import render_template,redirect,url_for, flash,request
from .. import db
from flask_login import login_user,logout_user,login_required, current_user
from ..models import User, Subscribe
from .forms import LoginForm,RegistrationForm,SubscribeForm,RequestResetPasswordForm, PasswordResetForm, ChangeEmailForm, ChangePasswordForm
from ..email import mail_message

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        
        if user is None or not user.verify_password(login_form.password.data):
            flash('invalid username or password', 'form-error')
            return redirect(url_for('auth.login'))
        login_user(user)
        next_page = request.args.get('next')
        if next_page is None or not next_page.startswith('/'):
            next_page = url_for('main.blogs')
        flash("You are now logged in", 'form-success')
        return redirect(next_page)

    title = "KairuBlog website login"
    return render_template('auth/login.html',login_form = login_form,title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been successfully logged out')
    return redirect(url_for("main.index"))

@auth.route('/register',methods = ["GET","POST"])
def register():
    
    form = RegistrationForm()
    
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        mail_message("Welcome to blogging website","email/welcome_user",user.email,user=user)
        
        return redirect(url_for('auth.login'))
    title = "New Account"
    return render_template('auth/register.html',registration_form = form, title =title)


@auth.route('/subscribe', methods=["GET", "POST"])
def subscribe():
    subscribingform = SubscribeForm()
    if subscribingform.validate_on_submit():
        subscribers = Subscribe(name=subscribingform.usename.data, email=subscribingform.useremail.data)

        db.session.add(subscribers)
        db.session.commit()

        mail_message("Welcome to KairuBlog website...",
                     "email/welcome_user", subscribers.email, subscribers=subscribers)

        return redirect(url_for('main.index'))
    title = "Subscribe to get new update on our website"
    return render_template('auth/subscribe.html', title =title, subscribe_form=subscribingform)