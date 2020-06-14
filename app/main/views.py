import markdown2, os
from flask import render_template,request,redirect,url_for,abort, flash
from . import main
from werkzeug.utils import secure_filename
from .forms import BlogForm, CommentForm, UpdateProfile, UpdateBlogForm
from .. import db, photos
from ..models import PhotoProfile, Blog, User, Comment
from flask_login import login_required, current_user
from ..requests import get_quote



def allowed_image(filename):

    # only want files with a . in the filename
    if not "." in filename:
        return False

    # Split the extension from the filename
    ext = filename.rsplit(".", 1)[1]

    # Check if the extension is in ALLOWED_IMAGE_EXTENSIONS
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

def allowed_image_filesize(filesize):

    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False


@main.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":

        if request.files:

            if "filesize" in request.cookies:

                if not allowed_image_filesize(request.cookies["filesize"]):
                    print("Filesize exceeded maximum limit")
                    return redirect(request.url)

                image = request.files["image"]

                if image.filename == "":
                    print("No filename")
                    return redirect(request.url)

                if allowed_image(image.filename):
                    filename = secure_filename(image.filename)

                    image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

                    print("Image saved")

                    return redirect(request.url)

                else:
                    print("That file extension is not allowed")
                    return redirect(request.url)

        return render_template("public/upload_image.html")


# Views
@main.route('/', methods = ['GET','POST'])
def index():

    '''
    View root page function that returns the index page and its data
    '''

    blog= Blog.query.all()
    quote = get_quote()
    title = 'Home - Welcome to our KairuBlog-app Website Online'

    return render_template('index.html', title = title, blog = blog, quote=quote )


@main.route('/blogs/new/', methods = ['GET', 'POST'])
@login_required
def new_blog():
    form = BlogForm()

    if form.validate_on_submit():
       description = form.description.data
       title = form.title.data
       user_id = current_user
   
       print(current_user._get_current_object().id)
       new_blog = Blog(user_id = current_user._get_current_object().id, title = title, description=description)
       db.session.add(new_blog)
       db.session.commit()
       return redirect(url_for('main.index'))
    
    return render_template('blog.html',form=form)


@main.route('/comment/new/<int:blog_id>', methods = ['GET','POST'])
@login_required
def new_comment(blog_id):
    form = CommentForm()
    blog=Blog.query.get(blog_id)
    if form.validate_on_submit():
        description = form.description.data

        new_comment = Comment(description = description, user_id = current_user._get_current_object().id, blog_id = blog_id)
        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('.new_comment', blog_id= blog_id))

    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
    return render_template('comment.html', form = form, comment = all_comments, blog = blog )


@main.route('/profile/dltcmts/<int:blog_id>',methods = ['GET','POST'])
@login_required
def delete_Comment(blog_id):
    blog=Blog.query.filter_by(id = blog_id).first()

    if blog.comments:
       for comment in comments:
           db.session.delete(comment)
           db.session.commit()
           user = current_user
           
           db.session.delete(comment)
           db.session.commit()
           
           return redirect(url_for('.profile', uname=user.username))
    return render_template('profile/profile.html', user=user) 


@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    get_blogs = Blog.query.filter_by(user_id = current_user.id).all()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, description = get_blogs)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        user_photo = PhotoProfile(pic_path = path,user = user)
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/profile/delete/<int:blog_id>',methods = ['GET','POST'])
@login_required
def delete_blog(blog_id):
    blog=Blog.query.filter_by(id = blog_id).first()
    comments=blog.comments
    if blog.comments:
       for comment in comments:
           db.session.delete(comment)
           db.session.commit()

    user = current_user
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('.profile', uname=user.username))
    return render_template('profile/profile.html', user=user) 


@main.route('/profile/update/<int:blog_id>',methods = ['GET','POST'])
@login_required
def UpdateBlog(blog_id):
    owner = Blog.query.filter_by(id=blog_id).first()
    if owner is None:
        abort(404)
    user = current_user
    form = UpdateBlogForm()

    if form.validate_on_submit():
        owner.description = form.description.data
        owner.title = form.title.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/edit.html',form = form, user = user )