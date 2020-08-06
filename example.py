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

    # Prompt for each data point
    x = []
    for name, feature in data.meta.features:
        # Get value from user
        value = input(f'{name} ({feature.catstring}): ')
        
        # Ask again if user doesn't give appropriate value
        while value not in feature.values:
            print(f'{value} not one of allowed values ({feature.values})')
            value = input(f'{name} ({feature.catstring}): ')
        
        # Append value to datapoint
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