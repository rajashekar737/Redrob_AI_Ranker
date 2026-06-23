import faiss
import numpy as np
import pandas as pd

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
    500
)

rows = []

for rank in range(500):

    rows.append({
        "candidate_id":
        candidate_ids[ids[0][rank]],

        "semantic_score":
        float(scores[0][rank])
    })

df = pd.DataFrame(rows)

df.to_csv(
    "output/top500_semantic.csv",
    index=False
)

print("Top 500 Saved")