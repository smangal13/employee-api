from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()

class Employee(BaseModel):
    id: int
    name: str
    department: str
    position: str
    salary: float

class EmployeeResponse(BaseModel):
    message: str
    employee: Employee

class UpdateEmployee(BaseModel):
    name: Optional[str] = None
    department: Optional[str] = None
    position: Optional[str] = None
    salary: Optional[float] = None
employees = []

#To add employee data
@app.post("/employeeData", response_model = EmployeeResponse)
def add_employee_data(employee: Employee):
    for emp in employees:
        if emp.id == employee.id:
            raise HTTPException(status_code=400, detail="Employee with the given employee_id already exists")
    employees.append(employee)
    return {"message": "Employee Data Successfully stored!", "employee": employee}

#To get all the employees and their data
@app.get("/employeeData", response_model = List[Employee])
def get_all_employees():
    return employees

#To get a particular Employee from its id
@app.get("/employeeData/{employee_id}", response_model = Employee)
def get_employee_from_id(employee_id: int):
    for employee in employees:
        if employee.id == employee_id:
            return employee
    raise HTTPException(status_code=404, detail="Employee with the given employee_id not found")

#Update Employee details: Cannot change the Employee Id
@app.put("/employeeData/{employee_id}", response_model = EmployeeResponse)
def update_employee_data(employee_id: int, employee:Employee):
    for index, emp in enumerate(employees):
        if emp.id == employee_id:
            if employee.id != emp.id:
                raise HTTPException(status_code=400, detail="Employee_id cannot be changed")
            employees[index] = employee
            return {"message": "Employee data Successfully Updated","employee":employees[index]}
    raise HTTPException(status_code=404, detail="Employee with the given employee_id not found")

#Update Specific Employee Details: Cannot change the Employee id
@app.patch("/employeeData/{employee_id}", response_model = EmployeeResponse)
def update_specific_employee_data(employee_id: int, employee:UpdateEmployee):
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

#Delete Employee details
@app.delete("/employeeData/{employee_id}")
def delete_employee_data(employee_id: int):
    for index, emp in enumerate(employees):
        if emp.id == employee_id:
            del employees[index]
            return {"message": "Employee data Successfully Deleted"}
    raise HTTPException(status_code=404, detail="Employee with the given employee_id not found")


''' Questions
Should Employee id be changed?
Should we check for default values as input?
'''
