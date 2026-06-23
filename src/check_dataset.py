count = 0

with open(
    "data/candidates.jsonl",
    "r",
    encoding="utf8"
) as f:

    for line in f:
        count += 1

print("Total Candidates:", count)