# pip install mysql-connector-python
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class DataBase():
    def __init__(self):
        self.mysqlConnection = mysql.connector.connect(
            host="localhost", #post=3306,
            user="root",
            password=os.getenv("DB_PASSWORD"),
            database="dte_2509"
        )

    def __enter__(self):
        try:
            self.cursor = self.mysqlConnection.cursor()
            return self
        except mysql.connector.Error as error:
            print("Error while connecting to MySQL", error)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.mysqlConnection.commit()
        self.cursor.close()
        self.mysqlConnection.close()


    def load_user(self, user_id):
        self.cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        return self.cursor.fetchone()


    def create_user(self, name, email, password):
        self.cursor.execute("INSERT INTO users (name, email, password_hash, role) VALUES (%s, %s, %s, 'user')", (name, email, password))
        # Default role set to 'user'
        return
    

    def load_user_by_email(self, email):
        self.cursor.execute("SELECT * FROM users WHERE email = %s;", (email,))
        return self.cursor.fetchone()
    

    def get_cars_by_owner(self, owner_id):
        self.cursor.execute("SELECT id, make, model, year, owner_id, vin FROM cars WHERE owner_id = %s;", (owner_id,))
        return self.cursor.fetchall()
    
    def get_car_by_id(self, id):
        self.cursor.execute("SELECT id, make, model, year, owner_id, vin FROM cars WHERE id = %s;", (id,))
        return self.cursor.fetchone()

    def delete_car(self, car_id):
        self.cursor.execute("DELETE FROM cars WHERE id = %s;", (car_id,))

    def add_car(self, make, model, year, owner_id, vin):
        self.cursor.execute(
            "INSERT INTO cars (make, model, year, owner_id, vin) VALUES (%s, %s, %s, %s, %s);",
            (make, model, year, owner_id, vin)
        )

    def update_car(self, car_id, make, model, year, owner_id, vin):
        self.cursor.execute(
            "UPDATE cars SET make = %s, model = %s, year = %s, owner_id = %s, vin = %s WHERE id = %s;",
            (make, model, year, owner_id, vin, car_id)
        )

