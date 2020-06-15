from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import Required,Email,Length
from wtforms import ValidationError
from ..models import Subscribe



class BlogForm(FlaskForm):
    
    title = StringField('Title',validators=[Required()])
    description = TextAreaField("What do you have for us today?",validators=[Required()])
    submit = SubmitField('Post your blog')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[Length(0, 64)])
    email = StringField('Email', render_kw={'disabled': ''})
    news_letter = BooleanField('Subscribe to NewsLetter')
    submit = SubmitField('SAVE CHANGES')

class CommentForm(FlaskForm):
	description = TextAreaField('Add comment',validators=[Required()])
	submit = SubmitField('Comment')

class UpdateBlogForm(FlaskForm):
    title=StringField('Title', validators=[Required()])
    description = TextAreaField('edit your blog',validators = [Required()])
    submit = SubmitField('Update')

class SubscribeForm(FlaskForm):
    usename = StringField('Enter your username', validators=[Required()])
    useremail = StringField('Enter your Email Address', validators=[Required(), Email()])
    submit = SubmitField('Subscribe')


    def validate_useremail(self, data_field):
        if Subscribe.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is an account with that email') 
