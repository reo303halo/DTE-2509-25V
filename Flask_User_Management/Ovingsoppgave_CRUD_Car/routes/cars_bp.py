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


@cars_bp.route('/cars/add', methods=['GET', 'POST'])
@login_required
def add_car():
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        vin = request.form['vin']
        with DataBase() as db:
            db.add_car(make, model, year, current_user.id, vin)
        return redirect(url_for('cars.all'))
    return render_template('cars/add_edit.html', car=None)


@cars_bp.route('/cars/edit/<int:car_id>', methods=['GET', 'POST'])
@login_required
def edit_car(car_id):
    with DataBase() as db:
        car = Car(*db.get_car_by_id(car_id))

        print(car.id)
        print(car.make)
        print(car.model)
        print(car.year)
        
        if car.owner_id == current_user.id:
            if not car:
                return redirect(url_for('cars.all'))

            if request.method == 'POST':
                make = request.form['make']
                model = request.form['model']
                year = request.form['year']
                vin = request.form['vin']

                print(make, model, year, vin)

                db.update_car(car_id, make, model, year, current_user.id, vin)
                return redirect(url_for('cars.all'))

    return render_template('cars/add_edit.html', car=car)


@cars_bp.route('/cars/delete/<int:car_id>', methods=['POST'])
@login_required
def delete_car(car_id):
    with DataBase() as db:
        car = Car(*db.get_car_by_id(car_id))
        
        if car.owner_id == current_user.id:
            db.delete_car(car_id)
    return redirect(url_for('cars.all'))

