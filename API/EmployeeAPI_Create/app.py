from flask import Flask, jsonify, request
from flask_cors import CORS # Cross-Origin Resource Sharing
import secrets
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
app.secret_key = secrets.token_urlsafe(16)


@app.route("/api/departments", methods=["GET"])
def get_departments():
    with DataBase() as db:
        departments = [Department(*dept).to_dict() for dept in db.getDept()]
        return jsonify(departments)
    

@app.route("/api/departments", methods=["POST"])
def create_department():
    data = request.get_json()

    if not data or "dname" not in data or "loc" not in data:
        return jsonify({"error": "Missing required fields: dname, loc"}), 400 # Bad Request
    
    with DataBase() as db:
        deptno = db.createDept((data["dname"], data["loc"]))
        return jsonify({"message": "Department created", "deptno": deptno}), 201 # Created


@app.route("/api/departments/<int:deptno>/employees", methods=["GET"]) # In department, filter by dept_number, fetch employees
def get_employees_by_dept(deptno):
    with DataBase() as db:
        employees = [Employee(*emp).to_dict() for emp in db.getEmpWithDeptno(deptno)]

        if not employees:
            return jsonify({"error": f"No employees was found for department {deptno}"}), 404 # Not Found

        return jsonify(employees)





@app.route("/api/employees", methods=["GET"])
def get_employees():
    with DataBase() as db:
        employees = [Employee(*emp).to_dict() for emp in db.getEmp()]
        return jsonify(employees)
    

@app.route("/api/employees", methods=["POST"])
def create_employee():
    data = request.get_json()

    required_fields = {"ename", "job", "mgr", "hiredate", "sal", "comm", "deptno"}
    if not data or not required_fields.issubset(data.keys()):
        return jsonify({"error": "Missing required fields"}), 400 

    with DataBase() as db:
        empno = db.createEmp((
            data["ename"], data["job"], data["mgr"],
            data["hiredate"], data["sal"], data["comm"], data["deptno"]
        ))
        return jsonify({"message": "Employee created", "empno": empno}), 201


@app.route("/api/employees/jobs", methods=["GET"])
def get_jobs():
    with DataBase() as db:
        return jsonify([job[0] for job in db.getJobsFromEmp()]) # Example: job = ("Salesman", ), job[0] = "Salesman"


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5004)