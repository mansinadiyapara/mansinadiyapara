from Employee_Repository.logging import logger
from Employee_validation.validation import (
    validate_employee_id,
    validate_employee_name,
    validate_employee_email,
    validate_employee_department,
    validate_employee_salary
)

class Manager:

    def __init__(self, repository):
        self.repository = repository

    def add_employee(self):
        employees = self.repository.get_all()
        print("\nAdd Employee Data.....")
        logger.debug("add_employee function called...")

        emp_id = validate_employee_id(employees)
        emp_name = validate_employee_name() 
        emp_email = validate_employee_email() 
        emp_department = validate_employee_department() 
        emp_salary = validate_employee_salary()

        employee = {
            "id": emp_id,
            "name": emp_name,
            "email": emp_email,
            "department": emp_department,
            "salary": emp_salary
        }
        self.repository.add(employee)
        print("Employee Data Added Successfully.....")
        logger.debug("Employee Data Added Successfully.....")

    def update_employee(self):
        employees = self.repository.get_all()
        logger.debug("update_employee function called...")
        if not employees:
            print("No Employee Data Found. Add Data First.")
        else:
            while True:
                try:
                    emp_id = int(input("Enter Employee ID For Update Employee Data:- "))
                    employee = None

                    for emp in employees:
                        if emp["id"] == emp_id:
                            employee = emp
                            break

                    if employee is None:
                        print("This Employee Id Does Not Exist")
                        return
                  
                    emp_name = validate_employee_name() 
                    emp_email = validate_employee_email() 
                    emp_department = validate_employee_department() 
                    emp_salary = validate_employee_salary()
                        
                    employee = {
                        "id": emp_id,
                        "name": emp_name,
                        "email": emp_email,
                        "department": emp_department,
                        "salary": emp_salary
                    }
                    self.repository.update(employee)
                    print("Employee Data Updated Successfully.....")
                    logger.debug("Employee Data Updated Successfully.....")
                    break
                except ValueError:
                    print("Please enter a valid integer ID")

    def search_employee(self):
        employees = self.repository.get_all()
        logger.debug("search_employee function called...")
        if not employees:
            print("Add Employee Data First")
        else:
            while True:
                try:
                    emp_id = int(input("Enter Employee ID For Search Employee:- "))
                    employee = None

                    for emp in employees:
                        if emp["id"] == emp_id:
                            employee = emp
                            break

                    if employee is not None:

                        print("\n--- Employee Details ---")

                        for key, value in employee.items():
                            print(f"{key.capitalize()}: {value}")

                        logger.debug("Search employee details displayed")
                        break

                    else:
                        print("This Employee ID Does Not Exist")

                except ValueError:
                    print("Please enter a valid integer ID") 
            
    def display_employee(self):
        employees = self.repository.get_all()
        logger.debug("display_employee function called...")
        if not employees:
            print("Add Employee Data First")
        else:
            print("Display All Employee.....")
            logger.debug("Display All Employee.....")
            print(employees)

    def delete_employee(self):
        employees = self.repository.get_all()
        logger.debug("delete_employee function called...")
        if not employees:
            print("Add Employee Data First")
        else:
            while True:
                try:
                    emp_id = int(
                        input("Enter Employee ID For Delete Employee:- ")
                    )

                    employee = None

                    for emp in employees:
                        if int(emp["id"]) == emp_id:
                            employee = emp
                            break

                    if employee is not None:

                        self.repository.delete(emp_id)

                        print("Employee Data Deleted Successfully")
                        logger.debug("Employee Data Deleted Successfully")

                        break

                    else:
                        print("This Employee ID Does Not Exist")

                except ValueError:
                    print("Please enter a valid integer ID")         

