# Demonstrating creating a training 
# application using Tensorflow.
#
# This file uses the trained model
# to make a prediction
#
# Author:  Anshul Kharbanda
# Created: 8 - 2 - 2020
import tensorflow as tf
import numpy as np
from training import data
import yaml

# Main function
if __name__ == "__main__":
    # Get model
    model = tf.keras.models.load_model('models/saved-model.h5')

    # Read meta
    with open('data/meta.yaml') as f:
        d = yaml.full_load(f)

    # Prompt for data point
    x = []
    for name, categories in d['features'].items():
        allowed_inputs = list(categories.keys())
        category_string = ', '.join(f'{key}={value}' for key, value in categories.items())
        value = input(f'{name} ({category_string}): ')
        
        while value not in allowed_inputs:
            allowed_input_string = ', '.join(allowed_inputs)
            print(f'{value} not one of allowed values ({allowed_input_string})')
            value = input(f'{name} ({category_string}): ')
        
        x.append(value)

    # Transform input and make prediction
    x = np.array([ x ])
    x = data.feature_encoder.transform(x).toarray()
    yHat = model.predict(x)
    yHat = data.label_encoder.inverse_transform(yHat)[0,0]
    
    # Print prediction
    if yHat == 'p':
        print('Looks like it\'s poisonous. You shouldn\'t eat it.')
    else:
        print('Looks like it\'s safe to eat! Hope it\'s tasty.')