import json

with open(
    "output/candidate_profiles.jsonl",
    "r",
    encoding="utf8"
) as f:

    first = json.loads(
        f.readline()
    )

print(
    "Candidate ID:",
    first["candidate_id"]
)

print(
    "\nExperience:",
    first["experience"]
)

print(
    "\nProfile Text:\n"
)

print(
    first["text"][:1000]
)