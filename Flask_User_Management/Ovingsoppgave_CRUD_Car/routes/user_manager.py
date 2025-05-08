from flask import render_template, redirect, url_for, request, Blueprint
from flask_login import logout_user, login_required, login_user, current_user, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from database import DataBase
from models.user import User


users_bp = Blueprint('users', __name__) # Creates a Blueprint
login_manager = LoginManager()
login_manager.login_view = 'users.login' # When unauthorized redirect to 'login'


# Required by flask_login
@login_manager.user_loader
def load_user(user_id):
    with DataBase() as db:
        user = db.load_user(user_id)
    if user:
        return User(user[0], user[1], user[2], user[4])
    return None


@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        with DataBase() as db:
            db.create_user(name, email, password)
        return redirect( url_for('users.login') )
    return render_template("users/register.html")


@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        with DataBase() as db:
            user = db.load_user_by_email(email)

            if user and check_password_hash(user[3], password):
                login_user(User(user[0], user[1], user[2], user[4]))
                return redirect( url_for('home') )
            
        return render_template('users/login.html', error = "Invalid credentials")
    return render_template("users/login.html")


@users_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect( url_for("users.login"))


# You can argue if this fits in here or should be elsewhere
@users_bp.route('/profile')
@login_required
def profile():
    return render_template("users/profile.html", user = current_user)
