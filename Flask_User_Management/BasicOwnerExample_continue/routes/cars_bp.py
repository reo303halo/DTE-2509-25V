from flask import render_template, redirect, url_for, request, Blueprint
from flask_login import login_required, current_user
from database import DataBase
from models.car import Car


cars_bp = Blueprint('cars', __name__) # Creates a Blueprint


@cars_bp.route('/cars')
@login_required
def all():
    with DataBase() as db:
        cars = [Car(*car) for car in db.get_cars_by_owner(current_user.id)]

    return render_template('cars/read.html', cars = cars)