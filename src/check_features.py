import json

with open(
    "output/features.jsonl",
    "r",
    encoding="utf8"
) as f:

    first = json.loads(
        f.readline()
    )

for key, value in first.items():

    print(
        key,
        ":",
        value
    )