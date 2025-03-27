from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_required, current_user
from database import DataBase
from routes.user_manager import users_bp
from models.user import User
from models.car import Car
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login' # When unauthorized redirect to 'login'


# Required by flask_login
@login_manager.user_loader
def load_user(user_id):
    with DataBase() as db:
        user = db.load_user(user_id)
    if user:
        return User(user[0], user[1], user[2], user[4])
    return None


# Register the Blueprint
app.register_blueprint(users_bp, url_prefix='/users')

# Add more blueprints....


@app.route("/")
@login_required
def home():
    with DataBase() as db:
        cars = [Car(*car) for car in db.get_cars_by_owner(current_user.id)]

    return render_template('index.html', user = current_user, cars = cars)


if __name__ == '__main__':
    app.run(debug=True)
