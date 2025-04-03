from flask import Flask, render_template
import requests


app = Flask(__name__)
API_BASE_URL = "http://localhost:5004/api"  # Make sure this matches your API URL

@app.route('/')
def index():
    try:
        # Fetch  data from your API with error handling
        employees = fetch_api_data("/employees")

        departments = fetch_api_data("/departments") # Make template for departments
        print(departments) 
        
        return render_template('index.html', employees=employees)
    except Exception as e:
        return render_template('error.html', error=str(e))


@app.route("/dept")
def departments():
    try: 
        departments = fetch_api_data("/departments") 
        
        return render_template('department.html', departments=departments) # Template not implemented
    except Exception as e:
        return render_template('error.html', error=str(e))


# Helper function to fetch data from API with proper error handling
def fetch_api_data(endpoint):
    try:
        response = requests.get(f"{API_BASE_URL}{endpoint}", timeout=5)
        response.raise_for_status()  # Raises an exception for 4XX/5XX status codes
        return response.json()
    
    except requests.Timeout:
        print(f"Error: Request to {endpoint} timed out.")
    except requests.ConnectionError:
        print(f"Error: Unable to connect to {API_BASE_URL}. Check your internet connection.")
    except requests.HTTPError as http_err:
        print(f"HTTP error {response.status_code}: {http_err}")
    except requests.RequestException as req_err:
        print(f"Unexpected error: {req_err}")
    return None  # Return None in case of failure

    

if __name__ == '__main__':
    app.run(debug=True, port=5002)  # Different port than your API