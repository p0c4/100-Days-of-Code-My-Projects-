from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

tmdbkey = "16784bd3fece5ddb139f8b61cad2697e"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with app.app_context():
    class Movie(db.Model):
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        title = db.Column(db.String(259), unique=True, nullable=False)
        year = db.Column(db.Integer, nullable=False)
        description = db.Column(db.String(500), nullable=False)
        rating = db.Column(db.Float, nullable=True)
        ranking = db.Column(db.Integer, nullable=True)
        review = db.Column(db.String(250), nullable=True)
        img_url = db.Column(db.String(250), nullable=False)

        def __repr__(self):
            return f'<Movie {self.title}>'
    
    db.create_all()


class MovieForm(FlaskForm):
    rating = StringField('Your Rating Out of 10 e.g. 7.5')
    review = StringField('Your Review')
    submit = SubmitField('Change Rating')

class AddMovieForm(FlaskForm):
    title = StringField('Movie title')
    submit = SubmitField('Add Movie')


@app.route("/")
def home():
    with app.app_context():
        all_movies = Movie.query.order_by(Movie.rating).all()
        for i in range(len(all_movies)):
            all_movies[i].ranking = len(all_movies) - i
        db.session.commit()
        return render_template("index.html", library=all_movies)


@app.route("/edit", methods=["GET","POST"])
def edit():
    form=MovieForm()
    movie_id = request.args.get('id')
    with app.app_context():
        movie = Movie.query.get(movie_id)
    print(movie)        
    if request.method== "POST":
        with app.app_context():
            movie = Movie.query.get(movie_id)
            movie.rating = float(form.rating.data)
            movie.review = form.review.data
            db.session.commit()
            print("commit done")
            return redirect(url_for('home'))    
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    # DELETE A RECORD BY ID
    with app.app_context():
        movie_to_delete = Movie.query.get(movie_id)
        db.session.delete(movie_to_delete)
        db.session.commit()
        return redirect(url_for('home'))


@app.route("/add", methods=["GET","POST"])
def add():
    form = AddMovieForm()    
    if request.method == "POST":
        title = form.title.data        
        parameters = {"api_key": tmdbkey, "query": title}
        response = requests.get("https://api.themoviedb.org/3/search/movie", params=parameters)
        data = response.json()["results"]
        return render_template("select.html", data=data)
    return render_template("add.html", form=form)


@app.route("/find")
def find_movie():
    movie_id = request.args.get("id")
    if movie_id:
        parameters = {"api_key": tmdbkey}
        response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}", params=parameters)
        data = response.json()
        with app.app_context():
            new_movie = Movie(
                title=data["title"], 
                year=data["release_date"].split("-")[0], 
                img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
                description=data["overview"]
            )
            db.session.add(new_movie)
            db.session.commit()
            return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
