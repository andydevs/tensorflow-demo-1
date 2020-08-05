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
from .data import get_train_test_data

# Main function
if __name__ == '__main__':
    # Get training and testing data
    train_labels, train_features, test_labels, test_features = get_train_test_data()
    print(train_labels)
    print(train_features)
    print(test_labels)
    print(test_features)