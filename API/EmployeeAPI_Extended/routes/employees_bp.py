from flask import Blueprint, request, jsonify
from database import DataBase
from models.employee import Employee


employees_bp = Blueprint("employees", __name__)


@employees_bp.route("/", methods=["GET"])
def get_employees():
    with DataBase() as db:
        employees = [Employee(*emp).to_dict() for emp in db.getEmp()]
        return jsonify(employees)
    

@employees_bp.route("/", methods=["POST"])
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


@employees_bp.route("/jobs", methods=["GET"])
def get_jobs():
    with DataBase() as db:
        return jsonify([job[0] for job in db.getJobsFromEmp()]) # Example: job = ("Salesman", ), job[0] = "Salesman"