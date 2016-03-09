#!flask/bin/python3
from app import app

app.debug = True
app.run(port=5006)
