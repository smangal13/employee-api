# employee-api
A backend Server using FastAPI in Python. Creating an Employee Data store, with in-memory storage. Creating API endpoints for CRUD operations.


# Documentation:
This Employee Management API provides an easy-to-use platform for managing employee data. It allows users to create, read, update, and delete (CRUD operations) employee information. The data is stored in-memory, meaning that it is not persisted beyond the runtime of the API server. 
The API is built using FastAPI—a modern web framework for building APIs with Python. FastAPI is designed for performance and ease of use. 

# 1. System Requirements
  Python 3.7 or higher
  pip package manager
  Git for version control
  VSCode or any other text editor for writing and editing code

# 2. Installation Instructions
  ## Step 1: Install Python 3 (if not already installed)
  Check if Python 3 is already installed by running the following command in the terminal:
    ```bash
    python3 --version
  If Python 3 is not installed, download and install it from the official website: python.org.
  ## Step 2: Install Git (if not already installed)
  Verify if Git is installed:
    git --version
  If Git is not installed, download and install it from git-scm.com.
  ## Step 3: Set Up Virtual Environment
  To create a Python 3 virtual environment, follow these steps:
    Open the terminal.
    Navigate to the project directory (where you want to store your project).
    Run the following command to create a new virtual environment:
      python3 -m venv venv
  ## Step 4: Install Required Packages
  Once the virtual environment is created, activate it:
    source venv/bin/activate  
  Install the necessary packages (fastapi,pydantic and uvicorn):
    pip install fastapi uvicorn
    pip install pydantic

# 3. API Endpoints
  ## 1. Add Employee
    Endpoint: POST /employeeData
    Adds a new employee to the in-memory database.
  ## 2. Get All Employees
    Endpoint: GET /employeeData
    Returns a list of all employees stored in memory.
  ## 3. Get Employee by ID
    Endpoint: GET /employeeData/{employee_id}
    Retrieves a specific employee's information based on their id.
    Path Parameter: employee_id
  ## 4. Update Employee
    Endpoint: PUT /employeeData/{employee_id}
    Updates all details of an employee except their id.
    Path Parameter: employee_id
  ## 5. Update Specific Employee
    Endpoint: PATCH /employeeData/{employee_id}
    Updates only the specific fields of an employee. The id cannot be updated.
    Path Parameter: employee_id
  ## 6. Delete Employee
    Endpoint: DELETE /employeeData/{employee_id}
    Deletes an employee's data from the in-memory list.
    Path Parameter: employee_id

# 4. Testing and Running the API
  ## Step 1: Run the FastAPI Server
  To run the FastAPI server, use Uvicorn:
    uvicorn main:app --reload
  This starts the server on http://127.0.0.1:8000.
  The environment needs to be active and you need to be in the directory where the code is stored in your system. 
  ## Step 2: Test Endpoints with cURL (Manual Testing)
  To test using cURL open a new terminal and run the following codes to test each API endpoint.
  
  ### Add Employee:
    Code:
    curl -X POST http://127.0.0.1:8000/employeeData \
      -H "Content-Type: application/json" \
      -d '{"id": 1, "name": "John Doe", "department": "Engineering", "position": "Software Engineer", "salary": 75000}'
    
    Expected Output:
    {
      "message": "Employee Data Successfully stored!",
      "employee": {
        "id": 1,
        "name": "John Doe",
        "department": "Engineering",
        "position": "Software Engineer",
        "salary": 75000
      }
    }
    
  ### Get All Employees:
    Code:
    curl -X GET http://127.0.0.1:8000/employeeData \
      -H "Content-Type: application/json"
    
    Expected Output: A JSON array of Employees
    [
      {
        "id": 1,
        "name": "John Doe",
        "department": "Engineering",
        "position": "Software Engineer",
        "salary": 75000
      }
    ]
    
  ### Get Employee by ID:
    Code:
    curl -X GET http://127.0.0.1:8000/employeeData/1 \
      -H "Content-Type: application/json"
    
    Expected Output:
    If the employee exists:
    {
      "id": 1,
      "name": "John Doe",
      "department": "Engineering",
      "position": "Software Engineer",
      "salary": 75000
    }
    
    If the employee does not exist:
    {
      "detail": "Employee with the given employee_id not found"
    }
    
  ### Update Employee:
    Code:
    curl -X PUT http://127.0.0.1:8000/employeeData/1 \
      -H "Content-Type: application/json" \
      -d '{"id": 1, "name": "John Doe", "department": "Engineering", "position": "Senior Software Engineer", "salary": 80000}'
      
    Expected Output:
    If the employee exists:
    {
      "message": "Employee data Successfully Updated",
      "employee": {
        "id": 1,
        "name": "John Doe",
        "department": "Engineering",
        "position": "Senior Software Engineer",
        "salary": 80000
      }
    }
    
    If the employee does not exist:
    {
      "detail": "Employee with the given employee_id not found"
    }
    
  ### Update Specific Employee Details:
    Code:
    curl -X PATCH http://127.0.0.1:8000/employeeData/1 \
      -H "Content-Type: application/json" \
      -d '{"salary": 85000}'
      
    Expected Output:
    If the employee exists:
    {
      "message": "Employee data Successfully Updated",
      "employee": {
        "id": 1,
        "name": "John Doe",
        "department": "Engineering",
        "position": "Senior Software Engineer",
        "salary": 85000
      }
    }
    
    If the employee does not exist:
    {
      "detail": "Employee with the given employee_id not found"
    }
    
  ### Delete Employee:
    Code:
    curl -X DELETE http://127.0.0.1:8000/employeeData/1 \
      -H "Content-Type: application/json"
    
    Expected Output:
    {
      "message": "Employee data Successfully Deleted"
    }
    
  ## Step 3: Test Using SwaggerUI (Optional)
  Perform the same test as Step 2, by using SwaggerUI instead of cURL.
    Access Swagger UI: Open a browser and go to http://127.0.0.1:8000/docs.
    Interact with the API: Use the "Try it out" button for each endpoint, provide the required data, and click "Execute" to test each endpoint.
    Review the responses: Swagger UI will show the output directly in the interface, including successful and error responses.

  ## Step 4: Unit Testing Using Pytest
    1. Download the necessary dependencies:
      pip install pytest pytest-asyncio
    
    2. Running Tests:
      To run a specific test file, use:
        pytest test_main.py
      To run a specific test within the file:
        pytest -k "test_function_name" test_main.py

    3. Output Display: (Optional)
        To display verbose output:
          pytest -v
        To generate coverage report:
          pip install pytest-cov
          pytest --cov=. test_main.py
        To generate HTML test report:
          pip install pytest-html
          pytest test_main.py --html=report.html --self-contained-html
          open report.html



