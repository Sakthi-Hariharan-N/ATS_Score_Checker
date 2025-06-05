from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter
import re
from textblob import TextBlob
nltk.download('wordnet')
nltk.download('omw-1.4')

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

def lemmatize_words(word_list):
    lemmatizer = WordNetLemmatizer()
    return set(lemmatizer.lemmatize(word.lower()) for word in word_list)
    
def extract_keywords(text, n=20,custom_stopwords=None):
    '''
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([text])
    feature_array = vectorizer.get_feature_names_out()
    tfidf_sorting = np.argsort(tfidf_matrix.toarray()).flatten()[::-1]
    top_n = feature_array[tfidf_sorting][:n]
    
    
    words = re.findall(r'\b\w+\b', text.lower())
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(w) for w in words]
    # Remove stopwords (optional)
    
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    filtered = [w for w in lemmatized if w not in stop_words]
    # Get top N words by frequency
    from collections import Counter
    most_common = [w for w, count in Counter(filtered).most_common(n)]
    return set(most_common)
    return set(top_n)
    
    
    
    lemmatizer = WordNetLemmatizer()
    words = re.findall(r'\b\w+\b', text.lower())
    lemmatized = [lemmatizer.lemmatize(w) for w in words]
    # Remove custom stopwords if provided
    if custom_stopwords:
        filtered = [w for w in lemmatized if w not in custom_stopwords]
    else:
        filtered = lemmatized
    # Count frequency and get top N
    from collections import Counter
    most_common = [w for w, count in Counter(filtered).most_common(n)]
    return set(most_common)
    
    nltk.download('stopwords')
    lemmatizer = WordNetLemmatizer()
    # Tokenize and lowercase
    words = re.findall(r'\b\w+\b', text.lower())
    # Lemmatize
    lemmatized = [lemmatizer.lemmatize(w) for w in words]
    # Remove custom stopwords if provided
    if custom_stopwords:
        filtered = [w for w in lemmatized if w not in custom_stopwords]
    else:
        filtered = lemmatized
    # Count frequency and get top N
    freq = Counter(filtered)
    most_common = [w for w, count in freq.most_common(n)]
    return set(most_common)
    '''
    
    
    text_clean = re.sub(r'[^\w\s]', '', text.lower())
    # Remove multi-word stopword phrases first
    if custom_stopwords:
        for phrase in custom_stopwords:
            if ' ' in phrase:
                text_clean = text_clean.replace(phrase, '')
    # Use TextBlob for tokenization and lemmatization
    blob = TextBlob(text_clean)
    lemmatized = [word.lemmatize() for word in blob.words]
    # Remove single-word stopwords
    if custom_stopwords:
        filtered = [w for w in lemmatized if w not in custom_stopwords]
    else:
        filtered = lemmatized
    # Count frequency and get top N
    freq = Counter(filtered)
    most_common = [w for w, count in freq.most_common(n)]
    return set(most_common)
