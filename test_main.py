import pytest
from fastapi.testclient import TestClient
from main import app, employees, Employee, UpdateEmployee
from fastapi import HTTPException


# Create a test client instance using the app object (FastAPI object)
client = TestClient(app)


# Tests to check Basic Functionality
# Test POST: Add an employee
def test_add_employee():
    employee_data = {
        "id": 1,
        "name": "John Doe",
        "department": "Engineering",
        "position": "Software Engineer",
        "salary": 70000.0
    }

    initial_num_enteries = len(employees)

    response = client.post("/employeeData", json=employee_data)
    
    assert response.status_code == 200
    assert response.json() == {
        "message": "Employee Data Successfully stored!",
        "employee": employee_data
    }

    # Verify that employee is added to in-memory list
    curr_num_enteries = len(employees)
    assert curr_num_enteries - initial_num_enteries == 1
    assert employees[curr_num_enteries - 1].id == 1

# Test GET: Retrieve all employees
def test_get_all_employees():
    response = client.get("/employeeData")

    # Verifying that the employees were retrieved
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == len(employees)

# Test GET: Retrieve employee by ID
def test_get_employee_by_id():
    response = client.get("/employeeData/1")

    # Verifying that the correct employee was retrieved
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "John Doe",
        "department": "Engineering",
        "position": "Software Engineer",
        "salary": 70000.0
    }

# Test PUT: Update employee's data (full update)
def test_update_employee():
    updated_employee = {
        "id": 1,
        "name": "John Doe",
        "department": "Engineering",
        "position": "Senior Software Engineer",
        "salary": 90000.0
    }

    response = client.put("/employeeData/1", json=updated_employee)

    assert response.status_code == 200
    assert response.json() == {
        "message": "Employee data Successfully Updated",
        "employee": updated_employee
    }

    # Verifying that the employee data was actually updated
    assert employees[0].position == "Senior Software Engineer"
    assert employees[0].salary == 90000.0

# Test PATCH: Update specific fields of an employee
def test_update_specific_employee():
    updated_fields = {
        "salary": 95000.0
    }

    response = client.patch("/employeeData/1", json=updated_fields)

    assert response.status_code == 200
    assert response.json() == {
        "message": "Employee data Successfully Updated",
        "employee": {
            "id": 1,
            "name": "John Doe",
            "department": "Engineering",
            "position": "Senior Software Engineer",
            "salary": 95000.0
        }
    }

    # Verifying the salary update
    assert employees[0].salary == 95000.0

# Test DELETE: Delete an employee by ID
def test_delete_employee():
    response = client.delete("/employeeData/1")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Employee data Successfully Deleted"
    }

    # Verifying that the employee list is empty
    assert len(employees) == 0



# Tests to Check Error Handling Functionality
# Test error handling for employee not found (GET by ID)
def test_get_employee_not_found():
    response = client.get("/employeeData/999")  # Employee with ID 999 does not exist

    assert response.status_code == 404
    assert response.json() == {"detail": "Employee with the given employee_id not found"}

# Test error handling for adding an employee with an existing ID
def test_add_employee_with_existing_id():
    employee_data = {
        "id": 1,
        "name": "John Doe",
        "department": "Engineering",
        "position": "Software Engineer",
        "salary": 70000.0
    }

    # First add the employee
    client.post("/employeeData", json=employee_data)
    
    # Try adding the same employee again
    response = client.post("/employeeData", json=employee_data)
    
    assert response.status_code == 400
    assert response.json() == {"detail": "Employee with the given employee_id already exists"}

    # Ensure only one entry in the list of employees 
    assert len(employees) == 1

# Test error handling for PUT: Updating a non-existing employee's data
def test_update_employee_not_exist():
    updated_employee = {
        "id": 2,
        "name": "John Smith",
        "department": "Engineering",
        "position": "Senior Software Engineer",
        "salary": 80000.0
    }

    response = client.put("/employeeData/2", json=updated_employee)

    assert response.status_code == 404
    assert response.json() == {"detail": "Employee with the given employee_id not found"}

    # Ensure only one entry in the list of employees (from previous test)
    assert len(employees) == 1
    assert employees[0].salary == 70000.0
    assert employees[0].id == 1

# Test error handling for PUT: Updating a employee's employee_id
def test_update_employee_id():
    updated_employee = {
        "id": 2,
        "name": "John Smith",
        "department": "Engineering",
        "position": "Senior Software Engineer",
        "salary": 80000.0
    }

    response = client.put("/employeeData/1", json=updated_employee)

    assert response.status_code == 400
    assert response.json() == {"detail": "Employee_id cannot be changed"}

    # Ensure only one entry in the list of employees (from previous test)
    assert len(employees) == 1
    assert employees[0].id == 1
    assert employees[0].salary == 70000.0

# Test error handling for PATCH: Updating specific fields of an non-existing employee
def test_update_specific_employee_not_exist():
    updated_fields = {
        "salary": 95000.0
    }

    response = client.patch("/employeeData/2", json=updated_fields)

    assert response.status_code == 404
    assert response.json() == {"detail": "Employee with the given employee_id not found"}

    # Verify the salary update did not occur
    assert employees[0].salary == 70000.0

# Test error handling for DELETE: Delete an non-existing employee by ID
def test_delete_employee_not_exist():
    response = client.delete("/employeeData/2")

    assert response.status_code == 404
    assert response.json() == {"detail": "Employee with the given employee_id not found"}

    # Verify that the employee list has 1 employee
    assert len(employees) == 1



# Tests to ensure that Default Values are not being stored
# Test Default Values for POST: Input employee with all default values
def test_add_employee_all_default():
    employee_data = {
        "id": 0,
        "name": "string",
        "department": "string",
        "position": "string",
        "salary": 0
    }
    
    # Try adding the employee with default values
    response = client.post("/employeeData", json=employee_data)
    
    assert response.status_code == 400
    assert response.json() == {"detail": "Employee data cannot have default values"}

    # Ensure only one entry in the list of employees 
    assert len(employees) == 1
    assert employees[0].id != 0

# Test Default Values for POST: Input employee with some default values
def test_add_employee_partial_default():
    employee_data = {
        "id": 1,
        "name": "Sam",
        "department": "string",
        "position": "string",
        "salary": 0
    }
    
    # Try adding the employee with default values
    response = client.post("/employeeData", json=employee_data)
    
    assert response.status_code == 400
    assert response.json() == {"detail": "Employee data cannot have default values"}

    # Ensure only one entry in the list of employees 
    assert len(employees) == 1
    assert employees[0].id != 0

# Test Default Values for PUT: Input employee with some default values
def test_update_employee_default():
    updated_employee = {
        "id": 1,
        "name": "string",
        "department": "string",
        "position": "Senior Software Engineer",
        "salary": 80000.0
    }

    response = client.put("/employeeData/1", json=updated_employee)

    assert response.status_code == 400
    assert response.json() == {"detail": "Employee data cannot have default values"}

    # Ensure only one entry in the list of employees (from previous test)
    assert len(employees) == 1
    assert employees[0].id == 1
    assert employees[0].name == "John Doe"
    assert employees[0].salary == 70000.0

# Test default values for PATCH: Input employee with some default values
def test_update_specific_default():
    updated_fields = {
        "salary": 0
    }

    response = client.patch("/employeeData/1", json=updated_fields)

    assert response.status_code == 400
    assert response.json() == {"detail": "Employee data cannot have default values"}

    # Verify the salary update did not occur
    assert employees[0].salary == 70000.0
