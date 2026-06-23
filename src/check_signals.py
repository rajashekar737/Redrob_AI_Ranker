import json

with open(
    "data/candidates.jsonl",
    "r",
    encoding="utf8"
) as f:

    first = json.loads(
        f.readline()
    )

signals = first["redrob_signals"]

print("Behavioral Signals:\n")

for key, value in signals.items():
    print(f"{key}: {value}")