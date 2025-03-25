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


