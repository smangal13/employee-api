# employee-api
A backend Server using FastAPI in Python. Creating an Employee Data store, with in-memory storage. Creating API endpoints for CRUD operations.

# Project Structure:
``` 
  project-directory/
  |
  ├── main.py            # API implementation.
  ├── test_main.py       # Unit tests for API endpoints.
  ├── report.html        # Generated test report.
  ├── assets/            # (Optional) Additional assets.
  ├── .gitignore         # Git ignore file.
  ├── requirements.txt   # Includes all necessary dependencies
  ├── __pycache__/       # Cache files.
  └── README.md          # Project documentation
  ```

# Documentation:
This Employee Management API provides an easy-to-use platform for managing employee data. It allows users to create, read, update, and delete (CRUD operations) employee information. The data is stored in-memory, meaning that it is not persisted beyond the runtime of the API server. 
The API is built using FastAPI—a modern web framework for building APIs with Python. FastAPI is designed for performance and ease of use. 

# 1. System Requirements
  1. Python 3.7 or higher
  2. pip package manager
  3. Git for version control
  4. VSCode or any other text editor for writing and editing code

# 2. Installation Instructions
  ## Step 1: Install Python 3 (if not already installed)
  Check if Python 3 is already installed by running the following command in the terminal:
     
    python3 --version

  If Python 3 is not installed, download and install it from the official website: [python.org](https://www.python.org/).
  ## Step 2: Install Git (if not already installed)
  Verify if Git is installed by running the following command in the terminal:

    git --version

  If Git is not installed, download and install it from [git-scm.com](https://git-scm.com/).
  ## Step 3: Clone the Repository
  To clone the repository, follow the these steps:
  1. In the terminal navigate to the project directory (where you want to store your project).
  2. Execute the following command:

    git clone https://github.com/smangal13/employee-api.git

  ## Step 4: Set Up Virtual Environment
  To create a Python 3 virtual environment, follow these steps:
  1. In the same project directory as above.
  2. Run the following command to create a new virtual environment:

    python3 -m venv venv

  3. Once the virtual environment is created, activate it:

    source venv/bin/activate

  ## Step 5: Install Required Packages
  1. Install the necessary packages (fastapi,pydantic,uvicorn and pytest) using the requirements.txt file:

    pip install -r requirements.txt

# 3. API Endpoints
  ## 1. Add Employee
  - Endpoint: POST /employeeData
  - Adds a new employee to the in-memory database.
  ## 2. Get All Employees
  - Endpoint: GET /employeeData
  - Returns a list of all employees stored in memory.
  ## 3. Get Employee by ID
  - Endpoint: GET /employeeData/{employee_id}
  - Retrieves a specific employee's information based on their id.
  - Path Parameter: employee_id
  ## 4. Update Employee
  - Endpoint: PUT /employeeData/{employee_id}
  - Updates all details of an employee except their id.
  - Path Parameter: employee_id
  ## 5. Update Specific Employee
  - Endpoint: PATCH /employeeData/{employee_id}
  - Updates only the specific fields of an employee. The id cannot be updated.
  - Path Parameter: employee_id
  ## 6. Delete Employee
  - Endpoint: DELETE /employeeData/{employee_id}
  - Deletes an employee's data from the in-memory list.
  - Path Parameter: employee_id

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

  If the employee exists:

    {
      "message": "Employee data Successfully Deleted"
    }

  If the employee does not exist:

    {
      "detail": "Employee with the given employee_id not found"
    }
  
  ### Update Employee (Changing the employee_id):
  Code:

    curl -X PUT http://127.0.0.1:8000/employeeData/1 \
      -H "Content-Type: application/json" \
      -d '{"id": 2, "name": "John Doe", "department": "Engineering", "position": "Senior Software Engineer", "salary": 80000}'
      
  Expected Output:
  
  If the employee exists:

    {
      "detail": "Employee_id cannot be changed"
    }
    
  If the employee does not exist:

    {
      "detail": "Employee with the given employee_id not found"
    }
    
  ## Step 3: Test Using SwaggerUI (Optional)
  Swagger UI is an interactive web-based interface that allows developers to visualize and interact with an API's endpoints. It auto-generates API documentation from OpenAPI specifications, enabling users to test API requests directly from the browser.

  Perform the same test as Step 2, by using SwaggerUI instead of cURL.
  
  1. Access Swagger UI: Open a browser and go to http://127.0.0.1:8000/docs.
  2. Interact with the API: Use the "Try it out" button for each endpoint, provide the required data, and click "Execute" to test each endpoint.
  3. Review the responses: Swagger UI will show the output directly in the interface, including successful and error responses.

  ![Sample image of Swagger UI interface for the above API](assests/image.png)

  ## Step 4: Unit Testing Using Pytest 
  ### Running Tests:
  To run a specific test file, use:

    pytest test_main.py

  ### Output Display: (Optional)
  To display verbose output:

    pytest -v

  ![Depicting the Execution of the above command](<assests/Pasted Graphic 11.png>)

  To generate coverage report:

    pytest --cov=. test_main.py

  ![Depicting the Execution of the above command](<assests/Pasted Graphic 12.png>)

  To generate HTML test report:

    pytest test_main.py --html=report.html --self-contained-html
    open report.html

  ![Depicting the Test Report](assests/report.html.png)

  ## Step 5: Optional API Documentation using ReDoc
  Redoc is an open-source tool that generates customizable, interactive API documentation from OpenAPI specifications. It provides a clean, user-friendly interface for exploring and understanding APIs with detailed descriptions and response models.

  To access this documentation use the link: [ReDoc](http://127.0.0.1:8000/redoc)

  ![ReDoc UI](assests/image-1.png)

# Contributors
  -***Shreya Mangal***
  ---



