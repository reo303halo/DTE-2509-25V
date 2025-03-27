from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, logout_user, login_required, login_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from database import DataBase
from user import User
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' # When unauthorized redirect to 'login'


# Required by flask_login
@login_manager.user_loader
def load_user(user_id):
    with DataBase() as db:
        user = db.load_user(user_id)
    if user:
        return User(user[0], user[1], user[2], user[4])
    return None


@app.route("/")
@login_required
def home():
    return render_template('index.html', user = current_user)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        with DataBase() as db:
            db.create_user(name, email, password)
        return redirect( url_for('login') )
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        with DataBase() as db:
            user = db.load_user_by_email(email)

            if user and check_password_hash(user[3], password):
                login_user(User(user[0], user[1], user[2], user[4]))
                return redirect( url_for('home') )
            
        return render_template('login.html', error = "Invalid credentials")
    return render_template("login.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect( url_for("login"))


if __name__ == '__main__':
    app.run(debug=True)
