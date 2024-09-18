import os
import PyPDF2
import nltk
from flask import Flask, request, jsonify, render_template
from collections import Counter

nltk.download('punkt') 

app = Flask(__name__)

def extract_text_from_pdf(pdf):
    reader = PyPDF2.PdfReader(pdf)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

def parse_resume(text):
    words = nltk.word_tokenize(text)
    words = [word for word in words if word.isalpha()]  # Remove punctuation
    word_freq = Counter(words)
    return word_freq

def score_resume(parsed_data, full_text):
    skills = ['c', 'java', 'python', 'cpp', '.net', 'sql', 'dart', 'c#', 'ruby', 'javascript', 'c++']
    technologies = ['salesforce', 'aws', 'full stack', 'aiml', 'flattur', 'cloud','rpa', 'gaming', 'arvr', 'ui/ux', 'robotics', 'data analytics','oracle', 'dbms', 'networking', 'redhat', 'servicenow']

    score = 2
    improvements = []
    # skills section
    missing_skills = []
    found_skills = 0
    for skill in skills:
        if skill.lower() in (word.lower() for word in parsed_data):
            score += 3
            found_skills += 1
        else:
            missing_skills.append(skill)
    if found_skills <= 2:
        if missing_skills:
            missing_skills_examples = ', '.join(missing_skills[:3])  # Take up to the first three missing skills as examples
            improvements.append(f"\u2022 Enhance your score by including languages are proficient in.. For example: {missing_skills_examples}")




    # tehnology section
    missing_skills = []
    found_skills = 0
    for I in technologies:
        if I.lower() in (word.lower() for word in parsed_data):
            score += 4
            found_skills += 1
        else:
            missing_skills.append(I)
    if found_skills <= 2:
        if missing_skills:
            missing_skills_examples = ', '.join(missing_skills[:3])  # Take up to the first three missing skills as examples
            improvements.append(f"\u2022 Adding technologies you are familiar with could help boost your score. For example: {missing_skills_examples}.")


    # Frameworks
    frameworks = ['reactjs', 'nodejs', 'flask', 'spring', 'springboot', 'angular', 'express']
    missing_skills = []
    found_skills = 0
    for I in frameworks:
        if I.lower() in (word.lower() for word in parsed_data):
            score += 3
            found_skills += 1
        else:
            missing_skills.append(I)
    if found_skills <= 2:
        if missing_skills:
            missing_skills_examples = ', '.join(missing_skills[:3])  # Take up to the first three missing skills as examples
            improvements.append(f"\u2022 To improve your score, try to add some Frameworks if you are familiar with them. For example: {missing_skills_examples}.")

    # Databases
    databases = ['MongoDB', 'MySQL', 'Oracle', 'DBMS']
    missing_skills = []
    found_skills = 0
    for I in databases:
        if I.lower() in (word.lower() for word in parsed_data):
            score += 2
            found_skills += 1
        else:
            missing_skills.append(I)
    if found_skills <= 2:
        if missing_skills:
            missing_skills_examples = ', '.join(missing_skills[:3])  # Take up to the first three missing skills as examples
            improvements.append(f"\u2022 Consider including any databases you are experienced with to enhance your score.. For example: {missing_skills_examples}.")


    # operating system
    operating_systems = ['linux', 'os', 'windows', 'ios']
    missing_skills = []
    found_skills = 0
    for I in operating_systems  :
        if I.lower() in (word.lower() for word in parsed_data):
            score += 3
            found_skills += 1
        else:
            missing_skills.append(I)
    if found_skills <= 2:
        if missing_skills:
            missing_skills_examples = ', '.join(missing_skills[:3])  # Take up to the first three missing skills as examples
            improvements.append(f"\u2022 Try adding any operating systems you have knowledge of. For example: {missing_skills_examples}.")



    # internships

    internship = ['internship', 'intern', 'summer intern', 'trainee', 'industrial training', 'internship program', 'co-op', 'graduate intern', 'student intern', 'apprenticeship', 'intern experience', 
    'internship position', 'internship role', 'internship opportunity', 'internship project', 'practicum']
    missing_skills = []
    found_skills = 0
    for I in internship:
        if I.lower() in (word.lower() for word in parsed_data):
            score += 4
            found_skills += 1
        else:
            missing_skills.append(I)
    if found_skills <= 2:
        if missing_skills:
            missing_skills_examples = ', '.join(missing_skills[:3])  # Take up to the first three missing skills as examples
            improvements.append(f"\u2022 To improve your score, you might want to list any internships you have experience with. For example: {missing_skills_examples}.")



    # projects
    projects = ['project', 'project management', 'project lead', 'team leader', 'project coordinator', 'project planning', 'project execution', 'project deliverables', 'project lifecycle', 'project implementation', 'project development', 'project documentation', 'project timeline', 'project strategy', 'project goals', 'project scope', 'project objectives', 'project outcomes', 'project milestones', 'project budget', 'project resources', 'project tasks', 'project team', 'project review', 'project analysis', 'project completion', 'project challenges', 'project collaboration', 'project results']
    missing_skills = []
    found_skills = 0
    for I in projects:
        if I.lower() in (word.lower() for word in parsed_data):
            score += 4
            found_skills += 1
        else:
            missing_skills.append(I)
    if found_skills <= 2:
        if missing_skills:
            missing_skills_examples = ', '.join(missing_skills[:3])  # Take up to the first three missing skills as examples
            improvements.append(f"\u2022 To improve your score, try to add some projects if you are familiar with them. For example: {missing_skills_examples}.")

    # experiance
    experience_keywords = ['experience', 'professional experience', 'work experience', 'previous experience', 'hands-on experience', 'field experience', 'practical experience', 'industry experience', 'relevant experience', 'expertise', 'background', 'job experience', 'employment history', 'career experience', 'experience in', 'experience with', 'project experience', 'training', 'accomplishments', 'achievements', 'roles and responsibilities', 'job role', 'job duties', 'employment experience', 'work history', 'practical knowledge']
    missing_skills = []
    found_skills = 0
    for I in experience_keywords:
        if I.lower() in (word.lower() for word in parsed_data):
            score += 4
            found_skills += 1
        else:
            missing_skills.append(I)
    if found_skills <= 2:
        if missing_skills:
            missing_skills_examples = ', '.join(missing_skills[:3])  # Take up to the first three missing skills as examples
            improvements.append(f"\u2022 Including experiances you are well-acquainted with can help increase your score. For example: {missing_skills_examples}.")


    # platforms
    coding_platforms = ['LeetCode', 'HackerRank', 'CodeChef', 'GeeksforGeeks', 'TopCoder', 'Codeforces', 'AtCoder', 'Kaggle', 'Project Euler', 'SPOJ', 'UVa Online Judge', 'Exercism', 'CodinGame', 'InterviewBit']
    missing_skills = []
    found_skills = 0
    for I in coding_platforms:
        if I.lower() in (word.lower() for word in parsed_data):
            score += 4
            found_skills += 1
        else:
            missing_skills.append(I)
    if found_skills <= 2:
        if missing_skills:
            missing_skills_examples = ', '.join(missing_skills[:3])  # Take up to the first three missing skills as examples
            improvements.append(f"\u2022 To improve your score, try to add some Databases if you are familiar with them. For example: {missing_skills_examples}.")





    return score, improvements
          
@app.route('/')
def upload_form():
    return render_template('index.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'resume' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['resume']
    if file.filename == '':
        return jsonify({"error": "No file selected for uploading"}), 400
    
    if file and file.filename.endswith('.pdf'):
        text = extract_text_from_pdf(file)
        parsed_data = parse_resume(text)
        score, improvements = score_resume(parsed_data, text)
        return jsonify({"score": score, "improvements": improvements})
    else:
        return jsonify({"error": "Invalid file type. Only PDFs are allowed."}), 400

@app.route('/evaluate', methods=['POST'])
def evaluate():
    content = request.get_json()
    resume_text = content.get('resume_text')
    requirements = content.get('requirements')
    parsed_data = parse_resume(resume_text)
    match_score = evaluate_requirements(parsed_data, requirements)
    return jsonify({"match_score": match_score})

if __name__ == "__main__":
    app.run(debug=True)