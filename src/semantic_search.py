import faiss
import numpy as np

print("Loading FAISS index...")

index = faiss.read_index(
    "embeddings/candidate_index.faiss"
)

print("Loading JD embedding...")

query = np.load(
    "embeddings/jd_embedding.npy"
)

query = query.astype("float32")

faiss.normalize_L2(query)

print("Searching candidates...")

scores, ids = index.search(
    query,
    20
)

print("\nTop 20 Matches\n")

for i in range(20):

    print(
        f"Rank {i+1}",
        "| Position:",
        ids[0][i],
        "| Score:",
        round(float(scores[0][i]), 4)
    )