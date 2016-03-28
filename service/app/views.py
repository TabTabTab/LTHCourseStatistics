
import app.tools.course_statistics as course_statistics

from flask import render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug import secure_filename
from app import app
import os

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')

@app.route('/info')
def info():
    return render_template('info.html',
                           title='Information')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'course_results' in request.files:
        pdf_file = request.files['course_results']
        if pdf_file and allowed_file(pdf_file.filename):
            filename = secure_filename(pdf_file.filename)
            pdf_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            pdf_abs_path = os.path.abspath(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            student_course_summary = course_statistics.get_course_statistics(
                pdf_abs_path)
            return render_template('student_summary_%s.html' % student_course_summary.language,
                                   title='Summary',
                                   student_summary=student_course_summary)

    return render_template('failure.html',
                           title='Failure')
