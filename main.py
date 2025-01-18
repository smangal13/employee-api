from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()

# Defining the Employee model, which represents the structure of employee data.
class Employee(BaseModel):
    id: int
    name: str
    department: str
    position: str
    salary: float

# Defining the response model for adding/updating employee data.
class EmployeeResponse(BaseModel):
    message: str
    employee: Employee

# Defining the model for updating specific fields of an employee.
class UpdateEmployee(BaseModel):
    name: Optional[str] = None
    department: Optional[str] = None
    position: Optional[str] = None
    salary: Optional[float] = None

# Default employee values to check against invalid data.
default_employee = {
  "id": 0,
  "name": "string",
  "department": "string",
  "position": "string",
  "salary": 0
}

default_employee_specific = {
  "name": "string",
  "department": "string",
  "position": "string",
  "salary": 0
}

# List to store employee data in memory.
employees = []

# Helper function to check if any field in the input matches the default employee values.
def is_default_employee(employee: Employee, default_employee: dict) -> bool:
    employee_dict = employee.__dict__
    
    return any(employee_dict[field] == default_employee[field] for field in employee_dict)


# Endpoint to add employee data
@app.post("/employeeData", response_model = EmployeeResponse)
def add_employee_data(employee: Employee):
    """
    Add a new employee to the in-memory list.

    - Parameters:
        - employee: Employee object containing employee details.
    - Returns:
        - A success message and the added employee data.
    - Raises:
        - HTTP 400 if employee has default values or if the ID already exists.
    """
    if is_default_employee(employee, default_employee):
        raise HTTPException(status_code=400, detail="Employee data cannot have default values")

    for emp in employees:
        if emp.id == employee.id:
            raise HTTPException(status_code=400, detail="Employee with the given employee_id already exists")

    employees.append(employee)
    return {"message": "Employee Data Successfully stored!", "employee": employee}

# Endpoint to retrieve all employees and their data
@app.get("/employeeData", response_model = List[Employee])
def get_all_employees():
    """
    Retrieve a list of all employees.

    - Returns:
        - A list of Employee objects.
    """
    return employees

# Endpoint to retrieve a specific employee by ID.
@app.get("/employeeData/{employee_id}", response_model = Employee)
def get_employee_from_id(employee_id: int):
    """
    Retrieve details of a specific employee by their ID.

    - Parameters:
        - employee_id: ID of the employee to retrieve.
    - Returns:
        - The Employee object matching the given ID.
    - Raises:
        - HTTP 404 if the employee is not found.
    """
    for employee in employees:
        if employee.id == employee_id:
            return employee
    raise HTTPException(status_code=404, detail="Employee with the given employee_id not found")

# Endpoint to update all details of an employee (except ID).
@app.put("/employeeData/{employee_id}", response_model = EmployeeResponse)
def update_employee_data(employee_id: int, employee:Employee):
    """
    Update all details of an existing employee.

    - Parameters:
        - employee_id: ID of the employee to update.
        - employee: Employee object containing updated details.
    - Returns:
        - A success message and the updated employee data.
    - Raises:
        - HTTP 400 if default values are provided or if the ID is being changed.
        - HTTP 404 if the employee is not found.
    """
    if is_default_employee(employee, default_employee):
        raise HTTPException(status_code=400, detail="Employee data cannot have default values")
    
    for index, emp in enumerate(employees):
        if emp.id == employee_id:
            if employee.id != emp.id:
                raise HTTPException(status_code=400, detail="Employee_id cannot be changed")
            employees[index] = employee
            return {"message": "Employee data Successfully Updated","employee":employees[index]}
    raise HTTPException(status_code=404, detail="Employee with the given employee_id not found")

# Endpoint to update specific details of an employee (except ID).
@app.patch("/employeeData/{employee_id}", response_model = EmployeeResponse)
def update_specific_employee_data(employee_id: int, employee:UpdateEmployee):
    """
    Update specific details of an existing employee.

    - Parameters:
        - employee_id: ID of the employee to update.
        - employee: UpdateEmployee object containing updated fields.
    - Returns:
        - A success message and the updated employee data.
    - Raises:
        - HTTP 400 if default values are provided.
        - HTTP 404 if the employee is not found.
    """
    if is_default_employee(employee, default_employee_specific):
        raise HTTPException(status_code=400, detail="Employee data cannot have default values")
    
    for index, emp in enumerate(employees):
        if emp.id == employee_id:
            if employee.name is not None:
                employees[index].name = employee.name
            if employee.department is not None:
                employees[index].department = employee.department
            if employee.position is not None:
                employees[index].position = employee.position
            if employee.salary is not None:
                employees[index].salary = employee.salary
            return {"message": "Employee data Successfully Updated","employee":employees[index]}
    raise HTTPException(status_code=404, detail="Employee with the given employee_id not found")

# Endpoint to delete an employee by ID.
@app.delete("/employeeData/{employee_id}")
def delete_employee_data(employee_id: int):
    """
    Delete an employee from the in-memory list.

    - Parameters:
        - employee_id: ID of the employee to delete.
    - Returns:
        - A success message if the employee is deleted.
    - Raises:
        - HTTP 404 if the employee is not found.
    """
    for index, emp in enumerate(employees):
        if emp.id == employee_id:
            del employees[index]
            return {"message": "Employee data Successfully Deleted"}
    raise HTTPException(status_code=404, detail="Employee with the given employee_id not found")
