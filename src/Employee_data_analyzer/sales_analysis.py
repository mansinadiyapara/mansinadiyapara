import pandas as pd

df = pd.read_csv("data/sales.csv")


df["quantity"] = pd.to_numeric(
    df["quantity"], errors="coerce"
)

df["unit_price"] = pd.to_numeric(
    df["unit_price"], errors="coerce"
)

df["discount"] = pd.to_numeric(
    df["discount"], errors="coerce"
)

df["date"] = pd.to_datetime(
    df["date"], errors="coerce"
)

df["suspicious_reason"] = ""

df.loc[
    df["quantity"].isna(),
    "suspicious_reason"
] += "Missing or invalid quantity; "

df.loc[
    df["quantity"] <= 0,
    "suspicious_reason"
] += "Non-positive quantity; "

df.loc[
    df["unit_price"].isna(),
    "suspicious_reason"
] += "Missing or invalid price; "

df.loc[
    df["unit_price"] < 0,
    "suspicious_reason"
] += "Negative price; "

df.loc[
    (df["discount"] < 0) |
    (df["discount"] > 100),
    "suspicious_reason"
] += "Discount outside 0-100%; "

df.loc[
    df["date"].isna(),
    "suspicious_reason"
] += "Invalid date; "

suspicious = df[
    df["suspicious_reason"] != ""
]

print(suspicious)