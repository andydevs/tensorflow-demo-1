# Demonstrating creating a training 
# application using Tensorflow.
#
# A web app to host the model
#
# Author:  Anshul Kharbanda
# Created: 8 - 2 - 2020
from flask import Flask, render_template

# Application
app = Flask(__name__)

# Main page route
@app.route('/')
def index():
    """
    Main page of the application
    """
    return render_template('index.html')