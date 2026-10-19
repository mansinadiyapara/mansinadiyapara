import pandas as pd

# df = pd.read_csv('data.csv')
# new = df.dropna()
# print(new)
# df = pd.read_csv('data.csv')
# df.dropna(inplace = True)
# print(df)
# df = pd.read_csv('data.csv')
# df.fillna({"Calories": 130}, inplace=True)
# print(df)

# print(pd.options.display.max_rows)

print(pd.__version__)

my_dataset = {
    'cars':['Volvo','BMW','Ford'],
    'passings':[3,2,1]
}
my_var = pd.DataFrame(my_dataset)
print(my_var)

a = [1,2,3]
abc = pd.Series(a)
print(abc)
print(abc[0])
var  = pd.Series(a, index=["x","y","z"])
print(var)

calories = {"day1": 420, "day2": 380, "day3": 390}
cal = pd.Series(calories, index = ["day1", "day2"])
print(cal)

# df = pd.read_json('data.json')
# print(df.info())


# import pandas as pd

# data = {
#     "Date": [
#         "2026-01-05", "2026-01-08", "2026-01-12",
#         "2026-01-15", "2026-02-03", "2026-02-07",
#         "2026-02-10", "2026-02-14", "2026-03-02",
#         "2026-03-06", "2026-03-11", "2026-03-15",
#         "2026-01-18", "2026-02-20", "2026-03-20",
#         "2026-01-22", "2026-02-24", "2026-03-25"
#     ],
#     "Region": [
#         "West", "East", "West", "North", "East", "West",
#         "North", "East", "West", "North", "East", "West",
#         "South", "South", "South", "North", "West", "East"
#     ],
#     "Salesperson": [
#         "Amit", "Priya", "Amit", "Neha", "Priya", "Amit",
#         "Neha", "Priya", "Amit", "Neha", "Priya", "Amit",
#         "Ravi", "Ravi", "Ravi", "Neha", "Amit", "Priya"
#     ],
#     "Product": [
#         "Laptop", "Mobile", "Laptop", "Tablet", "Laptop",
#         "Mobile", "Tablet", "Mobile", "Laptop", "Tablet",
#         "Laptop", "Mobile", "Tablet", "Laptop", "Mobile",
#         "Laptop", "Tablet", "Laptop"
#     ],
#     "Quantity": [
#         5, 10, 3, 8, 4, 12, 6, 15, 7,
#         9, 6, 11, 5, 3, 14, 4, 7, 2
#     ],
#     "Sales": [
#         250000, 150000, 150000, 120000, 200000, 180000,
#         90000, 225000, 350000, 135000, 300000, 165000,
#         75000, 180000, 210000, 200000, 105000, 100000
#     ]
# }

# df = pd.DataFrame(data)

# df["Date"] = pd.to_datetime(df["Date"])
# df["Month"] = df["Date"].dt.month_name()

# print(df)
# print("\nDataFrame shape:", df.shape)
# print("\nColumn names:", df.columns.tolist())

# table = pd.pivot_table(
#     df,
#     values="Sales",
#     index="Region",
#     aggfunc="sum"
# )

# print(table)

# table = pd.pivot_table(
#     df,
#     values="Sales",
#     index="Region",
#     columns="Product",
#     aggfunc="sum",
#     fill_value=0
# )

# print(table)

# table = pd.pivot_table(
#     df,
#     values="Sales",
#     index="Month",
#     aggfunc="sum"
# )

# print(table)

# table = pd.pivot_table(
#     df,
#     values="Sales",
#     index="Region",
#     aggfunc=["sum", "mean", "count"]
# )

# print(table)

# table = pd.pivot_table(
#     df,
#     values="Quantity",
#     index="Salesperson",
#     columns="Product",
#     aggfunc="sum",
#     fill_value=0,
#     margins=True
# )

# print(table)