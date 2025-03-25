# pip install mysql-connector-python
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

class DataBase():
    def __init__(self):
        self.mysqlConnection = mysql.connector.connect(
            host="localhost", #:3306
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


    def getAllData(self):
        self.cursor.execute("SELECT * FROM film;")
        return self.cursor.fetchall()


    def getMovieById(self, movie_id):
        self.cursor.execute("SELECT * FROM film WHERE fnr = %s;", (movie_id,)) # Note that the single parameter is made as a tuple.
        return self.cursor.fetchone()
    
    # Preventing SQL Injection (Prepared Statements)
    # Ensuring the right data structure
    # Consistency with multiple parameters (making the "connector"-api more predictable)
    
    def createMovie(self, data):
        sql = """
            INSERT INTO film (tittel, år, land, sjanger, alder, tid, pris)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        self.cursor.execute(sql, data)
        return self.cursor.fetchone()