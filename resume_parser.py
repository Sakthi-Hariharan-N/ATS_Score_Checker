import re
from pdfminer.high_level import extract_text
import docx2txt

def parse_resume(file):
    if file.filename.endswith('.pdf'):
        from pdfminer.high_level import extract_text
        raw_text = extract_text(file.stream)
    elif file.filename.endswith('.docx'):
        import docx2txt
        raw_text = docx2txt.process(file)
    else:
        raw_text = ""
    # Clean the extracted text
    return clean_text(raw_text)
        
        

def analyze_resume_structure(resume_text):
    '''
    required_sections = ['experience', 'education', 'skills']
    found_sections = []
    for section in required_sections:
        if re.search(rf'{section}', resume_text, re.IGNORECASE):
            found_sections.append(section)
    return {
        'missing_sections': list(set(required_sections) - set(found_sections)),
        'formatting_issues': check_formatting(resume_text)
    }'''
    required_sections = ['experience', 'education', 'skills','project',]
    found_sections = []
    resume_text_lower = resume_text.lower()
    for section in required_sections:
        if section.lower() in resume_text_lower:
            found_sections.append(section)
    return {
        'missing_sections': list(set(required_sections) - set(found_sections)),
        'formatting_issues': check_formatting(resume_text)
    }

def check_formatting(text):
    issues = []
    # Ignore common resume Unicode characters like bullets, en-dash, em-dash, smart quotes, etc.
    allowed = "•–-‘’“”…"
    if re.search(rf'[^\x00-\x7F{re.escape(allowed)}]', text):
        issues.append('Special characters detected')
    return issues
    
def clean_text(text):
    # Replace common Unicode bullets and dashes with ASCII equivalents
    text = text.replace('•', '-').replace('–', '-').replace('-', '-')
    # Replace smart quotes with normal quotes
    text = text.replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'")
    # Remove other non-ASCII characters
    text = re.sub(r'[^\x00-\x7F]', '', text)
    return text
