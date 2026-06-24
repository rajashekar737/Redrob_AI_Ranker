import json
from tqdm import tqdm

INPUT_FILE = "data/candidates.jsonl"
OUTPUT_FILE = "output/candidate_profiles.jsonl"

count = 0

with open(INPUT_FILE, "r", encoding="utf8") as fin, \
     open(OUTPUT_FILE, "w", encoding="utf8") as fout:

    for line in tqdm(fin):

        candidate = json.loads(line)

        headline = candidate["profile"].get(
            "headline", ""
        )

        summary = candidate["profile"].get(
            "summary", ""
        )

        skills = " ".join([
            s["name"]
            for s in candidate["skills"]
        ])

        career = " ".join([
            job["description"]
            for job in candidate["career_history"]
        ])

        text = f"""
        {headline}

        {summary}

        Skills:
        {skills}

        Career:
        {career}
        """

        profile = {
    "candidate_id":
    candidate["candidate_id"],

    "text":
    text,

    "experience":
    candidate["profile"][
        "years_of_experience"
    ],

    "redrob_signals":
    candidate.get(
        "redrob_signals",
        {}
    )
}
        fout.write(
            json.dumps(profile)
            + "\n"
        )

        count += 1

print(
    f"Created {count} profiles"
)