# ATS_Score_Checker
User Can Checkout their resume score based on job description.
ATS Resume & Quality Checker
A modern web application to analyze and score resumes for job matching and quality, powered by Flask, NLP, and semantic similarity.

Features
ATS Resume Checker:
Upload your resume and a job description to see your match score, keyword overlap, and receive bonus points for semantic matches and extra details.

Basic Resume Quality Check:
Upload your resume to get a quality score based on spelling, presence of key sections (email, phone, summary, projects, certifications), and formatting (e.g., bullet points).

Semantic Matching:
Uses SentenceTransformer to recognize synonyms and related skills, not just exact keyword matches.

User-Friendly Interface:
Tabbed UI for easy navigation between job matching and basic quality checks.

Spelling & Section Analysis:
Get suggestions to improve your resume’s structure and content.

Getting Started
1. Clone the Repository
bash
git clone https://github.com/yourusername/ats-resume-checker.git
cd ats-resume-checker
2. Install Dependencies
Make sure you have Python 3.8+ installed.

bash
pip install -r requirements.txt
3. Run the Application
bash
python app.py
Visit http://localhost:5000 in your browser.

Project Structure
text
├── app.py

├── requirements.txt

├── templates/
│   └── index.html

├── resume_parser.py

├── jd_analyzer.py

├── similarity_checker.py

├── semantic_matcher.py

├── basic_quality.py

How It Works
ATS Resume Checker Tab:
Paste a job description and upload your resume. The app extracts keywords, checks for overlaps, and uses semantic similarity to find related skills for a comprehensive match score.

Basic Resume Quality Check Tab:
Just upload your resume. The app checks for spelling, contact details, key sections, and bullet point usage, then gives you a total quality score and improvement suggestions.

Technologies Used
Flask

python-docx

pdfplumber

TextBlob

SentenceTransformers

PyTorch


Acknowledgements
Inspired by modern ATS and resume parsing tools.

Uses open-source NLP models and libraries.
