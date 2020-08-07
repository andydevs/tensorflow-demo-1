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
from . import parsing

# Data parameters
data_directory = 'data'
data_filename = 'mushrooms.csv'
meta_filename = 'meta.yaml'

# Read meta
with open(f'{data_directory}/{meta_filename}') as f:
    meta = yaml.full_load(f)

# Create One-Hot Encoders
label_encoder = OneHotEncoder(categories=[meta.output.labels.values])
feature_encoder = OneHotEncoder(categories=meta.features.categories)

# "Fit" the one hot encoders for some odd reason
df = pd.read_csv(f'{data_directory}/{data_filename}')
labels, features = meta.split_dataset(df)
label_encoder.fit(labels)
feature_encoder.fit(features)


def prepare_dataset(dataframe):
    """
    Split dataframe into feature and labels and 
    encode them into one-hot representation
    """
    # Split data into labels and features
    labels, features = meta.split_dataset(df)

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