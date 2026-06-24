import json
import pandas as pd

rows = []

with open("output/candidate_profiles.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        p = json.loads(line)

        s = p.get("redrob_signals", {})

        activity_score = (
            min(s.get("github_activity_score",0)/10,1)*0.30 +
            min(s.get("saved_by_recruiters_30d",0)/10,1)*0.25 +
            min(s.get("search_appearance_30d",0)/300,1)*0.25 +
            min(s.get("endorsements_received",0)/100,1)*0.20
        )

        rows.append({
            "candidate_id": p["candidate_id"],
            "activity_score": activity_score
        })

df = pd.DataFrame(rows)

df.to_csv(
    "output/activity_scores.csv",
    index=False
)

print(df.head())
print("Activity Scores Saved")