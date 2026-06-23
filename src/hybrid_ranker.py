import pandas as pd

semantic = pd.read_csv(
    "output/top500_semantic.csv"
)

features = pd.read_csv(
    "output/features.csv"
)

df = semantic.merge(
    features,
    on="candidate_id"
)

df["exp_score"] = (
    df["experience"] / 10
).clip(0, 1)

df["ai_skill_score"] = (
    df["ai_skill_score"] / 15
).clip(0, 1)

df["final_score"] = (
      0.75 * df["semantic_score"]
    + 0.15 * df["ai_skill_score"]
    + 0.10 * df["exp_score"]
)

df = df.sort_values(
    "final_score",
    ascending=False
)

df.to_csv(
    "output/final_ranked_candidates.csv",
    index=False
)

print(df.head(20))

print("\nFinal Ranking Generated")