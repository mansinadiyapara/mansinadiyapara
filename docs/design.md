
# Project Design: Sales Data Processor

## 1. Project Overview

The Sales Data Processor loads sales and product datasets,
validates and cleans the data, merges related records,
calculates sales totals, and exports a report.

The project uses separate modules for each major
responsibility to improve maintainability, testability,
and readability.

## 2. Project Structure

- src/: Contains the application's Python source code.
- tests/: Contains automated tests for application modules.
- docs/: Contains design decisions and debugging notes.
- config/: Contains non-secret application settings.
- data/input/: Contains source CSV files.
- output/: Contains generated sales reports.
- logs/: Contains application log files.
- requirements.txt: Lists required Python packages.
- .gitignore: Excludes temporary, generated, and sensitive files.

## 3. Module Responsibilities

### main.py
Coordinates the processing workflow and handles
the overall execution of the application.

### loader.py
Loads source datasets and reports loading errors.

### cleaner.py
Validates records and handles missing, invalid,
and duplicate data according to defined rules.

### merger.py
Combines datasets using the appropriate keys
and checks for unexpected row duplication.

### calculator.py
Calculates sales revenue and other required totals.

### exporter.py
Exports processed results to the required report format.

## 4. Data Flow

1. Read source files from data/input/.
2. Validate and clean the loaded records.
3. Merge sales data with product information.
4. Calculate sales totals.
5. Export the report to output/.
6. Record processing events in logs/.

## 5. Testing Strategy

Automated tests are stored in tests/.

Tests cover:
- Normal data
- Missing and invalid values
- Duplicate records
- Empty files
- Missing or unexpected columns
- Incorrect merge behavior
- Sales total calculations
- Report export behavior

## 6. Logging Strategy

The application records processing start and finish times,
input filenames, record counts, invalid record counts,
processing durations, and errors.

Logs are written to logs/application.log.

## 7. Design Decisions

The project separates data loading, cleaning, merging,
calculation, and export because each operation has
a distinct responsibility.

Tests are separate from application code so that
individual behaviors can be verified independently.

Input data, generated reports, and logs are stored
in separate directories to avoid confusion and
accidental overwriting.

Configuration is kept separate from business logic
so that file paths and processing settings can be
changed without rewriting core modules.

## 8. Expected Benefits

- Easier debugging and maintenance.
- Clear separation of responsibilities.
- Better automated test coverage.
- Easier identification of processing failures.
- Simpler addition of new features.
