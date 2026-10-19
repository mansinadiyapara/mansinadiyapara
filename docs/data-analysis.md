# Employee Data Analysis Application

## 1. Project Overview

The Employee Data Analysis Application is a Python-based data-processing project that uses Pandas to analyze employee information, attendance records, employee activities, and working duration.

The application processes CSV files, checks data quality, performs calculations, and generates useful reports to help understand employee and department data.

## 2. Objectives

- Load employee-related datasets from CSV files.
- Analyze employees and departments.
- Calculate attendance summaries.
- Calculate employee working duration.
- Analyze employee activities and activity duration.
- Identify missing and invalid data.
- Clean inconsistent records.
- Use Pandas DataFrames, grouping, merging, and pivot tables.
- Generate meaningful statistical summaries and reports.

## 3. Dataset Description

The application uses three datasets.

### 3.1 employees.csv

This file contains basic employee information.

**Columns:**
- `employee_id`: Unique employee identifier.
- `employee_name`: Name of the employee.
- `department`: Department in which the employee works.
- `job_title`: Employee's job role.
- `joining_date`: Date the employee joined the organization.
- `salary`: Employee's salary.
- `city`: Employee's city.

### 3.2 attendance.csv

This file contains employee attendance records.

**Columns:**
- `employee_id`: Employee identifier.
- `date`: Attendance date.
- `status`: Attendance status, such as Present, Absent, or Leave.
- `check_in`: Employee check-in time.
- `check_out`: Employee check-out time.
- `break_minutes`: Break duration in minutes.

### 3.3 activity.csv

This file contains employee activity records.

**Columns:**
- `employee_id`: Employee identifier.
- `date`: Activity date.
- `activity_type`: Type of activity, such as Coding, Meeting, Email, Report, Training, or Support.
- `duration_minutes`: Time spent on the activity in minutes.
- `completed`: Indicates whether the activity was completed.

## 4. Technologies Used

- Python
- Pandas
- NumPy
- CSV files
- Jupyter Notebook or a Python IDE
- Git for version control

## 5. Data Processing

### 5.1 Data Loading

The application loads the three CSV files into Pandas DataFrames using `pd.read_csv()`.

### 5.2 Data Inspection

The application uses the following methods to inspect the datasets:

- `head()` to display the first records.
- `shape` to check the number of rows and columns.
- `info()` to inspect column data types and missing values.
- `describe()` to calculate numerical summaries.
- `isnull().sum()` to count missing values.

### 5.3 Data Cleaning

The application checks for:

- Missing values.
- Invalid dates and times.
- Negative durations.
- Inconsistent category names.
- Duplicate records.
- Unknown employee IDs.
- Unusually large activity durations.
- Check-out times earlier than check-in times.

Data should be corrected, excluded from specific calculations, or flagged for review according to documented rules. Unusual values should not automatically be treated as errors.

## 6. Employee Analysis

Employee analysis includes:

- Total number of employees.
- Employee count by department.
- Employee count by city.
- Average salary by department.
- Minimum and maximum salary.
- Employee joining-date analysis.

Pandas `groupby()` and `pivot_table()` are used to summarize employee information.

## 7. Attendance Analysis

Attendance analysis includes:

- Total attendance records.
- Present, absent, and leave counts.
- Attendance summaries by employee.
- Attendance summaries by department.
- Missing check-in and check-out records.
- Invalid attendance statuses.
- Potential duplicate attendance records.

## 8. Working Duration Analysis

Working duration is calculated using check-in time, check-out time, and break duration.

For a valid same-day attendance record:

**Working duration = Check-out time − Check-in time − Break duration**

The application should handle missing times, invalid times, overnight shifts, and negative calculated durations according to its validation rules.

Working duration is calculated only when the required time values are valid.

## 9. Employee Activity Analysis

Activity analysis includes:

- Total number of activities.
- Total activity duration by employee.
- Total activity duration by department.
- Activity counts by type.
- Completed and incomplete activity counts.
- Missing or invalid activity durations.
- Unusually long activity records.

These summaries help describe recorded activity. Activity duration alone does not necessarily measure employee productivity.

## 10. Data Quality Analysis

Data quality is evaluated by checking:

