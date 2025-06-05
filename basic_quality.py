import re
from textblob import TextBlob

def check_spelling(text):
    blob = TextBlob(text)
    words = [w for w in blob.words if w.isalpha()]
    misspelled = [w for w in words if w.correct().lower() != w.lower()]
    score = 100 - (len(misspelled) / len(words) * 100) if words else 100
    return round(score, 2), misspelled

def has_email(text):
    return bool(re.search(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', text))

def has_gmail(text):
    return bool(re.search(r'\b[\w\.-]+@gmail\.com\b', text, re.IGNORECASE))

def has_phone(text):
    return bool(re.search(r'(\+?\d{1,3})?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text))

def has_blog(text):
    return bool(re.search(r'(https?://\S+|www\.\S+)', text, re.IGNORECASE))

def has_section(text, section):
    return bool(re.search(rf'{section}', text, re.IGNORECASE))

def all_bullet_points(text):
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    bullet_lines = [line for line in lines if line.startswith(('-', '•', '*','➛','➣','➢', '•'))]
    # Consider "all" if at least 80% of lines are bullet points (adjust as needed)
    return (len(bullet_lines) / len(lines)) > 0.8 if lines else False

def basic_resume_quality(resume_text):
    #spelling_score, misspelled = check_spelling(resume_text)
    spelling_score, misspelled = check_spelling(resume_text)
    checks = {
        'has_email': has_email(resume_text),
        'has_gmail': has_gmail(resume_text),
        'has_phone': has_phone(resume_text),
        'has_blog': has_blog(resume_text),
        'has_summary': has_section(resume_text, 'summary'),
        'has_project': has_section(resume_text, 'project'),
        'has_certification': has_section(resume_text, 'certification'),
        'all_bullet_points': all_bullet_points(resume_text)
    }
    # Score: spelling (max 40), each present item (max 60/8 per item)
    section_points = 60 / len(checks)
    total_score = spelling_score * 0.4  # 40% weight for spelling
    for present in checks.values():
        if present:
            total_score += section_points
    total_score = min(round(total_score, 2), 100)

    report = {
        'spelling_score': spelling_score,
        'misspelled': misspelled,
        **checks,
        'suggestions': [],
        'total_score': total_score
    }
    # Suggestions
    if spelling_score < 95:
        report['suggestions'].append('Check for spelling errors.')
    if not report['has_email']:
        report['suggestions'].append('Add an email address.')
    if not report['has_phone']:
        report['suggestions'].append('Add a phone number.')
    if not report['has_summary']:
        report['suggestions'].append('Add a summary section.')
    if not report['has_project']:
        report['suggestions'].append('Add a project section.')
    if not report['has_certification']:
        report['suggestions'].append('Add a certification section.')
    if not report['all_bullet_points']:
        report['suggestions'].append('Use bullet points for most sentences in experience/skills.')
    return report
