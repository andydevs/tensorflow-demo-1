# Demonstrating creating a training 
# application using Tensorflow.
#
# The model itself!
#
# Author:  Anshul Kharbanda
# Created: 8 - 2 - 2020
import tensorflow as tf
from .data import get_feature_columns, get_output_size

# Create preprocessing layer
preprocessing = tf.keras.layers.DenseFeatures(
    feature_columns=get_feature_columns())

# Define model using keras
model = tf.keras.models.Sequential([
    preprocessing,
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(get_output_size(), activation='softmax')
])
model.compile(
    loss=tf.keras.losses.CategoricalCrossentropy(),
    optimizer='adam',
    metrics=['accuracy']
)