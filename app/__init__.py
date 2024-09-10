import pandas as pd


def pandas_settings() -> None:
    """
    Applies Pandas utility settings to provide better readability
    for DataFrames in Notebooks.

    This includes:
    - Float value DataFrame outputs are configured to 2 decimal places
    - All columns are displayed in output
    """
    pd.options.display.float_format = "{:20.2f}".format
    pd.set_option("display.max_columns", 999)


def missing_values(df: pd.DataFrame) -> dict[str, int]:
    """
    Returns a dictionary of columns with missing values: `{column_name, count}`.
    """
    missing_series = df.isna().sum()
    return missing_series[missing_series > 0].to_dict()
