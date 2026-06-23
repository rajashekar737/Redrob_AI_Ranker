import json
from tqdm import tqdm

INPUT_FILE = "data/candidates.jsonl"
OUTPUT_FILE = "output/features.jsonl"

AI_SKILLS = {
    "retrieval",
    "ranking",
    "embedding",
    "embeddings",
    "llm",
    "fine-tuning",
    "lora",
    "milvus",
    "faiss",
    "pinecone",
    "weaviate",
    "qdrant",
    "vector",
    "nlp"
}

count = 0

with open(INPUT_FILE, "r", encoding="utf8") as fin, \
     open(OUTPUT_FILE, "w", encoding="utf8") as fout:

    for line in tqdm(fin):

        c = json.loads(line)

        candidate_id = c["candidate_id"]

        experience = c["profile"][
            "years_of_experience"
        ]

        skills = [
            s["name"].lower()
            for s in c["skills"]
        ]

        skill_count = len(skills)

        ai_skill_score = 0

        for skill in skills:

            for keyword in AI_SKILLS:

                if keyword in skill:
                    ai_skill_score += 1

        signals = c["redrob_signals"]

        behavior_score = (
            signals["profile_completeness_score"]/100
            + signals["recruiter_response_rate"]
            + signals["interview_completion_rate"]
            + max(
                signals["github_activity_score"],
                0
            )/100
        ) / 4

        feature_record = {
            "candidate_id": candidate_id,
            "experience": experience,
            "skill_count": skill_count,
            "ai_skill_score": ai_skill_score,
            "behavior_score":
                round(behavior_score,4)
        }

        fout.write(
            json.dumps(feature_record)
            + "\n"
        )

        count += 1

print(
    f"Generated Features For {count} Candidates"
)