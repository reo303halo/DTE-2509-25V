# Common names for file: app.py, main.py, __init__.py

from flask import Flask, render_template, url_for
from book import Book

app = Flask(__name__) # Creates a Flask application


@app.route('/hello') # URL
def hello():
    return 'Hello, Flask!' 


@app.route('/') #Home page / about_html
def index():
    return render_template('index.html')

@app.route('/about_web') #Home page
def web_dev():
    return render_template('web_dev.html')

@app.route('/about_flask') #Home page
def intro_flask():
    return render_template('intro_flask.html')


@app.route('/recommended_books')
def books():
    rec_books= [
        Book("Flask Web Development", "Miguel Grinberg", 2018),
        Book("Python Crash Course", "Eric Matthes", 2015),
        Book("Databasesystemer", "Bjørn Kristoffersen", 2019),
        Book("Clean Codes", "Martin", 2016)
    ]
    return render_template('books.html', rec_books=rec_books) #Render list and adds to html


if __name__ == '__main__':
    app.run(debug=True) # Run the Flask application