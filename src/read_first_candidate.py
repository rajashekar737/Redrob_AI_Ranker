import json

with open(
    "data/candidates.jsonl",
    "r",
    encoding="utf8"
) as f:

    first_line = f.readline()

candidate = json.loads(first_line)

print(candidate.keys())

print("\nCandidate ID:")
print(candidate["candidate_id"])

print("\nHeadline:")
print(candidate["profile"]["headline"])

print("\nExperience:")
print(candidate["profile"]["years_of_experience"])