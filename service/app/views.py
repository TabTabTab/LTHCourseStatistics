import app.tools.course_statistics as course_statistics
from app.tools.file_utils import create_unique_filename

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

@app.route('/course_summary', methods=['GET', 'POST'])
def course_summary():
    if request.method == 'POST' and 'course_results' in request.files:
        pdf_file = request.files['course_results']
        if pdf_file and allowed_file(pdf_file.filename):
            original_filename = secure_filename(pdf_file.filename)
            unique_filename = create_unique_filename(app.config['UPLOAD_FOLDER'],
                                                     original_filename)
            pdf_file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
            pdf_abs_path = os.path.abspath(os.path.join(app.config['UPLOAD_FOLDER'],
                                                        unique_filename))
            student_course_summary = None
            try:
                student_course_summary = course_statistics.get_course_statistics(
                    pdf_abs_path)
            except course_statistics.ReadPDFException as e:
                return render_template('failure.html',
                                       title='Failure',
                                       redirect=True,
                                       message='It seems the file you provided cound not be read as a PDF.')

            return render_template('student_summary_%s.html' % student_course_summary.language,
                                   title='Summary',
                                   student_summary=student_course_summary)

    return redirect(url_for('index'))
