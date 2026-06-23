import json
import numpy as np
from tqdm import tqdm
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)

texts = []
candidate_ids = []

with open(
    "output/candidate_profiles.jsonl",
    "r",
    encoding="utf8"
) as f:

    for line in tqdm(f):

        record = json.loads(line)

        texts.append(
            record["text"]
        )

        candidate_ids.append(
            record["candidate_id"]
        )

print("Generating embeddings...")

embeddings = model.encode(
    texts,
    batch_size=128,
    show_progress_bar=True,
    convert_to_numpy=True
)

np.save(
    "embeddings/candidate_embeddings.npy",
    embeddings
)

np.save(
    "embeddings/candidate_ids.npy",
    np.array(candidate_ids)
)

print(
    "Embeddings Saved Successfully"
)