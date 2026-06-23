with open(
    "output/jd_text.txt",
    "r",
    encoding="utf8"
) as f:

    jd = f.read().lower()

skills = [
    "python",
    "retrieval",
    "ranking",
    "embeddings",
    "vector",
    "faiss",
    "pinecone",
    "milvus",
    "weaviate",
    "qdrant",
    "llm",
    "fine-tuning",
    "lora",
    "evaluation",
    "ndcg",
    "mrr",
    "map"
]

found_skills = []

for skill in skills:

    if skill in jd:
        found_skills.append(skill)

print("\nSkills Found In JD:\n")

for skill in found_skills:
    print(skill)