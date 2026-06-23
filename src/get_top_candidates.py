import faiss
import numpy as np

index = faiss.read_index(
    "embeddings/candidate_index.faiss"
)

query = np.load(
    "embeddings/jd_embedding.npy"
).astype("float32")

candidate_ids = np.load(
    "embeddings/candidate_ids.npy",
    allow_pickle=True
)

faiss.normalize_L2(query)

scores, ids = index.search(
    query,
    20
)

print("\nTop 20 Candidates\n")

for rank in range(20):

    candidate_id = candidate_ids[
        ids[0][rank]
    ]

    score = scores[0][rank]

    print(
        rank + 1,
        candidate_id,
        round(float(score), 4)
    )