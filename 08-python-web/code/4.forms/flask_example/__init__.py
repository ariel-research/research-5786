# Here, we add a secret key:
from flask import Flask
app = Flask(__name__)
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
from flask_example import routes
