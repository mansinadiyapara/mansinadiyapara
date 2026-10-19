import pandas as pd


employees = pd.read_csv("data/employees.csv")
attendance = pd.read_csv("data/attendance.csv")
activity = pd.read_csv("data/activity.csv")


for df in [employees, attendance, activity]:
    df["employee_id"] = (
        df["employee_id"]
        .astype("string")
        .str.strip()
    )


duplicate_employees = employees[
    employees["employee_id"].duplicated(keep=False)
]

print("Duplicate employee master records:")
print(duplicate_employees)


if employees["employee_id"].isna().any():
    raise ValueError("Employee master contains missing employee IDs.")

if employees["employee_id"].duplicated().any():
    raise ValueError("Resolve duplicate employee IDs before merging.")


known_ids = set(employees["employee_id"].dropna())

unmatched_attendance = attendance[
    ~attendance["employee_id"].isin(known_ids)
]

unmatched_activity = activity[
    ~activity["employee_id"].isin(known_ids)
]

print("\nUnmatched attendance records:")
print(unmatched_attendance)

print("\nUnmatched activity records:")
print(unmatched_activity)


unmatched_attendance.to_csv(
    "data/unmatched_attendance.csv", index=False
)
unmatched_activity.to_csv(
    "data/unmatched_activity.csv", index=False
)


attendance["status"] = (
    attendance["status"]
    .astype("string")
    .str.strip()
    .str.lower()
)

attendance_summary = (
    attendance[
        attendance["employee_id"].isin(known_ids)
    ]
    .groupby("employee_id")
    .agg(
        attendance_records=("date", "size"),
        present_days=("status", lambda s: s.eq("present").sum())
    )
    .reset_index()
)


activity["duration_minutes"] = pd.to_numeric(
    activity["duration_minutes"],
    errors="coerce"
)

valid_activity = activity[
    activity["employee_id"].isin(known_ids)
    & activity["duration_minutes"].notna()
    & (activity["duration_minutes"] >= 0)
].copy()

activity_summary = (
    valid_activity
    .groupby("employee_id")
    .agg(
        activity_count=("activity_type", "size"),
        total_activity_minutes=("duration_minutes", "sum"),
        average_activity_minutes=("duration_minutes", "mean")
    )
    .reset_index()
)


unified = employees.merge(
    attendance_summary,
    on="employee_id",
    how="left",
    validate="one_to_one"
)

unified = unified.merge(
    activity_summary,
    on="employee_id",
    how="left",
    validate="one_to_one"
)

summary_columns = [
    "attendance_records",
    "present_days",
    "activity_count",
    "total_activity_minutes"
]

unified[summary_columns] = unified[summary_columns].fillna(0)


unified.to_csv("data/unified_employee_data.csv", index=False)

print("\nUnified employee dataset:")
print(unified)

print("\nTotal employees:", len(unified))