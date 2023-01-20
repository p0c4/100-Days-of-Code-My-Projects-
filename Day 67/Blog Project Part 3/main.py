from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
with app.app_context():
    class BlogPost(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(250), unique=True, nullable=False)
        subtitle = db.Column(db.String(250), nullable=False)
        date = db.Column(db.String(250), nullable=False)
        body = db.Column(db.Text, nullable=False)
        author = db.Column(db.String(250), nullable=False)
        img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post", )


@app.route('/')
def get_all_posts():
    with app.app_context():
        posts = BlogPost.query.all()        
        return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    with app.app_context():
        requested_post = BlogPost.query.get(post_id)
        return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/new-post", methods=["GET", "POST"])
def create_new_post():
    form = CreatePostForm()
    date_time = datetime.now()
    if request.method == "POST":
        with app.app_context():
            new_post = BlogPost(
                title = form.title.data,
                subtitle = form.subtitle.data,
                date = f"{date_time.strftime('%B')}{date_time.strftime('%d')}, {date_time.year}",
                body = form.body.data,
                author = form.author.data,
                img_url = form.img_url.data
            )
            db.session.add(new_post)
            db.session.commit()
        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=form)

@app.route("/edit_post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    with app.app_context():
        requested_post = BlogPost.query.get(post_id)
        form = CreatePostForm(
                title=requested_post.title,
                subtitle=requested_post.subtitle,
                img_url=requested_post.img_url,
                author=requested_post.author,
                body=requested_post.body
        )
        if form.validate_on_submit():
            requested_post.title = form.title.data
            requested_post.subtitle = form.subtitle.data
            requested_post.img_url = form.img_url.data
            requested_post.author = form.author.data
            requested_post.body = form.body.data    
            db.session.commit()
            return redirect(url_for("show_post", post_id=requested_post.id))
    return render_template("make-post.html", form=form, is_edit=True)

@app.route("/delete/<post_id>", methods=["GET", "POST"])
def delete_post(post_id):    
    with app.app_context():
        post_to_delete = BlogPost.query.get(post_id)
        db.session.delete(post_to_delete)
        db.session.commit()
    return redirect(url_for('get_all_posts'))

if __name__ == "__main__":
    app.run(debug=True)