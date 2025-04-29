from flask import Flask, render_template, request, redirect, url_for, session, flash
# pip install flask-WTF
from flask_wtf import CSRFProtect
from database import DataBase
from movie import Movie
import secrets
from forms import MovieForm


app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)
csrf = CSRFProtect(app)


@app.route("/")
def home():
    with DataBase() as db:
        movies = [Movie(*movie) for movie in db.getAllData()]

        #deleted_movie = session["deleted_movie"]
        deleted_movie = session.pop("deleted_movie", None) # Remove after retrieving

        if deleted_movie != None:
            flash(f"Movie '{deleted_movie}' was deleted.")

    return render_template('index.html', movies = movies)


@app.route("/movie/<int:movie_id>")
def movie_info(movie_id):
    with DataBase() as db:
        movie_data = db.getMovieById(movie_id)

        if movie_data:
            movie = Movie(*movie_data)
        else:
            return "Movie not found.", 404 # Error: 404 Not Found
        
    return render_template('movie.html', movie = movie)


@app.route("/add_movie", methods = ["GET", "POST"])
def create():
    form = MovieForm()

    if form.validate_on_submit():
        data = (
            form.title.data, 
            form.year.data, 
            form.country.data, 
            form.genre.data, 
            form.age_rating.data, 
            form.duration.data, 
            form.price.data
        )
        with DataBase() as db:
            db.createMovie(data)

        return redirect ( url_for('home') )

    # GET
    return render_template('create.html', form = form)



@app.route("/delete/<int:movie_id>", methods = ["POST"])
def delete(movie_id):
    with DataBase() as db:
        movie_data = db.getMovieById(movie_id)

        if movie_data:
            movie = Movie(*movie_data)
            db.deleteMovie(movie_id)
            
            session["deleted_movie"] = movie.title # Store in session

            return redirect( url_for("home") )

        else:
            return "Movie not found.", 404 # Error: 404 Not Found


if __name__ == '__main__':
    app.run(debug = True)
