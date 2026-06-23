import faiss

index = faiss.read_index(
    "embeddings/candidate_index.faiss"
)

print(
    "Total vectors:",
    index.ntotal
)
