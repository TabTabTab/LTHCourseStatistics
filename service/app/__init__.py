from flask import Flask

from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
from app import views
