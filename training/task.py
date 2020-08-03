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
from . import data

if __name__ == '__main__':
    print(data.prepare_train_test_data())