import os
from flask import Flask

#create an instance of a flask app and indicating its location
app_path = os.path.dirname(__file__)
app = Flask(__name__, static_folder=app_path+'/static')
#creating a secret key for security
app.config['SECRET_KEY'] = 'ALHqC7dkzjNdyZdYBMmTzQ'


from application import routes