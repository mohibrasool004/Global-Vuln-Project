import pandas as pd

df = pd.read_csv("data/raw/cnnvd.csv")
df.columns = df.columns.str.strip()  # Remove any spaces

print(df.columns)  # Check if 'description' exists now
