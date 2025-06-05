from flask import Flask, render_template, request
from resume_parser import parse_resume, analyze_resume_structure
from jd_analyzer import extract_keywords
from similarity_checker import calculate_match
from basic_quality import basic_resume_quality
#from flask_ngrok import run_with_ngrok
#from pyngrok import ngrok

app = Flask(__name__)
#run_with_ngrok(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    structure_report = None
    basic_report = None
    if request.method == 'POST':
        jd_text = request.form.get('job_description', '')
        if not jd_text.strip():
            warning = "Job Description cannot be empty or just spaces."
        else:
            resume_file = request.files.get('resume')
            if resume_file:
                resume_text = parse_resume(resume_file)
                structure_report = analyze_resume_structure(resume_text)
                #basic_report = basic_resume_quality(resume_text)
                if not structure_report['missing_sections']:
                    #result = calculate_match(jd_text, resume_text)
                    result = calculate_match(jd_text,resume_text,bonus_keywords=['hackathons','certifications',], bonus_value=10,extra_score_value=5)
                
                
    
                
            
    return render_template('index.html', result=result, structure=structure_report, basic_report=basic_report)
@app.route('/basic', methods=['GET', 'POST'])
def basic():
    basic_report = None
    result = None
    if request.method == 'POST':
        resume_file = request.files.get('resume')
        if resume_file:
            resume_text = parse_resume(resume_file)
            #from basic_quality import basic_resume_quality
            basic_report = basic_resume_quality(resume_text)
    return render_template('index.html', basic_report=basic_report, result=result)
if __name__ == '__main__':
    #public_url = ngrok.connect(5000)
    app.debug=True
    app.run()
