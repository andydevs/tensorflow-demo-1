# Demonstrating creating a training 
# application using Tensorflow.
#
# This file cleanly loads the data
# dictionary (stored in the .yaml
# file) to be used in the data pipeline
#
# Author:  Anshul Kharbanda
# Created: 8 - 2 - 2020
import yaml


class DataDictionary(yaml.YAMLObject):
    """
    Spec for data dictionary. Contains Features and Output
    """
    yaml_tag = u'!DataDictionary'

    def __init__(self, output, features):
        """
        DataDictionary initialization

        :param output:   output spec
        :param features: feature spec
        """
        self.output = output
        self.features = features

    def __repr__(self):
        """
        String representation of object
        """
        return f'DataDictionary(output={self.output}, features={self.features})'


class Output(yaml.YAMLObject):
    """
    Spec for output definition. Column name and labels
    """
    yaml_tag = u'!Output'
    
    def __init__(self, column, labels):
        """
        Output initialization

        :param column: column name of output data in dataset
        :param labels: label categories to train with
        """
        self.column = column
        self.labels = labels

    def __repr__(self):
        """
        Detailed string representation
        """
        return f'Output(column={self.column}, labels={self.labels})'


class FeatureSet(yaml.YAMLObject):
    """
    Set of features in model.
    """
    yaml_tag = u'!FeatureSet'

    def __init__(self, features):
        """
        FeatureSet initialization

        :param features: dictionary of feature specs
        """
        self.features = features

    def __repr__(self):
        """
        Detailed string representation
        """
        return f'FeatureSet(features={self.features})'


class CategorySet(yaml.YAMLObject):
    """
    Set of categories and their respective definitions for a feature or label-set
    """
    yaml_tag = u'!CategorySet'

    def __init__(self, categories):
        """
        CategorySet initialization

        :param categories: dictionary of categories 
        """
        self.categories = categories

    @property
    def catstring(self):
        """
        String of key/value pairs to be used for prompts
        """
        return ', '.join(f'{key}={value}' for key, value in self.categories.items())

    def __repr__(self):
        """
        Detailed string representation
        """
        return f'CategorySet(categories={self.categories})'
