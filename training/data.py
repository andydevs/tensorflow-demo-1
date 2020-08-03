# Demonstrating creating a training 
# application using Tensorflow.
#
# This file prepares the data
# for training and evaluation
#
# Author:  Anshul Kharbanda
# Created: 8 - 2 - 2020
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np
import json

# Data parameters
data_directory = 'data'
data_filename = 'mushrooms.csv'
dict_filename = 'dictionary.json'


def get_input_output_size():
    """
    Get input and output size of machine learning model
    from dictionary of categories and labels
    """
    with open(f'{data_directory}/{dict_filename}') as f:
        d = json.load(f)

        # Size of input vector to ML model
        input_size = sum(
            len(feature.keys())
            for feature in
            d['features'].values()
        )

        # Size of output vector in ML model
        output_size = len(d['output']['labels'].keys())

    # Return input and output size
    input_size, output_size


def prepare_dataset(dataframe, dictionary, label_encoder, feature_encoder):
    """
    Split dataframe into feature and labels and 
    encode them into one-hot representation
    """
    # Get feature and label columns
    label_column = dictionary['output']['column']
    feature_columns = list(dictionary['features'].keys())

    # Split data into labels and features
    labels = dataframe[label_column].values.reshape(-1,1)
    features = dataframe[feature_columns].values

    # Map features into one-hot vectors
    encoded_labels = label_encoder.transform(labels).toarray()
    encoded_features = feature_encoder.transform(features).toarray()

    # Return labels and features
    return encoded_labels, encoded_features


def prepare_train_test_data(train_frac=0.8):
    """
    Read csv file, convert it to 
    machine learning representation, 
    split features and labels, and 
    split into training and testing data.
    """
    # Read dictionary from json file
    dictionary = {}
    with open(f'{data_directory}/{dict_filename}') as f:
        dictionary = json.load(f)
    feature_names = list(dictionary['features'].keys())
    feature_categories = [list(feature.keys()) for feature in dictionary['features'].values()]
    label_name = dictionary['output']['column']
    label_classes = list(dictionary['output']['labels'].keys())

    # Reaed data from csv file
    data = pd.read_csv(f'{data_directory}/{data_filename}')

    # Create scikit learn encoders
    labels = data[label_name].values.reshape(-1,1)
    label_encoder = OneHotEncoder(categories=[label_classes])
    label_encoder.fit(labels)
    features = data[feature_names].values
    feature_encoder = OneHotEncoder(categories=feature_categories)
    feature_encoder.fit(features)

    # Split into training and testing data
    training = data.sample(frac=train_frac)
    testing = data.drop(training.index)
    train_labels, train_features = prepare_dataset(
        dataframe=training, 
        dictionary=dictionary, 
        label_encoder=label_encoder, 
        feature_encoder=feature_encoder)
    test_labels, test_features = prepare_dataset(
        dataframe=training, 
        dictionary=dictionary, 
        label_encoder=label_encoder, 
        feature_encoder=feature_encoder)

    # Return all this
    return (train_labels, train_features, test_labels, test_features)