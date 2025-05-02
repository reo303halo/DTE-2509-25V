from flask import Flask
from flask_cors import CORS # Cross-Origin Resource Sharing
import secrets
from routes.departments_bp import departments_bp
from routes.employees_bp import employees_bp

app = Flask(__name__)
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://127.0.0.1:5002"],  # Specify origin or ["*"] to allow all origins
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"], # Allowed methods
        "allowed_headers": ["Content-Type"]    # Allowed headers
    }
})
app.secret_key = secrets.token_urlsafe(16)

# Register Blueprints
app.register_blueprint(departments_bp, url_prefix="/api/departments")
app.register_blueprint(employees_bp, url_prefix="/api/employees")
# Add more blueprints...


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5004)