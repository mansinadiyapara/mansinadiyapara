# Inheritance vs Composition

Difference of inheritance vs composition

| Aspect |    Inheritance   | Composition                       |
| :-------- | :------- | :-------------------------------- |
|  Relationship     |  Represents an "is-a" relationship (e.g., a car is a vehicle)  | Represents an "has-a" relationship (e.g., a car has an engine)  |
|  Code Reusability     |  Reuse existing functionality by inheriting from parent classes | Reuse functionality by delegating tasks to other objects |
|  Flexibility     | Less flexible; changes in the parent affect all subclasses | More flexible; components can be swapped easily |
|  Coupling     | Leads to "Tight Coupling" between the parent and child | "Losser Coupling", making the system more modular |
|  Extensibility     | Can result in complex heirarchies that are hard to extend or modify | components can be added or removed easily without affecting the entire system |
|  Testing     | Harder to test in isolation, since the child class is dependent on the parent | Easier to test, as individual components can be tested separately |

## 1. Problem Statement

The Employee Management System needs to manage different entities such as employees, managers, departments, and employee addresses.

An employee has basic information such as name, email, salary, and department. A manager also has employee-related information but has additional responsibilities, such as managing a team.

Employees belong to departments and may have address information.

The relationship between these entities is intentionally not predefined. The developer must decide whether the relationship should be implemented using inheritance, composition, or simple association.

The main goal is to select the most appropriate relationship based on the meaning and responsibility of each entity.

---

## 2. Domain Entities

The main entities in this domain are:

### Employee

The Employee represents a person working in the organization.

Example responsibilities:

* Store employee information.
* Store salary information.
* Store contact information.
* Maintain the employee's department relationship.

### Manager

The Manager represents an employee who has additional management responsibilities.

Example responsibilities:

* Perform normal employee responsibilities.
* Manage a team.
* Assign work to employees.
* Monitor team activities.

### Department

The Department represents an organizational unit.

Example responsibilities:

* Store department information.
* Maintain information about employees working in the department.
* Identify the department name or department ID.

### Address

The Address represents an employee's address information.

Example information:

* House number
* Street
* City
* State
* Country
* PIN code

---

## 3. Why Inheritance Might Work

Inheritance can be considered for the relationship between Manager and Employee.

A manager is a specialized type of employee. A manager has common employee information such as name, email, salary, and employee ID, but also has additional responsibilities related to managing a team.

Therefore, the relationship can be described as:

**Manager IS-A Employee**

Conceptually:

```
Employee
   |
   ↓
Manager
```

Inheritance can help avoid duplicating common employee properties and behaviors.

For example, if Employee contains common functionality such as displaying employee information, Manager can reuse that functionality and add manager-specific behavior.

Inheritance can therefore provide:

* Code reuse
* Common behavior
* Clear specialization
* Polymorphism

---

## 4. Why Inheritance Might Be a Bad Choice

Inheritance should not be used just because two entities are related.

Inheritance is appropriate when there is a strong "IS-A" relationship.

For example:

**Department IS NOT an Employee.**

Therefore, Department should not inherit from Employee.

Similarly, Address is not an Employee. It is information associated with an employee.

Inheritance can also create tight coupling between parent and child classes.

If the Employee class changes significantly, the Manager class may also be affected.

A large inheritance hierarchy can become difficult to understand and maintain.

For example:

```
Employee
   |
   ↓
Manager
   |
   ↓
SeniorManager
   |
   ↓
RegionalManager
```

Such a deep hierarchy may become difficult to modify when business requirements change.

Therefore, inheritance should only be selected when the relationship represents a genuine specialization.

---

## 5. When Composition Is Better

Composition is better when one entity contains or uses another entity instead of being a specialized version of it.

For example:

**Employee HAS-A Address**

An Address is not a type of Employee. It is a separate object containing address-related information.

Conceptually:

```
Employee
   |
   ↓
Address
```

Composition allows the Employee object to contain an Address object.

This provides better separation of responsibil
