import pandas as pd

# Load files
semantic = pd.read_csv(
    "output/top500_semantic.csv"
)

features = pd.read_csv(
    "output/features.csv"
)

behavior = pd.read_csv(
    "output/behavior_scores.csv"
)

activity = pd.read_csv(
    "output/activity_scores.csv"
)

# Merge all data
df = semantic.merge(
    features,
    on="candidate_id"
)

df = df.merge(
    behavior,
    on="candidate_id"
)

df = df.merge(
    activity,
    on="candidate_id"
)

# Experience score (0-1)
df["exp_score"] = (
    df["experience"] / 10
).clip(0, 1)

# AI skill score (0-1)
df["ai_skill_score"] = (
    df["ai_skill_score"] / 15
).clip(0, 1)

# Final hybrid score
df["final_score"] = (
    0.55 * df["semantic_score"]
    + 0.15 * df["exp_score"]
    + 0.10 * df["ai_skill_score"]
    + 0.10 * df["behavior_score"]
    + 0.10 * df["activity_score"]
)

# Sort by score
df = df.sort_values(
    "final_score",
    ascending=False
)

# Save ranked candidates
df.to_csv(
    "output/final_ranked_candidates.csv",
    index=False
)

# Show top 20
print(
    df[
        [
            "candidate_id",
            "semantic_score",
            "experience",
            "ai_skill_score",
            "behavior_score",
            "activity_score",
            "final_score"
        ]
    ].head(20)
)

print("\nFinal Ranking Generated")