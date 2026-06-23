import pandas as pd

df = pd.read_csv("output/final_ranked_candidates.csv")

print(df.columns.tolist())
print(df.head())