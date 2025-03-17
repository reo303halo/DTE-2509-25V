from flask import Flask, render_template
from database import DataBase
from movie import Movie
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)


@app.route("/")
def home():
    with DataBase() as db:
        movies = [Movie(*movie) for movie in db.getAllData()]

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


if __name__ == '__main__':
    app.run(debug = True)
