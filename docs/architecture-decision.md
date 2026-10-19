# Architecture Decision: Employee Management Platform

**Status:** Proposed  
**Language:** Python  
**Initial scale:** Approximately 100 employees  
**Primary goal:** Keep the application maintainable as requirements change.

---

## 1. Problem Analysis

The platform must manage employee records and support validation, notifications, reporting, logging, persistent storage, and automated tests. Management expects the system to grow, and requirements may change.

The architecture should:

- Keep business rules separate from storage and user-interface code.
- Allow storage to change without rewriting employee-management logic.
- Allow notification methods and employee types to be added with limited changes.
- Make important behavior testable without a real database or external services.
- Handle failures consistently and record useful diagnostic information.
- Avoid unnecessary complexity while the application is small.

## 2. Assumptions

The following are design assumptions because the requirement does not specify every implementation detail:

1. The first version is a Python application.
2. The system initially manages about 100 employee records.
3. Employee data must remain available after the application exits.
4. SQLite is sufficient for the initial version.
5. The application may later need a server database or web/API interface.
6. Notifications can initially be simulated or logged during development.
7. Employee records have an ID, name, email, department, and salary. More fields may be added later.
8. Automated tests should run without sending real notifications.
9. Access control and deployment requirements will be clarified before a production release.

## 3. Proposed Components

| Component | Purpose |
|---|---|
| Employee model | Represents employee data |
| Employee service | Coordinates employee use cases and business rules |
| Validator | Checks employee input and domain rules |
| Repository interface | Defines storage operations independently of storage technology |
| Repository implementations | Store and retrieve data using SQLite or another supported source |
| Notification interface/service | Requests notifications without depending on a particular provider |
| Reporting service | Builds reports from employee data |
| Logging configuration | Configures consistent application logging |
| Composition root / `main.py` | Creates implementations and injects dependencies |
| Tests | Verify behavior at unit, repository, and integration levels |

## 4. Responsibilities and Boundaries

- **Employee model:** Holds employee attributes and, if appropriate, simple domain behavior.
- **Employee service:** Coordinates adding, updating, searching, and deleting employees. It calls validators and repositories rather than directly issuing SQL.
- **Validator:** Checks required fields, formats, allowed values, and business constraints.
- **Repository interface:** Defines operations such as `get_all`, `get_by_id`, `add`, `update`, and `delete`.
- **Repository implementation:** Handles SQL, transactions, database connections, or JSON file details.
- **Notification service:** Sends or simulates notifications through a selected provider.
- **Reporting service:** Calculates and formats reports. It should not duplicate storage logic.
- **Logger:** Records operational events and errors without logging unnecessary personal information.
- **`main.py`:** Selects concrete implementations and injects them into services. Business logic should not choose its own storage implementation.

## 5. Data Flow

### Example: Add an employee

1. The user interface collects employee details.
2. The employee service receives the request.
3. The validator checks the details and business rules.
4. If validation fails, the service returns a clear validation error and does not save the employee.
5. If validation succeeds, the service calls the repository interface.
6. The repository implementation persists the record and commits the operation.
7. The service records the result in the application log.
8. If the operation requires a notification, the service requests it through the notification interface.
9. The service returns a success result.

### Failure behavior

- Validation failure: do not save; return a useful error.
- Storage failure: roll back where possible, log the exception, and report that the operation failed.
- Notification failure: log the failure. Unless the business requirement says otherwise, do not silently undo an employee record that was already saved.
- Unexpected failure: log diagnostic details and return a safe message to the caller.

## 6. Class Responsibilities

These are proposed classes; names may be adjusted to match the final implementation.

| Class / abstraction | Responsibility |
|---|---|
| `Employee` | Represents employee data |
| `EmployeeValidator` | Validates employee fields and rules |
| `EmployeeService` | Coordinates employee use cases |
| `EmployeeRepository` | Defines the storage contract |
| `SQLiteEmployeeRepository` | Implements persistence using SQLite |
| `JsonEmployeeRepository` | Optional implementation for JSON storage or import/export |
| `NotificationSender` | Defines the required notification behavior |
| `LoggingNotificationSender` | Simulates notifications by logging them |
| `EmailNotificationSender` | Optional email implementation |
| `ReportService` | Creates employee reports |
| `main()` / application setup | Constructs implementations and injects dependencies |

Use an abstract base class or `typing.Protocol` for an interface when it provides real value. Do not introduce an abstraction solely to increase the number of classes.

## 7. Storage Strategy

### Initial decision

Use **SQLite** as the primary persistent store for the first version. It provides structured queries, constraints, and transactions without requiring a separate database server.

### Design rules

- Access storage through the repository interface.
- Keep SQL and database connection management inside the SQLite repository.
- Use parameterized SQL queries.
- Use transactions for operations that must succeed or fail together.
- Add schema migrations if the database structure changes over time.
- Use test databases or in-memory SQLite databases for repository tests.

### Future migration

If multiple application instances or heavier concurrent access become requirements, evaluate PostgreSQL or another server database. Because services depend on the repository interface rather than SQL details, the new repository can be introduced with less impact on business logic.

JSON can remain useful for simple exports, fixtures, or a small local prototype, but it is not the selected primary store for a growing platform.

