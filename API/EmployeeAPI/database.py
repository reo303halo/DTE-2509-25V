# pip install mysql-connector-python
# pip install dotenv
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


    def getDept(self):
        self.cursor.execute("SELECT * FROM dept;")
        return self.cursor.fetchall()
    
    def getEmp(self):
        self.cursor.execute("SELECT * FROM emp;")
        return self.cursor.fetchall()
    
    def getEmpWithDeptno(self, deptno):
        self.cursor.execute("SELECT * FROM emp WHERE deptno = %s;", (deptno,))
        return self.cursor.fetchall()

    def getJobsFromEmp(self):
        self.cursor.execute("SELECT distinct job FROM emp;")
        return self.cursor.fetchall()
    


