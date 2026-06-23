import json

with open(
    "output/candidate_profiles.jsonl",
    "r",
    encoding="utf8"
) as f:

    first = json.loads(next(f))

print(first.keys())

print("\nFULL RECORD:\n")

print(first)