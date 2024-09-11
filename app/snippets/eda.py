import pandas as pd
import pandas_profiling


# One line EDA of dataset without writing plots
# Requires Python 3.7 - 3.11
# https://github.com/ydataai/ydata-profiling
df = pd.read_csv("data.csv")
profile = df.profile_report(title="Pandas Profiling Report")
profile.to_file(output_file="output.html")


# Filter columns by dtype
df.select_dtypes(include="number")
df.select_dtypes(include=["category", "datetime"])

df.select_dtypes(exclude="object")


# Infer numeric dtypes (if they are objects)
df.infer_objects().dtypes

# Downcasting column type
pd.to_numeric(df.numeric_col, downcast="integer")  # smallest signed int dtype
pd.to_numeric(df.numeric_col, downcast="float")  # smallest float dtype
