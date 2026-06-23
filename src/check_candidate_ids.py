import numpy as np

ids = np.load(
    "embeddings/candidate_ids.npy",
    allow_pickle=True
)

print("Total IDs:", len(ids))
print("First ID:", ids[0])
print("Last ID:", ids[-1])