
# Project Title

A brief description of what this project does and who it's for

# Employee Management System - Design Document

## 1. Problem Understanding

The Employee Management System is a small command-line application for managing employee records.

The application will allow the user to:

* Add a new employee
* Update employee details
* Delete an employee
* Search for an employee
* Display all employees
* Exit the application

The application will initially store employee data in memory. The main purpose of the system is to provide a simple and organized way to manage employee information through the command line.

The application will be divided into multiple Python files instead of putting all the code into one large file.

---

## 2. Assumptions

The following assumptions are made for the application:

* Each employee has a unique Employee ID.
* Employee ID is used to identify an employee.
* An employee has an ID, name, email, department, and salary.
* Employee data will initially be stored in memory.
* Data will not be permanently saved after the application is closed.
* The application will run through the command line.
* The user will select operations from a menu.
* Invalid input should not crash the application.
* After an error, the user should be able to return to the menu and try again.

---

## 3. Employee Data Structure

Each employee will contain the following information:

| Field       | Description                       |
| ----------- | --------------------------------- |
| Employee ID | Unique identifier of the employee |
| Name        | Employee's name                   |
| Email       | Employee's email address          |
| Department  | Employee's department             |
| Salary      | Employee's salary                 |

An `Employee` class will be used to represent an employee.

The Employee class will be kept separately in `employee.py`.

The employee management operations will be handled separately in `employee_manager.py`.

---

## 4. Data Storage Approach

Initially, employee records will be stored in memory.

A dictionary can be used to store the employees because Employee ID needs to be unique and can be used as the key.

Conceptually:

```text
Employee ID → Employee Object

E001 → Employee
E002 → Employee
E003 → Employee
```

This makes it easier to find an employee using their Employee ID.

The data will only exist while the application is running. Permanent storage such as a database or file is not required for the initial version.

---

## 5. Program Flow

The application will start by displaying the main menu.

```text
Start
  ↓
Display Main Menu
  ↓
User selects an operation
  ↓
Validate the input
  ↓
Perform selected operation
  ↓
Display result or error message
  ↓
Return to Main Menu
  ↓
Exit when user selects Exit
```

Example menu:

```text
===== Employee Management System =====

1. Add Employee
2. Update Employee
3. Delete Employee
4. Search Employee
5. Display All Employees
6. Exit

Enter your choice:
```

The application should continue displaying the menu until the user chooses the Exit option.

---

## 6. Application Operations

### Add Employee

The user provides employee details such as Employee ID, name, email, department, and salary.

Before adding the employee, the system will validate the input and check whether the Employee ID already exists.

If the ID is unique and the data is valid, the employee will be added.

### Update Employee

The user provides an existing Employee ID.

If the employee exists, the system will allow the employee details to be updated.

If the employee does not exist, an appropriate error message will be displayed.

### Delete Employee

The user provides an Employee ID.

If the employee exists, the employee record will be removed.

If the employee does not exist, the system will display an appropriate message.

### Search Employee

The user provides an Employee ID.

The system will search for the employee using the ID.

If the employee is found, the employee details will be displayed.

If the employee is not found, an error message will be displayed.

### Display All Employees

The system will display all employees currently stored in memory.

The employee details can be displayed in a structured table format.

### Exit

The application will stop when the user selects the Exit option.

---

## 7. Validation Rules

Input validation will be performed before processing employee data.

### Employee ID

* Employee ID is required.
* Employee ID must be unique when adding an employee.
* An existing Employee ID must be provided for update, delete, or search operations.

### Name

* Name is required.
* Name should not be empty.

### Email

* Email is required.
* Email should follow a valid email format.

### Department

* Department is required.
* Department should not be empty.

### Salary

* Salary is required.
* Salary must be a valid numeric value.
* Salary should not be negative.

### Menu Choice

* The user must select a valid menu option.
* Invalid menu choices should display an error message and allow the user to try again.

---

## 8. Error Handling

The application should handle invalid input without crashing.

Examples of errors include:

* Duplicate Employee ID
* Employee not found
* Empty employee name
* Invalid email
* Invalid salary
* Negative salary
* Invalid menu choice
* Non-numeric input where a number is expected

When an error occurs, the system should display a clear message to the user.

Example:

```text
Employee not found.

Please try again.
```

The application should continue running after an error and return the user to the appropriate menu or allow them to enter the information again.

The goal is to make the application user-friendly and prevent unexpected termination because of invalid input.

## 9. Possible Edge Cases

The application should handle unusual or unexpected situations properly.

* User tries to add an employee with an existing Employee ID.
* User tries to update an employee that does not exist.
* User tries to delete an employee that does not exist.
* User searches for an Employee ID that is not available.
* User enters an empty employee name.
* User enters an invalid email address.
* User enters a negative salary.
* User enters text instead of a numeric salary.
* User selects an invalid menu option.
* User tries to display employees when there are no employees.
* User enters empty input where a value is required.

The application should display a clear error message and allow the user to continue using the application.

## 10. Chosen Approach

The application will use Python classes and a dictionary for storing employee records in memory.

An `Employee` class will represent each employee and contain employee details such as Employee ID, name, email, department, and salary.

The `EmployeeManager` class will handle operations such as:

* Add Employee
* Update Employee
* Delete Employee
* Search Employee
* Display All Employees

The dictionary will use the Employee ID as the key and the Employee object as the value.

This approach keeps the employee data structure and business operations separate from the user interface.

## 11. Alternative Approaches Considered

### List of Dictionaries

A list of dictionaries could be used to store employee information.

Example:

```text
[
    {
        "id": "E001",
        "name": "Mansi",
        "email": "mansi@example.com"
    }
]
```

However, searching and updating employees would require checking each employee one by one.

### Dictionary of Dictionaries

A dictionary could store employee details as another dictionary.

Example:

```text
{
    "E001": {
        "name": "Mansi",
        "email": "mansi@example.com"
    }
}
```

This provides quick access using the Employee ID, but it does not represent an employee as an object.

### Database

A database such as SQLite could be used to permanently store employee records.

However, the current requirement is to keep the data in memory, so a database is not required at this stage.

## 12. Why the Selected Approach Was Chosen

The class-based approach with a dictionary was selected because it is simple and suitable for a small command-line application.

The Employee class provides a clear structure for employee data, while the EmployeeManager class keeps the application operations organized.

Using Employee ID as the dictionary key makes searching, updating, and deleting employees straightforward.

The approach also keeps the application divided into separate files, making the code easier to understand, test, and maintain.

