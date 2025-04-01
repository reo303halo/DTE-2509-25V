from flask import Flask, jsonify
from flask_cors import CORS # Cross-Origin Resource Sharing
from database import DataBase
from models.department import Department
from models.employee import Employee

app = Flask(__name__)
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://127.0.0.1:5002"],  # Specify origin or ["*"] to allow all origins
        "methods": ["GET", "POST", "OPTIONS"], # Allowed methods
        "allowed_headers": ["Content-Type"]    # Allowed headers
    }
})


@app.route("/api/departments")
def get_departments():
    with DataBase() as db:
        departments = [Department(*dept).to_dict() for dept in db.getDept()]
        return jsonify(departments)


@app.route("/api/employees")
def get_employees():
    with DataBase() as db:
        employees = [Employee(*emp).to_dict() for emp in db.getEmp()]
        return jsonify(employees)


@app.route("/api/departments/<int:deptno>/employees") # In department, filter by dept_number, fetch employees
def get_employees_by_dept(deptno):
    with DataBase() as db:
        employees = [Employee(*emp).to_dict() for emp in db.getEmpWithDeptno(deptno)]
        return jsonify(employees)
    

@app.route("/api/jobs")
def get_jobs():
    with DataBase() as db:
        return jsonify([job[0] for job in db.getJobsFromEmp()]) # Example: job = ("Salesman", ), job[0] = "Salesman"


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5004)