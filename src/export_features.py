import json
import pandas as pd

AI_KEYWORDS = [
    "llm",
    "fine-tuning",
    "lora",
    "rag",
    "embedding",
    "retrieval",
    "vector",
    "faiss",
    "pinecone",
    "milvus",
    "weaviate",
    "qdrant",
    "nlp",
    "transformer",
    "bert",
    "gpt"
]

rows = []

with open(
    "output/candidate_profiles.jsonl",
    "r",
    encoding="utf8"
) as f:

    for line in f:

        data = json.loads(line)

        text = data["text"].lower()

        ai_skill_score = sum(
            keyword in text
            for keyword in AI_KEYWORDS
        )

        rows.append({
            "candidate_id": data["candidate_id"],
            "experience": data["experience"],
            "ai_skill_score": ai_skill_score
        })

df = pd.DataFrame(rows)

df.to_csv(
    "output/features.csv",
    index=False
)

print(df.head())
print("\nFeatures Exported Successfully")