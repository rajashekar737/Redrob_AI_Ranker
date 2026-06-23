import numpy as np

embeddings = np.load(
    "embeddings/candidate_embeddings.npy"
)

print("Shape:", embeddings.shape)
print("Dtype:", embeddings.dtype)