import pandas as pd
import re

df = pd.read_csv("data.csv")
df2 = pd.read_csv("data2.csv")

# Add a prefix or suffix to the column names in a DataFrame
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add_prefix.html
df.add_prefix("pre_")
df.add_suffix("_suf")


# Add a column at a specific index
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.insert.html
df.insert(3, "new_column", df2["new_column"])  # Insert at 3rd column

# Text item exists in column
df["name"].str.contains("John")
df["phone_number"].str.contains("...-...-...", regex=True)


# Findall regex pattern with flags
# https://pandas.pydata.org/docs/reference/api/pandas.Series.str.findall.html
pattern = "([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\\.([A-Z]{2,4})"

df["email"].str.findall(pattern, flags=re.IGNORECASE)
