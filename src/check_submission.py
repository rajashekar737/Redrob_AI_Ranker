import pandas as pd

df = pd.read_csv("output/submission.csv")

print(df.head())
print()
print("Rows:", len(df))
print("Columns:", df.columns.tolist())