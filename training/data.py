# Demonstrating creating a training 
# application using Tensorflow.
#
# This file prepares the data
# for training and evaluation
#
# Author:  Anshul Kharbanda
# Created: 8 - 2 - 2020
import tensorflow as tf
import pandas as pd
import numpy as np
import yaml

# Data parameters
data_directory = 'data'
data_filename = 'mushrooms.csv'
dict_filename = 'dictionary.yaml'


def get_features():
    with open(f'{data_directory}/{dict_filename}') as f:
        d = yaml.full_load(f)
        features = d['features']
    return features


def get_output():
    with open(f'{data_directory}/{dict_filename}') as f:
        d = yaml.full_load(f)
        output = d['output']
    return output


def get_feature_columns():
    features = get_features()
    feature_columns = [
        tf.feature_column.indicator_column(
            tf.feature_column.categorical_column_with_vocabulary_list(
                key=feature_name,
                vocabulary_list=list(categories.keys())
            )
        )
        for feature_name, categories in features.items()
    ]
    return feature_columns


def one_hot_encode_labels(series):
    # Get label names
    output = get_output()
    labels = sorted(output['labels'].keys())
    print(labels)

    # Get array from series
    array = series.values

    # Map labels to indeces
    indexer = np.vectorize(lambda y: labels.index(y))
    indeces = indexer(array)
    print(indeces)

    # Create a identity matrix for one-hot-assignment
    one_hot_matrix = np.identity(len(labels))
    print(one_hot_matrix)

    # Map indeces to one-hot vectors
    one_hot_labels = np.apply_along_axis(
        lambda index: one_hot_matrix[index, :],
        0, indeces
    )
    return one_hot_labels


def process_dataset(dataset):
    features = get_features()
    output = get_output()
    labels = dataset[output['column']]
    features = dataset[features.keys()]
    one_hot_labels = one_hot_encode_labels(labels)
    return one_hot_labels, features


def get_train_test_data(train_frac=0.8):
    df = pd.read_csv(f'{data_directory}/{data_filename}')
    training = df.sample(frac=train_frac)
    testing = df.drop(training.index)
    train_labels, train_features = process_dataset(training)
    test_labels, test_features = process_dataset(testing)
    return (
        train_labels,
        train_features,
        test_labels,
        test_features
    )