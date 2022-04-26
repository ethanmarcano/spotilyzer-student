import os

from flask import Flask

app_path = os.path.dirname(__file__)
app = Flask(__name__, static_folder=app_path+'/static')
app.config['SECRET_KEY'] = 'ALHqC7dkzjNdyZdYBMmTzQ'

from application import routes