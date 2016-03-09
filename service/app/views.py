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

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'course_results' in request.files:
        file = request.files['course_results']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('student_summary.html',
                                   title='Home', summary='hi')

    return render_template('failure.html',
                           title='Failure')
