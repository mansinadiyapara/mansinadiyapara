import pandas as pd

employees = pd.read_csv("data/employees.csv")
attendance = pd.read_csv("data/attendance.csv")
activity = pd.read_csv("data/activity.csv")

print("pandas version", pd.__version__)

print("Employees Dataframe Type", type(employees))
print("Attendance Dataframe Type", type(attendance))
print("Activity Dataframe Type", type(activity))

print("Show First 5 Rows of employees", employees.head())
print("Show Last 5 Rows of employees", employees.tail())
print("Shape of Employee DataFrame", employees.shape)
print("Show the list of columns in Employee Dataframe", employees.columns)
print("Rename of Column", employees.rename(columns={'salary': 'monthly_salary'}, inplace=True))
print("Employee Info", employees.info())
print("Employee Describe", employees.describe())
print("Show single row", employees[['employee_name']])
print("Show single row using loc", employees.loc[employees.employee_name=='Aarav Shah'])
print("Show multiple row using loc", employees.loc[(employees.employee_name=='Aarav Shah') & (employees.monthly_salary>=40000)])
print("Display data using loc indexing", employees.loc[0:2])
print("Display data using iloc indexing", employees.iloc[0:2])

print("Filter by duration_minutes", activity[activity['duration_minutes']<=0])
print("Filter by duration_minutes and completed", activity[(activity['duration_minutes']<=0) & (activity['completed']=='Yes')])
print("Filter by where function", activity.where(activity['duration_minutes']<=0, other = 'Not Eligible'))

employees.loc[employees["employee_name"] == "Aarav Shah", "monthly_salary"] = 45000
print("Updated value:", employees.loc[employees["employee_name"] == "Aarav Shah", "monthly_salary"])
# print("Sort values", employees.sort_values('monthly_salary'))
# print("Sort values", employees.sort_values('monthly_salary', ascending=False))
print("Type of Joining Date", employees['joining_date'].dtype)
employees['joining_date'] = pd.to_datetime(employees['joining_date'])
print("Type of Joining Date", employees['joining_date'].dtype)
# print("Show Joining Date year",employees['joining_date'].dt.year)
# print("Show Joining Date month",employees['joining_date'].dt.month)
# print("Show Joining Date day",employees['joining_date'].dt.day)
# print("Show Joining Date day's name",employees['joining_date'].dt.day_name)
print("Detect Missing Value", employees.isnull().sum())

print("Detect Missing Value", activity.isnull().sum())
print("If any null value that store with 0", activity.fillna(0))

print("Aggregation using same city name display", employees[employees['city']=='Rajkot'].value_counts)
print("Aggregation using groupby", employees.groupby('city')['monthly_salary'].sum())
print("Aggregation using groupby in mean",employees.groupby('city').agg({'monthly_salary':'mean','employee_name':'count'}))

print("Detect Missing Value", attendance.isnull().sum())
print("Detect Missing Value",attendance[attendance.isnull().any(axis=1)])

print("Duplicate count in employees:", employees.duplicated().sum())
print("Duplicate count in activity:", activity.duplicated().sum())
print("Duplicate count in attendance:", attendance.duplicated().sum())