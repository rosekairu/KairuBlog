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
            next_page = url_for('main.index')
        flash("You are now logged in", 'form-success')
        return redirect(next_page)

    title = "Kai's Blog website login"
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
        mail_message("Welcome to Kai's Blog","email/welcome", user.email,user=user)
        
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

        mail_message("Welcome to Kai's Blog...", "email/subscribing", subscribers.email, subscribers=subscribers)
        
        flash('You have been successfully Subscribed')
        return redirect(url_for('main.index'))
        
    title = "Subscribe to get new updates"
    return render_template('auth/subscribe.html', title =title, subscribe_form=subscribingform)


@auth.route('/reset', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RequestResetPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            token = user.generate_reset_token()
            send_email(user.email, 'Reset your Password',
                       'bp/email/reset_password',
                       user=user, token=token)
            flash('A password reset link has been sent to {}'.format(
                form.email.data), 'form-info')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password.html', form=form, title='Password Reset')


@auth.route('/reset/<token>', methods=['GET', 'POST'])
def password_reset(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = PasswordResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash('Invalid email address!', 'form-error')
            return redirect(url_for('main.index'))
        if user.password_reset(token, form.password.data):
            flash('Your password has been updated!', 'form-success')
            return redirect(url_for('auth.login'))
        else:
            flash('The password link is invalid or has expired', 'form-error')
    return render_template('auth/email/reset_password.html', form=form)


@auth.route('/change-email/<token>')
@login_required
def change_email(token):
    if current_user.change_email(token):
        db.session.commit()
        flash("Email address has been updated!", 'form-success')
    else:
        flash("Invalid request", 'form-warning')
    return redirect(url_for('auth.login'))


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.new_blog'))
    if current_user.confirm(token):
        flash('You have confirmed your account', 'form-success')
    else:
        flash('The confirmation link is invalid or has expired ', 'form-error')
    return redirect(url_for('main.index'))


@auth.route('/user/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.password.data
            db.session.add(current_user)
            db.session.commit()
            flash("your password has been updated!", 'form-success')
            return redirect(url_for('auth.login'))
        else:
            flash('Invalid password', 'form-error')
    return render_template('auth/change_password.html', form=form)


@auth.route('/user/change-email', methods=['GET', 'POST'])
@login_required
def change_email_request():
    form = ChangeEmailForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.password.data):
            new_email = form.email.data
            token = current_user.generate_change_email_token(new_email)
            send_email(new_email, 'Confirm your email address',
                       'auth/email/change_email',
                       user=current_user, token=token)
            flash('A confirmation link has been sent to {}'.format(new_email),
                  'form-info')
            return redirect(url_for('auth.login'))
        flash('Invalid email address', 'form-error')
    return render_template('auth/change_email.html', form=form)