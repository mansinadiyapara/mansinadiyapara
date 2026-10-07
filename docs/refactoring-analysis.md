| Problem                      | Why it is a problem                 | Proposed change                 | Impact                 | Risk                           | Final result               |
| ---------------------------- | ----------------------------------- | ------------------------------- | ---------------------- | ------------------------------ | -------------------------- |
| One huge class               | Difficult to maintain               | Split responsibilities          | Better maintainability | Existing behavior may change   | Smaller focused classes    |
| Duplicated logic             | Changes required in multiple places | Create reusable validation      | Less duplication       | Validation behavior may change | Centralized validation     |
| Hard-coded values            | Difficult to configure              | Move values to configuration    | Easier configuration   | Wrong configuration            | Centralized settings       |
| Tight coupling               | Difficult to replace dependencies   | Use abstraction/injection       | More flexibility       | Incorrect dependency setup     | Loosely coupled components |
| Poor naming                  | Difficult to understand             | Rename variables/functions      | Better readability     | References may break           | Clear naming               |
| Mixed storage/business logic | Difficult to test/change storage    | Separate service and repository | Better testing         | Data behavior may change       | Clear separation           |
