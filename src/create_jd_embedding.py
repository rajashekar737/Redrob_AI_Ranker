import numpy as np
from sentence_transformers import SentenceTransformer

print("Loading JD...")

with open(
    "output/jd_text.txt",
    "r",
    encoding="utf8"
) as f:
    jd = f.read()

print("Loading model...")

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

jd_embedding = model.encode(
    [jd],
    convert_to_numpy=True
)

np.save(
    "embeddings/jd_embedding.npy",
    jd_embedding
)

print("JD Embedding Saved")
print("Shape:", jd_embedding.shape)