- Completeness: Are required values present?
- Validity: Do values follow expected formats and rules?
- Consistency: Are categories and identifiers consistent?
- Uniqueness: Are unexpected duplicate records present?
- Referential integrity: Does each employee ID correspond to an employee in `employees.csv`?

The application reports data-quality problems so they can be investigated.

## 11. Pandas Operations

The project practices the following Pandas operations:

- Creating and inspecting DataFrames.
- Selecting columns and filtering rows.
- Updating values with `loc`.
- Handling missing values.
- Converting date and time columns.
- Grouping data with `groupby()`.
- Combining datasets with `merge()`.
- Creating summaries with `pivot_table()`.
- Sorting and aggregating data.
- Exporting reports to CSV files.

## 12. Expected Reports

The application should eventually generate reports such as:

1. Employee Summary Report.
2. Department Summary Report.
3. Attendance Summary Report.
4. Working Duration Report.
5. Employee Activity Report.
6. Data Quality Report.

## 13. Project Folder Structure

```text
python-training/
├── data/
│   ├── employees.csv
│   ├── attendance.csv
│   └── activity.csv
├── src/
│   └── employee_data_analysis.py
└── docs/
    └── employee-data-analysis.md
```

## 14. Conclusion

The Employee Data Analysis Application provides practical experience in processing related datasets using Python, Pandas, and NumPy.

The project demonstrates how to load data, inspect its quality, clean invalid records, combine datasets, calculate working durations, analyze departments, and generate reports.

The main goal is to turn raw employee-related data into reliable and meaningful information while documenting assumptions, data-quality issues, and limitations.

## Data Cleaning: Missing Values and Duplicates

### Missing Values

I checked the employee, attendance, and activity datasets for missing values using Pandas.

Missing values can occur when information is not recorded, a system fails, or data entry is incomplete. I will not automatically delete rows containing missing values.

For each missing field, I will investigate whether the value can be recovered from a reliable source. If it cannot be recovered, I will flag the record and exclude it only from calculations that require that missing information.

For example, working duration cannot be calculated reliably when a required check-in or check-out time is missing.

### Duplicate Records

I will investigate three types of repeated records:

1. **Exact duplicates:** All fields are identical. If they represent the same event, a redundant copy can be removed.
2. **Conflicting duplicates:** Identifying fields match, but one or more values differ. These require investigation before any correction.
3. **Legitimate repeated records:** Multiple rows represent separate valid events. These must be retained.

### Assumptions and Decisions

- Missing employee IDs will be investigated rather than guessed.
- Missing departments will be checked against reliable employee records.
- Missing attendance times will be flagged before calculating working duration.
- Exact duplicates will be removed only after confirming they are redundant.
- Conflicting records will be flagged until the correct values can be established.
- Legitimate repeated transactions or activities will be preserved.

### Conclusion

Data cleaning requires understanding the meaning of each record. Pandas can identify missing values and repeated rows, but the developer must use business rules and source information to decide how to handle them.

## Data Normalization and Invalid Data

### Data Normalization

The purpose of data normalization is to maintain consistent values across the employee, attendance, and activity datasets.

Changes performed:
- Removed unnecessary leading and trailing spaces from text fields.
- Standardized department names using uppercase letters.
- Converted valid salary and duration values to appropriate numeric types.
- Standardized valid dates into a consistent date format.
- Investigated spelling differences before correcting them.

Changes intentionally not performed:
- Did not change employee names without evidence of an error.
- Did not assume that similar category names always mean the same thing.
- Did not remove special characters without checking their meaning.
- Did not replace unknown values with guessed values.

### Invalid Data

Invalid records were identified using validation rules.

Examples of validation rules:
- Employee IDs must follow the required ID format.
- Salary must not be negative.
- Attendance times must be valid and logically consistent with the work schedule.
- Activity duration must not be negative.
- Employee IDs in attendance and activity records should exist in the employee master dataset.

Invalid records are reported with the affected row, field name, original value, problem description, and recommended action.

Invalid records are not silently deleted. They are flagged for review or rejected according to the relevant business rule.

### Conclusion

Normalization improves consistency, while validation identifies data that violates defined rules. Both processes improve data quality and help produce reliable analysis results.