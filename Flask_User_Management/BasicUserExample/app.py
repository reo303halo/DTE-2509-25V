from flask import Flask, render_template
from database import DataBase
from user import User
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
