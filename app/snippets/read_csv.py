import pandas as pd


# Read a CSV with limited columns
df = pd.read_csv("data.csv", usecols=["date", "price"])

# Read a CSV that passes columns as datetimes
df = pd.read_csv("data.csv", parse_dates=["date_col_name"])

# Read a CSV with specific data types
# https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#dtypes
df = pd.read_csv(
    "data.csv",
    dtype={
        "column_name": "dtype",
    },
)

# Read a small sample of a CSV dataset
df = pd.read_csv("data.csv", nrows=100)
