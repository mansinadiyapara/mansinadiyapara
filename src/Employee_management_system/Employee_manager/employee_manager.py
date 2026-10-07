from Employee_Repository.load_save_data import load_data, save_data
from Employee_Repository.logging import logger
from Employee_validation.validation import (
    validate_employee_id,
    validate_employee_name,
    validate_employee_email,
    validate_employee_department,
    validate_employee_salary
)

class Manager:

    def add_employee(self):
        employees = load_data()
        print("\nAdd Employee Data.....")
        logger.debug("add_employee function called...")

        emp_id = validate_employee_id(employees)
        emp_name = validate_employee_name() 
        emp_email = validate_employee_email() 
        emp_department = validate_employee_department() 
        emp_salary = validate_employee_salary()

        employees[str(emp_id)] = {
            "id": emp_id,
            "name": emp_name,
            "email": emp_email,
            "department": emp_department,
            "salary": emp_salary
        }
        save_data(employees)
        print("Employee Data Added Successfully.....")
        logger.debug("Employee Data Added Successfully.....")

    def update_employee(self):
        employees = load_data()
        logger.debug("update_employee function called...")
        if not employees:
            print("No Employee Data Found. Add Data First.")
        else:
            while True:
                try:
                    emp_id = int(input("Enter Employee ID For Update Employee Data:- "))
                    if str(emp_id) in employees:
                        
                        emp_name = validate_employee_name() 
                        emp_email = validate_employee_email() 
                        emp_department = validate_employee_department() 
                        emp_salary = validate_employee_salary()
                        
                        employees[str(emp_id)] = {
                            "id": emp_id,
                            "name": emp_name,
                            "email": emp_email,
                            "department": emp_department,
                            "salary": emp_salary
                        }
                        save_data(employees)
                        print("Employee Data Updated Successfully.....")
                        logger.debug("Employee Data Updated Successfully.....")
                        break
                    else:
                        print("This Employee Id Does Not Exits")
                except ValueError:
                    print("Please enter a valid integer ID")

    def search_employee(self):
        employees = load_data()
        logger.debug("search_employee function called...")
        if not employees:
            print("Add Employee Data First")
        else:
            while True:
                try:
                    emp_id = int(input("Enter Employee ID For Search Employee:- "))
                    if str(emp_id) in employees:
                        print("\n--- Employee Details ---")
                        for key, value in employees[str(emp_id)].items():
                            print(f"{key.capitalize()}: {value}")
                        logger.debug("search_employee display...")
                        break
                    else:
                        print("This Employee Id Does Not Exits")
                except ValueError:
                    print("Please enter a valid integer ID") 
            
    def display_employee(self):
        employees = load_data()
        logger.debug("display_employee function called...")
        if not employees:
            print("Add Employee Data First")
        else:
            print("Display All Employee.....")
            logger.debug("Display All Employee.....")
            print(employees)

    def delete_employee(self):
        employees = load_data()
        logger.debug("delete_employee function called...")
        if not employees:
            print("Add Employee Data First")
        else:
            while True:
                try:
                    emp_id = int(input("Enter Employee ID For Delete Employee:- "))
                    if str(emp_id) in employees:
                        del employees[str(emp_id)]
                        save_data(employees)
                        print("Employee Data Deleted Successfully")
                        logger.debug("Employee Data Deleted Successfully")
                        break
                    else:
                        print("This Employee Id Does Not Exits")
                except ValueError:
                    print("Please enter a valid integer ID")            

