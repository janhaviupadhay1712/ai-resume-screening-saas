import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

dimension = 384  # embedding size

index = faiss.IndexFlatL2(dimension)

resume_texts = []


def add_resumes(texts):
    global resume_texts

    embeddings = model.encode(texts)
    embeddings = np.array(embeddings).astype("float32")

    index.add(embeddings)

    resume_texts.extend(texts)


def search_resumes(job_description, top_k=3):

    query_embedding = model.encode([job_description])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for i, idx in enumerate(indices[0]):
        results.append({
            "resume_id": int(idx),
            "score": float(100 - distances[0][i])
        })

    return results