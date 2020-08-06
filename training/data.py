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
import yaml

# Data parameters
data_directory = 'data'
data_filename = 'mushrooms.csv'
dict_filename = 'dictionary.yaml'


# Input and output sizes
with open(f'{data_directory}/{dict_filename}') as f:
    # Read dictionary
    d = yaml.full_load(f)

    # Size of input vector to ML model
    input_size = sum(
        len(feature.keys())
        for feature in
        d['features'].values()
    )

    # Size of output vector in ML model
    output_size = len(d['output']['labels'].keys())

    # Fit one hot encoders
    label_column = d['output']['column']
    feature_columns = list(d['features'].keys())
    label_classes = list(d['output']['labels'].keys())
    feature_categories = [list(feature.keys()) for feature in d['features'].values()]
    label_encoder = OneHotEncoder(categories=[label_classes])
    feature_encoder = OneHotEncoder(categories=feature_categories)
    df = pd.read_csv(f'{data_directory}/{data_filename}')
    labels = df[label_column].values.reshape(-1,1)
    features = df[feature_columns].values
    label_encoder.fit(labels)
    feature_encoder.fit(features)


def prepare_dataset(dataframe):
    """
    Split dataframe into feature and labels and 
    encode them into one-hot representation
    """
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
    # Reaed data from csv file
    data = pd.read_csv(f'{data_directory}/{data_filename}')

    # Split into training and testing data
    training = data.sample(frac=train_frac)
    testing = data.drop(training.index)
    train_labels, train_features = prepare_dataset(training)
    test_labels, test_features = prepare_dataset(testing)

    # Return all this
    return train_labels, train_features, test_labels, test_features