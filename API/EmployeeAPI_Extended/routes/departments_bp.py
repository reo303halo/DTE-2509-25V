from flask import Blueprint, request, jsonify
from database import DataBase
from models.department import Department
from models.employee import Employee


departments_bp = Blueprint("departments", __name__) # Creates the blueprint


@departments_bp.route("/", methods=["GET"]) # /api/departments
def get_departments():
    with DataBase() as db:
        departments = [Department(*dept).to_dict() for dept in db.getDept()]
        return jsonify(departments)
    

@departments_bp.route("/", methods=["POST"])
def create_department():
    data = request.get_json()

    if not data or "dname" not in data or "loc" not in data:
        return jsonify({"error": "Missing required fields: dname, loc"}), 400 # Bad Request
    
    with DataBase() as db:
        deptno = db.createDept((data["dname"], data["loc"]))
        return jsonify({"message": "Department created", "deptno": deptno}), 201 # Created


@departments_bp.route("/<int:deptno>/employees", methods=["GET"]) # In department, filter by dept_number, fetch employees
def get_employees_by_dept(deptno):
    with DataBase() as db:
        employees = [Employee(*emp).to_dict() for emp in db.getEmpWithDeptno(deptno)]

        if not employees:
            return jsonify({"error": f"No employees was found for department {deptno}"}), 404 # Not Found

        return jsonify(employees)
    

@departments_bp.route("/<int:deptno>", methods=["PUT"])
def update_department(deptno):
    data = request.get_json()

    if not data or ("dname" not in data and "loc" not in data):
        return jsonify({"error": "Missing required fields: dname, loc"}), 400 # Bad Request
    
    with DataBase() as db:
        # Check if department exists
        existing_dept = db.getDeptByNo(deptno)
        if not existing_dept:
            return jsonify({"error": f"Department {deptno} not found"}), 404 
        
        # Prepare updated values
        updated_fields = {
            "dname": data.get("dname", existing_dept[1]),
            "loc": data.get("loc", existing_dept[2])
        }

        db.updateDept(deptno, updated_fields["dname"], updated_fields["loc"])
        return jsonify({"message": f"Department {deptno} updated successfully!"})
    

@departments_bp.route("/<int:deptno>", methods=["DELETE"])
def delete_department(deptno):
    with DataBase() as db:
        # Check if department exists
        existing_dept = db.getDeptByNo(deptno)
        if not existing_dept:
            return jsonify({"error": f"Department {deptno} not found"}), 404 
        
        db.deleteDept(deptno)
        return jsonify({"message": f"Department {deptno} deleted successfully!"})
