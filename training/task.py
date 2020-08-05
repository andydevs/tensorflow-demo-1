# Demonstrating creating a training 
# application using Tensorflow.
#
# This file executes the training
# and evaluation of the model with
# the data
#
# Author:  Anshul Kharbanda
# Created: 8 - 2 - 2020
from .data import get_train_test_data
from .model import model

# Model filename
model_filename = 'models/saved-model.h5'

# Main function
if __name__ == '__main__':
    # Get training and testing data
    train_labels, train_features, test_labels, test_features = get_train_test_data()
    
    # Train model
    print('Training...')
    model.fit(train_features, train_labels, epochs=10)
    model.summary()

    # Evaluate model
    print('Testing...')
    _, accuracy = model.evaluate(test_features, test_labels)
    print('Accuracy:', accuracy)

    # Save model
    print('Saving...')
    model.save(model_filename)