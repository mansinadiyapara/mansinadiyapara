# OOP Design — Employee Management System

## 1. Identified Entities

The Employee Management System works with employee information and provides operations such as adding, updating, deleting, searching, displaying, and storing employee data.

After analyzing the requirements, the following main entities and components were identified:

### EmployeeMain 

An `EmployeeMain` represents one employee in the system.

The employee contains information such as:

* Employee ID
* Name
* Email
* Department
* Salary

The `EmployeeMain` object is responsible for representing and holding employee-specific information.

### EmployeeManager

`EmployeeManager` is responsible for managing employee records.

It coordinates operations such as:

* Adding an employee
* Updating an employee
* Deleting an employee
* Searching for employees
* Displaying employee information

The manager works with `Employee` objects rather than storing all employee-related behavior in the `Employee` class.

### EmployeeRepository

`EmployeeRepository` is responsible for employee data storage and retrieval.

Its responsibilities may include:

* Loading employee data
* Saving employee data
* Reading data from the JSON file
* Writing updated data to the JSON file

The repository separates storage-related logic from employee management logic.

---

## 2. Responsibilities

Each class should have a clear responsibility.

### EmployeeMain Responsibilities

The `EmployeeMain` class is responsible for representing one employee and storing employee-specific data.

It should not be responsible for:

* Reading JSON files
* Writing JSON files
* Displaying the application menu
* Managing all employees
* Handling user input

The object represents the employee and owns the employee-specific values.

### EmployeeManager Responsibilities

The `EmployeeManager` is responsible for coordinating employee operations.

Examples:

```text
add
update
delete
search
display
```

It can communicate with the validator before changing data and with the repository when employee data needs to be stored.

### EmployeeRepository Responsibilities

The repository manages persistence.

For example:

```text
EmployeeManager
       ↓
EmployeeRepository
       ↓
employee_data.json
```

This means the manager does not need to know the detailed JSON file-handling code.

---

## 3. Relationships

The classes have different relationships with each other.

### EmployeeManager and Employee

`EmployeeManager` works with multiple `Employee` objects.

```text
EmployeeManager
      |
      | manages
      ↓
 Employee objects
```

The manager performs operations on employee records.

### EmployeeManager and EmployeeRepository

The manager uses the repository to save and load employee information.

```text
EmployeeManager
      |
      | uses
      ↓
EmployeeRepository
      |
      ↓
employee_data.json
```

This creates a separation between business operations and storage.

## 4. Proposed Class Design

The proposed design contains the following classes:

```text
EmployeeMain
EmployeeManager
EmployeeRepository
```

### Employee

```python
class EmployeeMain:
    call the method of EmployeeManager
```

The purpose of this class is to represent a single employee.

### EmployeeManager

```python
class EmployeeManager:

    def add_employee(self, employee):
        pass

    def update_employee(self, employee_id):
        pass

    def delete_employee(self, employee_id):
        pass

    def search_employee(self, value):
        pass

    def display_employee(self):
        pass
```

The manager controls employee-related operations.

### EmployeeRepository

```python
class EmployeeRepository:

    def load_data(self):
        pass

    def save_data(self, data):
        pass
```

The repository handles persistence.

---

## 5. Expected Interactions

The classes should communicate through clearly defined responsibilities.

### Adding an Employee

The expected flow is:

```text
User
 ↓
main.py
 ↓
EmployeeManager
 ↓
Employee
 ↓
EmployeeRepository
 ↓
employee_data.json
```

Example process:

1. The user enters employee information.
2. `main.py` passes the information to the manager.
3. The manager creates or receives an `Employee` object.
4. If the data is valid, the manager asks `EmployeeRepository` to save it.
5. The repository writes the data to `employee_data.json`.

### Loading Employees

```text
main.py
   ↓
EmployeeManager
   ↓
EmployeeRepository
   ↓
employee_data.json
```

The repository reads the JSON data and returns Python data to the manager.

### Updating an Employee

```text
User
 ↓
EmployeeManager
 ↓
Find Employee
 ↓
EmployeeRepository
 ↓
employee_data.json
```

The manager identifies the employee, validates updated data, and asks the repository to save the changes.

### Deleting an Employee

```text
User
 ↓
EmployeeManager
 ↓
Find Employee
 ↓
Remove Employee
 ↓
EmployeeRepository
 ↓
employee_data.json
```

---

## 6. Alternative Designs

Several different designs were considered.

### Alternative 1 — One Large Employee Class

One possible approach is to place everything into one class:

```python
class Employee:
    def add_employee(self):
        pass

    def update_employee(self):
        pass

    def delete_employee(self):
        pass

    def validate_employee(self):
        pass

    def load_data(self):
        pass

    def save_data(self):
        pass
```

This design is simple for a very small program, but the class would have too many responsibilities.

It would contain:

* Employee data
* Employee management
* Validation
* File handling

This increases coupling and makes the class harder to maintain and test.

### Alternative 2 — Employee + EmployeeManager

Another design is:

```text
Employee
EmployeeManager
```

The manager handles validation and file handling internally.

This is simpler than the proposed design and may be suitable for a very small application.

However, as the project grows, `EmployeeManager` can become too large because it would handle:

* Business operations
* Validation
* Storage

### Alternative 3 — Separate Responsibilities

The selected design separates:

```text
Employee
EmployeeManager
EmployeeValidator
EmployeeRepository
```

Each component has a more focused responsibility.

---

## 7. Design Decision

The selected design is:

```text
EmployeeMain
EmployeeManager
EmployeeRepository
```

The decision was made because the application contains different types of work that should not all be handled by one class.

The `Employee` class represents employee information.

The `EmployeeManager` coordinates employee operations.

The `EmployeeRepository` handles reading and writing employee data.

This design provides clearer boundaries between the different parts of the application.

---

## 8. Database Responsibility

An important design question is:

> Should an `Employee` object be responsible for saving itself to MongoDB?

The selected design does not place database or storage operations inside the `Employee` class.

For example, this design is avoided:

```python
class Employee:

    def save_to_mongodb(self):
        # Database logic
        pass
```

The reason is that the responsibility of `Employee` is to represent employee information.

Saving data is a persistence responsibility.

Therefore, persistence is handled by the repository:

```text
Employee
   ↓
EmployeeRepository
   ↓
Database / JSON / other storage
```

This means the `Employee` class does not need to know:

* Which database is being used
* How a connection is created
* How data is stored
* How data is converted into database format

For the current project, JSON is used as the storage format. The same separation makes it easier to change the storage mechanism later.

For example:

```text
Current:
EmployeeRepository
        ↓
JSON

Possible future:
EmployeeRepository
        ↓
MongoDB
```

The employee model can remain focused on employee data.

---