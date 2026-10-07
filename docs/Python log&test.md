# Python File Handling, Logging, and Testing

## 1. File Handling

File handling is used to read, write, and manage employee data stored in files.

### 1.1 File Reading

Read employee data from a file when the program starts.

### 1.2 File Writing

Save employee data into a file after changes.

### 1.3 Context Managers

Use `with open(...)` to safely open and close files.

### 1.4 JSON

Store employee data in a structured `.json` format.

### 1.5 Serialization

Convert Python data, such as a dictionary, into JSON so it can be stored in a file.

### 1.6 Deserialization

Convert JSON data from the file back into Python data.

### 1.7 File Paths

Specify where the employee data file is located.

### 1.8 Error Handling

Handle problems such as:

* File does not exist
* JSON data is invalid
* File cannot be read or written
* Stored data has an unexpected format
* User enters invalid input

---

# 2. Logging

Logging means recording important events that happen while the application is running. Instead of using `print()` for application diagnostics, Python's `logging` module can save these events into a log file.

## 2.1 Logging Levels

Logging levels show how important a log message is.

| Level      | Purpose                                                         |
| ---------- | --------------------------------------------------------------- |
| `DEBUG`    | Detailed information useful during development                  |
| `INFO`     | Normal application activity                                     |
| `WARNING`  | Something unexpected happened, but the application can continue |
| `ERROR`    | A problem occurred and an operation failed                      |
| `CRITICAL` | A very serious problem that may stop the application            |

## 2.2 Logger

A logger is responsible for creating log messages.

Example:

```python
logger.info("Employee added successfully")
```

## 2.3 Handler

A handler determines where the log messages go.

Examples:

* Console
* Log file

For this task, the application should write logs to:

```text
logs/
└── application.log
```

## 2.4 Formatter

A formatter determines how each log message looks.

Example:

```text
2026-09-22 10:30:15 - INFO - Employee added successfully
```

A formatted log message can include:

* Timestamp
* Log level
* Message

## 2.5 Log File

A log file stores application events permanently.

Example:

```text
logs/
└── application.log
```

## 2.6 Timestamps

A timestamp records when an event happened.

Example:

```text
2026-09-22 10:30:15
```

This helps determine when a problem or event occurred.

## 2.7 Error Logging

Use `ERROR` when an operation fails.

Example:

```text
ERROR - Unable to load employee data
```

## 2.8 Warning Logging

Use `WARNING` when something unexpected happens but the program can continue.

Example:

```text
WARNING - Employee ID already exists
```

## 2.9 Information Logging

Use `INFO` for normal important application activities.

Examples:

```text
INFO - Employee added successfully
INFO - Employee data loaded
INFO - Employee deleted
```

## 2.10 What Should Be Logged?

| Level     | Examples                                          |
| --------- | ------------------------------------------------- |
| `INFO`    | Employee added, updated, deleted                  |
| `WARNING` | Employee ID already exists, invalid operation     |
| `ERROR`   | File cannot be read, unexpected application error |
| `DEBUG`   | Detailed development information                  |

## 2.11 What Should NOT Be Logged?

Avoid logging sensitive information, such as:

* Passwords
* Authentication tokens
* Unnecessary personal data

---

# 3. Testing

Testing is used to check whether different parts of the application work correctly.

## 3.1 Unit Tests

Unit tests test a small part of the application, usually one function, to check whether it works correctly.

## 3.2 Test Cases

A test case is a specific situation used to test the expected behavior of the application.

## 3.3 Assertions

Assertions compare the actual result with the expected result.

Example:

```python
assertEqual(actual, expected)
```

## 3.4 Edge Cases

Edge cases test unusual, boundary, or extreme inputs that could cause problems.

Examples:

```text
Salary = 0
Salary = -1000
Name = ""
```

## 3.5 Test Organization

Keep test files and test cases properly structured, usually inside a separate:

```text
tests/
```

folder.

## 3.6 Test Naming

Give tests clear names that describe what they are testing.

Example:

```python
test_salary_cannot_be_negative()
```

## 3.7 Test Isolation

Each test should work independently and should not depend on another test's data or execution order.
