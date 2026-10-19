
def validate_employee_id(employees):
    """Get and validate a unique employee ID."""

    while True:
        try:
            emp_id = int(input("Enter Employee ID:- "))

            if str(emp_id) in employees:
                print("Enter Unique ID. This ID Already Exists.")
            else:
                return str(emp_id)

        except ValueError:
            print("Please enter a valid integer ID")


def validate_employee_name():
    """Get and validate employee name."""

    while True:
        emp_name = input("Enter Employee Name:- ")

        if emp_name.replace(" ", "").isalpha():
            return emp_name
        else:
            print("Please enter a valid name")


def validate_employee_email():
    """Get and validate employee email."""

    while True:
        emp_email = input("Enter Employee Email:- ")

        if "@" not in emp_email or "." not in emp_email:
            print("Please enter a valid email address")
        else:
            return emp_email


def validate_employee_department():
    """Get and validate employee department."""

    while True:
        emp_department = input("Enter Employee Department:- ")

        if emp_department.replace(" ", "").isalpha():
            return emp_department
        else:
            print("Please enter a valid department name")


def validate_employee_salary():
    """Get and validate employee salary."""

    while True:
        try:
            emp_salary = int(input("Enter Employee Salary:- "))

            if emp_salary <= 0:
                print("Salary must be greater than 0.")
            else:
                return emp_salary

        except ValueError:
            print("Please enter a valid integer number")

