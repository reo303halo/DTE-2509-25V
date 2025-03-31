from flask import Flask, render_template, redirect, url_for, request
from flask_login import login_required
from routes.user_manager import users_bp, login_manager
from routes.cars_bp import cars_bp
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)
login_manager.init_app(app)

# Register the Blueprint
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(cars_bp, url_prefix='/cars')

# Add more blueprints...


@app.route("/")
@login_required
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
