# Demonstrating creating a training 
# application using Tensorflow.
#
# A web app to host the model
#
# Author:  Anshul Kharbanda
# Created: 8 - 2 - 2020
from flask import Flask, render_template
from .form import DataForm
from training.data import meta, feature_encoder, label_encoder
from tensorflow.keras.models import load_model
from re import sub
import numpy as np
import config

# Application
app = Flask(__name__)
app.config.from_object('config')

# Model
model = load_model(f'{config.model_directory}/{config.model_filename}')

# Main page route
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Main page of the application
    """
    # Create a form
    form = DataForm()
    message = None
    message_color = None

    # Only if we're submitting a prediction
    if form.validate_on_submit():
        # Convert form data to array
        x = [ ]
        for name in meta.features.columns:
            input_name = sub('-', '_', name)
            x.append(form.data[input_name])

        # Encode and predict
        x = np.array([ x ])
        x = feature_encoder.transform(x)
        yHat = model.predict(x)
        yHat = label_encoder.inverse_transform(yHat)
        yHat = yHat[0, 0]

        # Set message based on encoding
        if yHat == 'p':
            message = 'Looks like it\'s poisonous. Don\'t eat it!'
            message_color = 'error'
        else:
            message = 'Looks safe to eat! Hope it\'s tasty.'
            message_color = 'success'

    # Render template
    return render_template('index.html',
        form=form,
        message=message,
        message_color=message_color)