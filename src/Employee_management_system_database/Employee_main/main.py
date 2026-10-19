import Employee_manager.employee_manager as emp
from Employee_Repository.database_employee_repository import DatabaseEmployeeRepository
from Employee_Repository.json_employee_repository import JsonEmployeeRepository
from Employee_Repository.logging import logger

class Main:

    def create_repository(self):

        storage_type = input(
            "Choose storage (json/database): "
        ).lower()

        if storage_type == "json":
            return JsonEmployeeRepository()

        elif storage_type == "database":
            return DatabaseEmployeeRepository()

        else:
            raise ValueError("Invalid storage type")

    def main(self):
        repository = self.create_repository()
        manager = emp.Manager(repository)
        print("")
        print("=======================================")
        print("Welcome to Employee Management System")
        print("=======================================")
        print("")
        print("choose an option for using Employee Management System")
        logger.info("Application is started...")
    
        while True:
            try :
                print("1. Add Employee")
                print("2. Update Employee")
                print("3. Search Employee")
                print("4. Display All Employee")
                print("5. Delete Employee")
                print("6. Exit\n")
                case = int(input("Enter Option :- "))
                print(" ")
                if case == 1:
                    manager.add_employee()
                elif case == 2:
                    manager.update_employee()
                elif case == 3:
                    manager.search_employee()
                elif case == 4:
                    manager.display_employee()
                elif case == 5:
                    manager.delete_employee()
                elif case == 6:
                    print("Exit")
                    logger.info("Application is off...")
                    break
                else :
                    print("please select a valid option")
            except ValueError:
                print("please enter a valid number")


main = Main()
main.main()