from flask import Flask, jsonify
from database import DataBase
from car import Car


app = Flask(__name__)


@app.route("/api/message", methods=["GET"])
def message():
    return jsonify({"message": "Hello, World!"})


@app.route("/api/cars", methods=["GET"])
def get_all_cars():
    with DataBase() as db:
        cars = [Car(*car).to_dict() for car in db.get_cars()]

        return jsonify(cars)


if __name__ == '__main__':
    app.run(debug=True)