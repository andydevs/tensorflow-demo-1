Tensorflow Demo 1
================================================================

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Demonstrating creating a training application using Tensorflow.

The Data
----------------------------------------------------------------

This project aims to predict if a mushroom is poisonous or not
depending on various characteristics of the mushroom. The data
is stored in the `data` directory, which contains the `mushrooms.csv`
file, as well as a `meta.yaml` that outlines the structure of each
feature (column) of the csv file.

Developing
----------------------------------------------------------------

### Setup

Clone source tree from github

    $ git clone https://github.com/andydevs/tensorflow-demo-1.git

Create environment using virtualenv and activate it

    $ virtualenv env
    $ ./env/Scripts/activate

Install requirements

    $ pip install -r requirements.txt

### Commands

To run the training step.

    $ python -m training.task

To run the web app

    $ flask run

