from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


with app.app_context():
    class Book(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(80), unique=True, nullable=False)
        author = db.Column(db.String(120), nullable=False)
        rating = db.Column(db.Float, nullable=False)

        def __repr__(self):
            return f'<Book {self.title}>'
    
    # db.create_all()

    # new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    # db.session.add(new_book)
    # db.session.commit()

    all_books = db.session.query(Book).all()




class LibraryForm(FlaskForm):
    book_name = StringField('Book Name', validators=[DataRequired()])
    book_author = StringField('Book Author', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])

    submit = SubmitField('Add Book')


@app.route('/')
def home():
    return render_template("index.html", library=all_books)


@app.route("/add", methods=["GET","POST"])
def add():
    form = LibraryForm()    
    if request.method == "POST":
        with app.app_context():
            new_book = Book(title=form.book_name.data, author=form.book_author.data, rating=form.rating.data)
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=form)


@app.route("/edit", methods=["GET","POST"])
def edit():
    if request.method == "POST":
        #UPDATE RECORD
        book_id = request.form["id"]
        with app.app_context():
            book_to_update = Book.query.get(book_id)
            book_to_update.rating = request.form["rating"]
            db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    with app.app_context():
        book_selected = Book.query.get(book_id)
    return render_template("edit_rating.html", book=book_selected)

@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    # DELETE A RECORD BY ID
    with app.app_context():
        book_to_delete = Book.query.get(book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

