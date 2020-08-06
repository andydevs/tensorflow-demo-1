# Demonstrating creating a training 
# application using Tensorflow.
#
# The model itself!
#
# Author:  Anshul Kharbanda
# Created: 8 - 2 - 2020
import tensorflow as tf
from .data import dictionary

# Define model using keras
model = tf.keras.models.Sequential([
    tf.keras.Input(shape=(dictionary.features.size,)),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(dictionary.output.size, activation='softmax')
])
model.compile(
    loss=tf.keras.losses.CategoricalCrossentropy(),
    optimizer='adam',
    metrics=['accuracy']
)
model.summary()