from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_match_score(resume_text, job_description):

    texts = [resume_text, job_description]

    # Create embeddings
    embeddings = model.encode(texts)

    # Compute similarity
    similarity = cosine_similarity(
        embeddings[0].reshape(1, -1),
        embeddings[1].reshape(1, -1)
    )[0][0]

    score = similarity * 100

    return float(round(score, 2))