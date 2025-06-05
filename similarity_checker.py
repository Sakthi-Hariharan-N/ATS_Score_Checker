from jd_analyzer import extract_keywords
import re
from semantic_matcher import semantic_similarity_score
CUSTOM_JD_STOPWORDS = {
    # Basic pronouns/prepositions
    "we", "our", "you", "your", "us", "they", "their", "them", "this", "that", "these", "those",
    
    # Modal verbs
    "will", "would", "should", "shall", "must", "might", "may", "can", "could",
    
    # Common JD action verbs
    "seeking", "looking", "need", "needs", "required", "requires", "requiring", "expect", "expects",
    "drive", "driven", "deliver", "delivers", "develop", "develops", "ensure", "ensures", "maintain",
    "maintains", "provide", "provides", "support", "supports", "work", "works", "join", "joins",
    
    # Corporate jargon
    "synergy", "leverage", "paradigm", "disrupt", "innovate", "innovation", "ecosystem", "stakeholder",
    "value-added", "best-in-class", "cutting-edge", "end-to-end", "holistic", "scalable", "robust",
    
    # JD-specific phrases
    "the ability to", "part of", "in addition to", "as well as", "in order to", "prior experience in",
    "strong understanding of", "familiar with", "working knowledge of", "knowledge of", "experience with",
    
    # Generic qualifications
    "preferred", "preferably", "plus", "bonus", "advantage", "asset", "nice to have", "would be a plus",
    
    # Education terms
    "degree", "bachelor's", "master's", "phd", "diploma", "certification", "qualified", "accredited",
    
    # Soft skills
    "team player", "self-starter", "detail-oriented", "results-driven", "multitask", "multitasking",
    "time management", "problem-solving", "critical thinking", "interpersonal skills",
    
    # Redundant terms
    "responsibilities", "duties", "tasks", "role", "position", "job", "opening", "opportunity",
    "candidate", "applicant", "successful candidate", "ideal candidate", "individual",
    
    # Add your existing words below
    "is", "for", "responsible", "be", "the", "a", "an", "to", "and", "or", "in", "on", "with", 
    "of", "as", "by", "at", "from", "who", "work", "team", "join", "role", "position", 
    "required", "preferred", "skills", "requirements", "qualifications", "experience", 
    "knowledge", "ability", "good", "strong", "excellent", "willingness", "looking for",
    "basic", "familiarity", "curious", "player", "like", "attitude", "exposure", "mindset",
    "tool", "requirements", "qualifications",
}
def has_gmail(text):
    return bool(re.search(r'\b[\w\.-]+@gmail\.com\b', text, re.IGNORECASE))

def has_blog_or_url(text):
    return bool(re.search(r'(https?://\S+|www\.\S+)', text, re.IGNORECASE))

def calculate_match(jd_text, resume_text, bonus_keywords=None, bonus_value=10, extra_score_value=5,semantic_bonus=5):
    '''
    jd_keywords = extract_keywords(jd_text)
    resume_keywords = extract_keywords(resume_text)
    common = jd_keywords & resume_keywords
    missing = jd_keywords - resume_keywords
    match_score = (len(common) / len(jd_keywords) * 100) if jd_keywords else 0
    return {
        'match_score': round(match_score, 2),
        'common_keywords': list(common),
        'missing_keywords': list(missing)
    }
    
    
    jd_keywords = extract_keywords(jd_text, n=100, custom_stopwords=CUSTOM_JD_STOPWORDS)
    resume_keywords = extract_keywords(resume_text, n=100)
    common = jd_keywords & resume_keywords
    missing = jd_keywords - resume_keywords
    match_score = (len(common) / len(jd_keywords) * 100) if jd_keywords else 0
    return {
        'match_score': round(match_score, 2),
        'common_keywords': list(common),
        'missing_keywords': list(missing)
    }
    '''
    #def calculate_match():
    jd_keywords = extract_keywords(jd_text, n=100, custom_stopwords=CUSTOM_JD_STOPWORDS)
    #resume_keywords = extract_keywords(resume_text, n=100)
    resume_keywords = list(extract_keywords(resume_text, n=100))
    common = set(jd_keywords) & set(resume_keywords)
    missing = set(jd_keywords) - set(resume_keywords)
    match_score = (len(common) / len(jd_keywords) * 100) if jd_keywords else 0

    # Bonus mechanism
    '''
    bonus_applied = []
    if bonus_keywords:
        for bonus_kw in bonus_keywords:
            if bonus_kw in jd_keywords and bonus_kw in resume_keywords:
                match_score += bonus_value
                bonus_applied.append(bonus_kw)
    # Cap the score at 100%
    match_score = min(match_score, 100)

    return {
        'match_score': round(match_score, 2),
        'common_keywords': list(common),
        'missing_keywords': list(missing),
        'bonus_applied': bonus_applied
    }'''
    bonus_applied = []
    if bonus_keywords:
        for bonus_kw in bonus_keywords:
            if bonus_kw in jd_keywords and bonus_kw in resume_keywords:
                match_score += bonus_value
                bonus_applied.append(bonus_kw)


    #Semantic matching
    semantic_matches = semantic_similarity_score(jd_keywords, resume_keywords, threshold=0.7)
    semantic_applied = []
    for jd_word, resume_word, score in semantic_matches:
        if jd_word not in common and jd_word not in bonus_applied:
            match_score += semantic_bonus
            semantic_applied.append((jd_word, resume_word, round(score, 2)))
    #match_score = min(match_score, 100)
    # Extra score for Gmail and blog/URL
    extra_applied = []
    if has_gmail(resume_text):
        match_score += extra_score_value
        extra_applied.append("gmail")
    if has_blog_or_url(resume_text):
        match_score += extra_score_value
        extra_applied.append("blog/url")

    # Cap the score at 100%
    match_score = min(match_score, 100)

    return {
        'match_score': round(match_score, 2),
        'common_keywords': list(common),
        'missing_keywords': list(missing),
        'bonus_applied': bonus_applied,
        'extra_applied': extra_applied,
        'semantic_applied': semantic_applied,
    }
