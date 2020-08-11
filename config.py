# Demonstrating creating a training 
# application using Tensorflow.
#
# This file stores configuration
# For the entire project!
#
# Author:  Anshul Kharbanda
# Created: 8 - 2 - 2020

# Flask config
SECRET_KEY = 'ivemadeaseverandcontinuouslapseinmyjudgement'
WTF_CSRF_SECRET_KEY = 'andidontexpecttobeforgivenimsimplyheretoapologize'

# Data system
data_directory = 'data'
data_filename = 'mushrooms.csv'
meta_filename = 'meta.yaml'
data_trainfrac = 0.8

# Model file
model_directory = 'models'
model_filename = 'saved-model.h5'