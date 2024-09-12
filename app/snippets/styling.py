import pandas as pd


df = pd.read_csv("data.csv")

# String layout formatting
format_dict = {
    "Date": "{:%d/%m/%y}",
    "Open": "${:.2f}",
    "Close": "${:.2f}",
    "Volume": "{:,}",
}

df.style.format(format_dict)


# Adding colour
# https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html
df.style.format(format_dict).hide_index().highlight_min(
    ["Open"], color="red"
).highlight_max(["Open"], color="green").background_gradient(
    subset="Close", cmap="Greens"
).bar("Volume", color="lightblue", align="zero").set_caption(
    "Tesla Stock Prices in 2017"
)
