from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError,SelectField
from wtforms.validators import Required,Email,EqualTo,Length
from ..models import User



class LoginForm(FlaskForm):
    email = StringField('Email:',validators=[Required(),Email(),Length(1, 64) ], render_kw={"placeholder": "e.g janedoe@pizzatoday.com"})
    password = PasswordField('Password:',validators =[Required()], render_kw={"placeholder": "Your password"})
    remember = BooleanField('Remember me')
    submit = SubmitField('LogIn')


class RegistrationForm(FlaskForm):
    email = StringField('Email:',validators=[Required(), Email(),Length(1, 64)], render_kw={"placeholder": "Enter your email address"})
    first_name = StringField('First name:', validators=[Required()], render_kw={"placeholder": "Enter your First Name"})
    last_name = StringField('Last name:', validators=[Required()], render_kw={"placeholder": "Enter your Last Name"})
    password = PasswordField('Password:',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')], render_kw={"placeholder": "Prefered password"})
    password_confirm = PasswordField('Confirm Password:',validators = [Required()], render_kw={"placeholder": "Confirm password"})
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
                if User.query.filter_by(email =data_field.data).first():
                    raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')


class RequestResetPasswordForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Email(), Length(1, 64)])
    submit = SubmitField('Reset Password')


class PasswordResetForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Email(), Length(1, 64)])
    password = PasswordField('New Password', validators=[
        Required(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Confirm new Password', validators=[Required()])
    submit = SubmitField('Reset Password')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('Unknown email address!')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old Password', validators=[Required()])
    password = PasswordField('New Password', validators=[
        Required(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Confirm new Password', validators=[Required()])
    submit = SubmitField('Update password')


class ChangeEmailForm(FlaskForm):
    email = StringField('New Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Update email')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already in use!")  


class SubscribeForm(FlaskForm):
    usename = StringField('Enter your username', validators=[Required()])
    useremail = StringField('Enter your Email Address', validators=[Required(), Email()])
    submit = SubmitField('Subscribe')

    def validate_usename(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('That username is taken')

    def validate_useremail(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is an account with that email') 