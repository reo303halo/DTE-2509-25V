from flask import Flask, render_template
import requests


app = Flask(__name__)
API_BASE_URL = "http://localhost:5004/api"  # Make sure this matches your API URL

@app.route('/')
def index():
    try:
        # Fetch  data from your API with error handling
        employees = fetch_api_data("/employees")

        departments = fetch_api_data("/departments")
        print(departments) # Make template for departments
        
        return render_template('index.html', employees=employees)
    except Exception as e:
        return render_template('error.html', error=str(e))


# Helper function to fetch data from API with proper error handling
def fetch_api_data(endpoint):

    response = requests.get(f"{API_BASE_URL}{endpoint}", timeout=5)
    response.raise_for_status()  # Raises exception for 4XX/5XX status codes
    return response.json()
    



if __name__ == '__main__':
    app.run(debug=True, port=5002)  # Different port than your API