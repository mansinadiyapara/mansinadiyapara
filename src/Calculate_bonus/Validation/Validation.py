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


def validate_employee_performance():
    """Get and validate employee performance."""

    performances = [
        "1/5 Rating",
        "2/5 Rating",
        "3/5 Rating",
        "4/5 Rating",
        "5/5 Rating"
    ]

    while True:
        print("\nSelect Employee Performance:")

        for i, performance in enumerate(performances, start=1):
            print(f"{i}. {performance}")

        try:
            choice = int(input("Enter your choice: "))

            if 1 <= choice <= len(performances):
                return performances[choice - 1]

            print("Please select a valid performance.")

        except ValueError:
            print("Please enter a number.")


def validate_employee_experience():
    """Get and validate employee experience."""

    while True:
        try:
            emp_experience = int(input("Enter Employee Experience:- "))

            if emp_experience <= 0:
                print("Salary must be greater than 0.")
            else:
                return emp_experience

        except ValueError:
            print("Please enter a valid integer number")


def validate_employee_department():
    """Get and validate employee department."""

    departments = [
        "IT",
        "HR",
        "Finance",
        "Marketing",
        "Sales"
    ]

    while True:
        print("\nSelect Employee Department:")

        for i, department in enumerate(departments, start=1):
            print(f"{i}. {department}")

        try:
            choice = int(input("Enter your choice: "))

            if 1 <= choice <= len(departments):
                return departments[choice - 1]

            print("Please select a valid department.")

        except ValueError:
            print("Please enter a number.")


