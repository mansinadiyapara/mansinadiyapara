from Employee_Repository.load_save_data import load_data

class EmployeeAnalyzer:

    def salary_analyzer(self):
        employees = load_data()
        if not employees:
            print("Add Data First...")
        else:
            salaries = []

            for emp_key, emp_details in employees.items():
                salary = emp_details["salary"]
                salaries.append(salary)

            average_salary = sum(salaries) / len(salaries)

            print("Salaries:", salaries)
            print("Minimum Salary:", min(salaries))
            print("Maximum Salary:", max(salaries))
            print("average salary:",average_salary)

    def sorting_data(self):
        employees = load_data()
        if not employees:
            print("Add Data First.....")
        else:
            names = []
            for emp_key, emp_details in employees.items():
                emp_name = emp_details["name"]
                names.append(emp_name)

            print("befor sorting by name",names)
            for i in range(len(names)):
                for j in range(i+1,len(names)):
                    if names[i] > names[j]:
                        temp = names[i]
                        names[i] = names[j]
                        names[j] = temp
            print("after sorting by name",names)

    def search_data(self):
        employees = load_data()
        if not employees:
            print("Add Data First.....")
        else:
            while True:
                    try:
                        print("Choose an option for searching")
                        print("1. Search by Id...")
                        print("2. Search by Name...")
                        print("3. Search by Department...")
                        print("4. Exit")
                        case = int(input("Enter Option :- "))

                        if case == 1:
                            search_id = int(input("Enter Search Id :- "))

                            found = False

                            for emp_key, emp_details in employees.items():

                                if emp_details["id"] == search_id:
                                    print("ID:", emp_details["id"])
                                    print("Name:", emp_details["name"])
                                    print("Department:", emp_details["department"])
                                    print("Salary:", emp_details["salary"])

                                    found = True
                                    break

                            if not found:
                                print("This ID Doesn't Exist")

                        elif case == 2:
                            search_name = input("Enter Search Name :- ")
                            
                            found = False

                            for emp_key, emp_details in employees.items():

                                if emp_details["name"] == search_name:
                                    print("ID:", emp_details["id"])
                                    print("Name:", emp_details["name"])
                                    print("Department:", emp_details["department"])
                                    print("Salary:", emp_details["salary"])

                                    found = True
                                    break

                            if not found:
                                print("This Name Doesn't Exist")
                        elif case == 3:
                            search_department = input("Enter Search Department :- ")
                            
                            found = False

                            for emp_key, emp_details in employees.items():

                                if emp_details["department"] == search_department:
                                    print("ID:", emp_details["id"])
                                    print("Name:", emp_details["name"])
                                    print("Department:", emp_details["department"])
                                    print("Salary:", emp_details["salary"])

                                    found = True
                                    break

                            if not found:
                                print("This Department Doesn't Exist")
                        elif case == 4:
                            print("Exit")
                            break
                        else:
                            print("please enter correct option")
                    except ValueError:
                        print("Invalid number selected")
                        
    def invalid_data(self):
        employees = load_data()
        if not employees:
            print("Add Data First...")
        else:
            for emp_key, emp_details in employees.items():
                if emp_details["salary"] < 0:
                    print(emp_details["salary"],": This salary is not valid and this is id :",emp_details["id"],"salary")
                
# object created
analyzer = EmployeeAnalyzer()

# method called
analyzer.salary_analyzer()
analyzer.sorting_data()
analyzer.search_data()
analyzer.invalid_data()