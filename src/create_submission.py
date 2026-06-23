import pandas as pd

df = pd.read_csv("output/top100.csv")

submission = pd.DataFrame()

submission["candidate_id"] = df["candidate_id"]
submission["rank"] = range(1, len(df) + 1)
submission["score"] = df["final_score"]

submission["reasoning"] = (
    df["experience"].round(1).astype(str)
    + " years experience, AI skill score "
    + df["ai_skill_score"].astype(str)
    + ", strong semantic match to AI Engineer requirements."
)

submission.to_csv(
    "output/submission.csv",
    index=False
)

print("Improved Submission Created")