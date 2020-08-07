# Demonstrating creating a training 
# application using Tensorflow.
#
# This file cleanly loads the data
# dictionary (stored in the .yaml
# file) as objects to be used in 
# the data pipeline
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

    def split_dataset(self, dataset):
        """
        Splits dataset into labels and features

        :param dataset: dataset being split
        """
        labels = dataset[self.output.column].values.reshape(-1,1)
        features = dataset[self.features.columns].values
        return labels, features


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

    @property
    def size(self):
        """
        Total output size
        """
        return len(self.labels)


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

    def __iter__(self):
        """
        Iterator over features
        """
        return iter(self.features.items())

    @property
    def size(self):
        """
        Total input size of feature set in ML model
        """
        return sum(len(feature) for feature in self.features.values())

    @property
    def categories(self):
        """
        Return all categories for all features
        """
        return [ feature.values for feature in self.features.values() ]

    @property
    def columns(self):
        """
        Return names of columns for all features
        """
        return list(self.features.keys())


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

    def __repr__(self):
        """
        Detailed string representation
        """
        return f'CategorySet(categories={self.categories})'

    def __len__(self):
        """
        Total number of categories in set
        """
        return len(self.categories.items())

    @property
    def catstring(self):
        """
        String of key/value pairs to be used for prompts
        """
        return ', '.join(f'{key}={value}' for key, value in self.categories.items())

    @property
    def values(self):
        """
        List of category values
        """
        return list(self.categories.keys())