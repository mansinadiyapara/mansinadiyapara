from Repository.LoadSaveData import load_data, save_data
from Validation.Validation import (
    validate_employee_id,
    validate_employee_name,
    validate_employee_salary,
    validate_employee_performance,
    validate_employee_experience,
    validate_employee_department,
)
from Rules.DepartmentRule import DepartmentRule
from Rules.ExperienceRule import ExperienceRule
from Rules.PerformanceRule import PerformanceRule

class Main:

    def run(self):

        print("===== Bonus Calculator =====")

        employees = load_data()

        emp_id = validate_employee_id(employees)
        emp_name = validate_employee_name() 
        emp_salary = validate_employee_salary()
        emp_performance = validate_employee_performance()
        emp_experience = validate_employee_experience()
        emp_department = validate_employee_department() 

        employees[str(emp_id)] = {
            "id": emp_id,
            "name": emp_name,
            "salary": emp_salary,
            "performance": emp_performance,
            "experience": emp_experience,
            "department": emp_department,
            
        }
        save_data(employees)

        while True:

            print("\nSelect Bonus Rule...")
            print("1.Department Rule")
            print("2.Experience Rule")
            print("3.Performance Rule")
            print("4.Exit")

            try:
                case = int(input("Enter Your Choice:- "))

            except ValueError:
                print("Please enter a valid number")
                continue

            if case == 1:
                department_rule = DepartmentRule()
                department_rule.calculate_bonus()
            elif case == 2:
                experience_rule = ExperienceRule()
                experience_rule.calculate_bonus()
            elif case == 3:
                performance_rule = PerformanceRule()
                performance_rule.calculate_bonus()
            elif case == 4:
                print("Exit")
                break
            else :
                print("please select a valid choice")


main = Main()
main.run()