import pandas as pd

df = pd.read_csv("output/final_ranked_candidates.csv")

top100 = df.head(100)

top100.to_csv(
    "output/top100.csv",
    index=False
)

print("Top 100 Saved")