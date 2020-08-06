# Demonstrating creating a training 
# application using Tensorflow.
#
# This file executes the training
# and evaluation of the model with
# the data
#
# Author:  Anshul Kharbanda
# Created: 8 - 2 - 2020
import argparse
from .model import model
from .data import prepare_train_test_data

# Model file name
model_filename = 'models/saved-model.h5'

# Main function
if __name__ == '__main__':
    # Get training and testing data
    train_labels, train_features, test_labels, test_features = prepare_train_test_data()

    # Train model on training data
    print('Training...')
    model.fit(train_features, train_labels, epochs=10)

    # Evaluate model on test data
    print('Evaluating...')
    _, accuracy = model.evaluate(test_features, test_labels)
    print('Accuracy:', accuracy)

    # Save model
    print('Saving...')
    model.save(model_filename)