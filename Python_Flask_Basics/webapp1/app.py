# Common names for file: app.py, main.py, __init__.py

from flask import Flask, render_template

app = Flask(__name__) # Creates a Flask application


@app.route('/hello') # URL
def hello():
    return 'Hello, Flask!' 


@app.route('/') #Home page
def index():
    return render_template('index.html')


@app.route('/programming')
def prog():
    languages = [
        "Python",
        "Swift",
        "C++",
        "C#",
        "Kotlin",
        "Java"
    ]
    return render_template('prog.html', prog_lang=languages) #Render list and adds to html


if __name__ == '__main__':
    app.run(debug=True) # Run the Flask application