# semantic_matcher.py

from sentence_transformers import SentenceTransformer, util

# Load model only once
model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_similarity_score(jd_keywords, resume_keywords, threshold=0.7):
    """
    Returns a list of (jd_word, resume_word, score) tuples where score >= threshold.
    """
    jd_keywords = list(jd_keywords)
    resume_keywords = list(resume_keywords)
    jd_emb = model.encode(jd_keywords, convert_to_tensor=True)
    resume_emb = model.encode(resume_keywords, convert_to_tensor=True)
    
    matched_pairs = []
    for i, jd_word in enumerate(jd_keywords):
        similarities = util.cos_sim(jd_emb[i], resume_emb)[0]
        best_idx = similarities.argmax()
        best_score = similarities[best_idx].item()
        if best_score >= threshold:
            matched_pairs.append((jd_word, resume_keywords[best_idx], best_score))
    return matched_pairs
