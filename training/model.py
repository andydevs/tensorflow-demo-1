# Demonstrating creating a training 
# application using Tensorflow.
#
# This file defines the model
# that will be trained with the
# data
#
# Author:  Anshul Kharbanda
# Created: 8 - 2 - 2020
import tensorflow as tf
import tempfile
import json

# Convert dictionary category features into feature columns
feature_columns = []
with open('data/dictionary.json') as f:
    # Load dictionary from file
    dictionary = json.load(f)

    # Create a "Categorical Column" for each feature in the dictionary
    for name, vocabulary in dictionary['features'].items():
        column = tf.feature_column.categorical_column_with_vocabulary_list(
            key=name,
            vocabulary_list=list(vocabulary.keys())
        )
        column = tf.feature_column.indicator_column(column)
        feature_columns.append(column)

# Create Model
model = tf.keras.models.Sequential([
    tf.keras.layers.DenseFeatures(feature_columns), # Processes the features to make them good for training
    tf.keras.layers.Dense(16, activation='relu'),   # An example of a hidden layer
    tf.keras.layers.Dense(2, activation='softmax')  # Classification layer
])
model.compile(
    loss=tf.keras.losses.CategoricalCrossentropy(), # Good error function for categories
    optimizer='adam') # Best optimizer to use right now

# Create an estimator which will help with training and evaluation
estimator = tf.keras.estimator.model_to_estimator(keras_model=model)