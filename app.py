from flask import Flask, render_template, request

app = Flask(__name__)

# Project Data
projects_data = [
    {
        'id': 'course-management',
        'title': 'Course Management Web Application',
        'description': 'A web-based application designed to manage university courses, schedules, and dashboards, developed as an academic capstone project. This comprehensive solution streamlines the administrative tasks associated with course planning and student management.',
        'tags': ['HTML', 'CSS', 'JavaScript', 'Python'],
        'images': ['projet-memoire-dashbord1.png', 'projet-memoire-dashbord2.png', 'projet-memoire-gestion1.png', 'projet-memoire-gestion2.png'],
        'github': 'https://github.com/BenDiya07/Projet-memoire'
    },
    {
        'id': 'payroll-management',
        'description': 'Comprehensive academic payroll management application: employees, advances, deductions, reports, authentication, and dashboard. Designed to streamline HR processes and ensure accurate salary calculations.',
        'tags': ['HTML', 'CSS', 'JavaScript', 'Python', 'MySQL'],
        'images': ['snel-payroll1.png', 'snel-payroll2.png', 'snel-payroll3.png', 'snel-payroll4.png'],
        'github': 'https://github.com/BenDiya07/Payroll-Management-System-SNEL-Academic-Project-'
    },
    {
        'id': 'jupython RDC',
        'title': 'Jupython Plateforme Frontend Éducative',
        'description': 'Interface frontend d’une plateforme éducative moderne comprenant des pages académiques, un catalogue de cours, un système de classement et des pages institutionnelles, avec une approche responsive et centrée utilisateur',
        'tags': ['HTML', 'Sass', 'JavaScript', 'Responsive UI'],
        'images': ['jupython-dashbord1.png', 'jupython-dashbord2.png', 'jupython-dashbord3.png', ],
        'github': 'https://github.com/Jupython-RDC/jupython-frontend'
    }
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=projects_data)

@app.route('/project/<project_id>')
def project_detail(project_id):
    project = next((p for p in projects_data if p['id'] == project_id), None)
    if project:
        return render_template('project_detail.html', project=project)
    return "Project not found", 404

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
