from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import Required,Email,Length
from wtforms import ValidationError



class BlogForm(FlaskForm):
    title = StringField('Title',validators=[Required()])
    description = TextAreaField("What do you have for us today?",validators=[Required()])
    submit = SubmitField('Post your blog')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class EditProfileForm(FlaskForm):
    first_name = StringField('First name', validators=[Length(0, 64)])
    last_name = StringField('Last name', validators=[Length(0, 64)])
    email = StringField('Email', render_kw={'disabled': ''})
    phone_number = StringField('Mobile')
    news_letter = BooleanField('Subscribe to NewsLetter')
    submit = SubmitField('SAVE CHANGES')


class CommentForm(FlaskForm):
	description = TextAreaField('Add comment',validators=[Required()])
	submit = SubmitField('Comment')

class UpdateBlogForm(FlaskForm):
    title=StringField('Title', validators=[Required()])
    description = TextAreaField('edit your blog',validators = [Required()])
    submit = SubmitField('Update')

