import faiss
import numpy as np

print("Loading embeddings...")

embeddings = np.load(
    "embeddings/candidate_embeddings.npy"
)

embeddings = embeddings.astype(
    "float32"
)

faiss.normalize_L2(
    embeddings
)

dimension = embeddings.shape[1]

print(
    "Creating FAISS index..."
)

index = faiss.IndexFlatIP(
    dimension
)

index.add(
    embeddings
)

faiss.write_index(
    index,
    "embeddings/candidate_index.faiss"
)

print(
    f"Index Created: {index.ntotal} vectors"
)