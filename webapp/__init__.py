# Demonstrating creating a training 
# application using Tensorflow.
#
# A web app to host the model
#
# Author:  Anshul Kharbanda
# Created: 8 - 2 - 2020
from flask import Flask, render_template
from .form import DataForm

# Application
app = Flask(__name__)
app.config.from_object('config')

# Main page route
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Main page of the application
    """
    form = DataForm()
    return render_template('index.html', form=form)