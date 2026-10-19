# Join Analysis — Dangerous Merge

## 1. Objective

The objective of this analysis is to understand the relationships between the employee, attendance, and activity datasets before merging them.

The investigation focuses on unexpected row multiplication, join-key uniqueness, unmatched records, and the logical correctness of the resulting dataset.

## 2. Dataset Relationships

### Employees

The employee dataset is expected to contain one master record per employee.

The `employee_id` column should uniquely identify each employee.

### Attendance

An employee may have multiple attendance records.

The relationship between employees and attendance is one-to-many.

### Activity

An employee may have many activity records, potentially thousands of records.

The relationship between employees and activity is also one-to-many.

Attendance records and activity records represent different events and should not automatically be combined as though each attendance event corresponds to every activity event.

## 3. Why Row Multiplication Occurs

Suppose employee 101 has:

- 1 employee record.
- 25 attendance records.
- 18,000 activity records.

When attendance and activity are merged directly using only `employee_id`, every attendance record matches every activity record for that employee.

The resulting number of rows is:

25 × 18,000 = 450,000 rows.

This is a many-to-many join. The join produces all matching combinations, not 450,000 independent real-world activities.

## 4. Expected Versus Actual Record Counts

The expected row count depends on the intended output.

| Output | Expected rows for employee 101 |
|---|---:|
| Employee-level summary | 1 |
| Attendance-level detail | 25 |
| Activity-level detail | 18,000 |
| Direct attendance/activity merge on employee ID | 450,000 |

The actual row count must be measured using the real datasets.

The predicted count for a direct inner join can be calculated by multiplying the attendance count by the activity count for each shared employee ID and summing the results.

The predicted count should be compared with the actual merge count.

## 5. Risks of a Dangerous Merge

A direct many-to-many merge can:

- Inflate activity counts and duration totals.
- Repeat attendance information across multiple activity rows.
- Produce misleading comparisons.
- Increase processing time and memory consumption.
- Make the resulting data difficult to interpret.

A successful merge does not guarantee that the resulting dataset is suitable for analysis.

## 6. Investigation Performed

The investigation should:

1. Inspect the columns and data types in each dataset.
2. Check whether employee IDs are unique in the employee master.
3. Count attendance and activity records per employee.
4. Identify missing and unmatched employee IDs.
5. Calculate the predicted number of rows for a direct many-to-many merge.
6. Compare the predicted count with the actual count.
7. Inspect duplicate keys and determine the intended row grain.
8. Select a merge strategy that preserves the meaning of the data.

Actual record counts, unmatched-record counts, and duplicate-key findings should be recorded after running the investigation script.

## 7. Selected Merge Strategy

For an employee-level summary, attendance and activity should be summarized separately by employee ID before merging them into the employee master.

For an activity-level analysis, employee details can be attached to activity records. Attendance information should be matched at an appropriate level, such as employee ID and date, only after verifying the attendance key and relationship.

The merge should use validation checks where possible to detect unexpected duplicate keys.

## 8. Conclusion

The row count of a merged dataset must be interpreted in the context of its relationships and intended purpose.

The correct number of rows is not simply the smallest number or the number that looks reasonable. It is the number expected for the chosen data grain and join relationship.

Understanding the underlying relationships prevents row multiplication, incorrect totals, and misleading analysis.