import json
import pandas as pd

rows = []

with open("output/candidate_profiles.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        p = json.loads(line)

        signals = p.get("redrob_signals", {})

        behavior_score = (
            signals.get("profile_completeness_score", 0) / 100 * 0.25 +
            signals.get("recruiter_response_rate", 0) * 0.25 +
            signals.get("interview_completion_rate", 0) * 0.25 +
            signals.get("offer_acceptance_rate", 0) * 0.25
        )

        rows.append({
            "candidate_id": p["candidate_id"],
            "behavior_score": behavior_score
        })

df = pd.DataFrame(rows)

df.to_csv(
    "output/behavior_scores.csv",
    index=False
)

print(df.head())
print("Behavior Scores Saved")