## 8. Error-Handling Strategy

Use clear, predictable error handling:

- **Validation errors:** Explain which field or rule failed.
- **Duplicate ID or email:** Reject the operation with a domain-level error if uniqueness is required.
- **Not found:** Return a clear result or raise a specific not-found exception.
- **Storage errors:** Log the technical exception, roll back the transaction when possible, and return a safe application-level error.
- **Notification errors:** Log the failure and apply the agreed retry or failure policy.
- **Unexpected errors:** Capture diagnostic information in logs and avoid showing stack traces or sensitive data to ordinary users.

Avoid catching every exception and silently continuing. Catch exceptions where the application can respond meaningfully.

## 9. Logging Strategy

Use Python's standard `logging` module with a centralized configuration.

| Level | Example |
|---|---|
| `DEBUG` | Detailed diagnostic information during development |
| `INFO` | Employee record created or report generated |
| `WARNING` | A recoverable or unexpected condition occurred |
| `ERROR` | A requested operation failed |
| `CRITICAL` | The application cannot continue safely |

Log useful identifiers and operation outcomes where appropriate, but avoid passwords, authentication tokens, and unnecessary personal employee data. Configure log rotation and retention for longer-running deployments. Tests should be able to capture logs when checking error behavior.

## 10. Testing Strategy

Use automated tests at several levels.

| Test type | What it verifies |
|---|---|
| Unit tests | Validation and employee business rules |
| Service tests | Use cases using fake repositories and fake notification senders |
| Repository tests | Correct saving, retrieval, update, delete, and transaction behavior |
| Integration tests | Real interactions between services and a test database |
| Notification tests | Correct notification requests without sending real messages |
| Reporting tests | Correct counts, grouping, and calculated values |
| Error-path tests | Behavior for invalid input, missing records, and dependency failures |

Use Python's `unittest` or `pytest`. Keep most unit tests fast and isolated; retain integration tests because fakes alone cannot verify actual database behavior.

## 11. Proposed Folder Structure

```text
python-training/
├── src/
│   └── employee_platform/
│       ├── __init__.py
│       ├── main.py
│       ├── models/
│       │   └── employee.py
│       ├── services/
│       │   ├── employee_service.py
│       │   ├── notification_service.py
│       │   └── report_service.py
│       ├── repositories/
│       │   ├── employee_repository.py
│       │   ├── sqlite_employee_repository.py
│       │   └── json_employee_repository.py
│       ├── validators/
│       │   └── employee_validator.py
│       └── utils/
│           └── logging_config.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fakes/
├── docs/
│   └── architecture-decision.md
├── logs/
├── requirements.txt
└── README.md
```

The exact layout can be simplified for a small coursework project. Keep tests and documentation separate from application code.

## 12. Possible Future Changes

| Possible change | Design response |
|---|---|
| Add contract or part-time employees | Introduce explicit employee types or domain rules only where behavior differs |
| Replace SQLite | Add another repository implementation |
| Add WhatsApp or SMS | Add a notification sender implementing the same contract |
| Add validation rules | Extend validator/rule components and add tests |
| Add PDF or Excel reports | Add report formatters or exporters |
| Add a web interface or API | Add a new presentation layer that calls the same services |
| Support multiple users | Evaluate authentication, authorization, concurrency, and a server database |
| Add role-based access | Add authorization policies around use cases |

## 13. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Too many abstractions for a small project | Add interfaces at likely change boundaries; keep the initial design modular but simple |
| Invalid or inconsistent data | Centralize validation and enforce appropriate database constraints |
| Database failure or data corruption | Use transactions, backups, and repository integration tests |
| Notification provider outage | Log failures and define retry or delivery-status behavior |
| Inadequate test coverage | Automate unit and integration tests in the development workflow |
| Sensitive data appears in logs | Define logging rules and review log messages |
| Growth creates concurrency or performance problems | Measure real usage and revisit database and deployment choices when requirements justify it |

## 14. Alternatives Considered

| Decision area | Alternative | Reason for decision |
|---|---|---|
| Storage access | SQL directly inside the employee service | Simpler at first, but couples business logic to the database; prefer a repository boundary |
| Initial storage | JSON file | Easy to inspect, but lacks relational constraints and transaction support; retain it only where useful |
| Initial database | PostgreSQL immediately | Powerful, but may add operational complexity before it is needed; reassess if deployment or concurrency requires it |
| Notifications | Provider-specific calls inside employee service | Quick initially, but makes testing and provider changes harder; use a small interface |
| Testing | All tests use a real database and live notification provider | Less isolated, slower, and can have side effects; use fakes for unit tests and a test database for integration tests |
| Architecture style | Microservices | Adds deployment and communication complexity; start with a modular monolith and split services only when justified |

## 15. Final Decision

Build a **modular Python application** with clear boundaries between employee models, validation, services, repositories, notifications, reporting, and logging.

Use SQLite for initial persistent storage. Make services depend on repository and notification interfaces, and inject the concrete implementations during application setup. Use centralized logging, unit tests with fakes, and integration tests against a test database.

This design avoids tying business logic to a specific storage or notification provider while keeping the first version understandable. Revisit the architecture when actual requirements—such as concurrent users, deployment scale, or operational constraints—justify additional complexity.
