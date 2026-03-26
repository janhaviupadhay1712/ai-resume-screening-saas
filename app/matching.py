from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_match_score(resume_text, job_description):

    texts = [resume_text, job_description]

    # Creating embeddings
    embeddings = model.encode(texts)

    # Computing similarity
    similarity = cosine_similarity(
        embeddings[0].reshape(1, -1),
        embeddings[1].reshape(1, -1)
    )[0][0]

    score = similarity * 100

    return float(round(score, 2))

def rank_resumes(resume_texts, job_description):

    job_embedding = model.encode([job_description])[0]

    scores = []

    for i, resume in enumerate(resume_texts):
        resume_embedding = model.encode([resume])[0]

        similarity = cosine_similarity(
            [resume_embedding],
            [job_embedding]
        )[0][0]

        scores.append({
            "resume_id": i,
            "score": float(round(similarity * 100, 2))
        })

    #highest score sorting
    ranked = sorted(scores, key=lambda x: x["score"], reverse=True)

    return ranked