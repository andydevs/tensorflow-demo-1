# Demonstrating creating a training 
# application using Tensorflow.
#
# This file splits original data
# into training and testing data
#
# Author:  Anshul Kharbanda
# Created: 8 - 2 - 2020
import pandas as pd

# Filename of data to split
data_directory = 'data'
original_filename = 'original.csv'
training_filename = 'training.csv'
testing_filename = 'testing.csv'
train_frac = 0.666 # Reserve ~2/3 of the sample for training

# Main program
if __name__ == "__main__":
    # Read data frame and shuffle data
    df = pd.read_csv(f'{data_directory}/{original_filename}')

    # Split into training and testing data
    df_train = df.sample(frac=train_frac)
    df_test = df.drop(df_train.index)

    # Write to csv
    df_train.to_csv(f'{data_directory}/{training_filename}', index=False)
    df_test.to_csv(f'{data_directory}/{testing_filename}', index=False)