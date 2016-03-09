import os

SERVICE_BASE_DIR = os.path.dirname(os.path.realpath(__file__))

UPLOAD_FOLDER = os.path.join(SERVICE_BASE_DIR, 'app', 'tmp')
ALLOWED_EXTENSIONS = set(['pdf'])
