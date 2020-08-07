# Demonstrating creating a training 
# application using Tensorflow.
#
# This file contains a form 
# that's waaay too long to 
# have been written manually
#
# Author:  Anshul Kharbanda
# Created: 8 - 2 - 2020
from flask_wtf import FlaskForm
from wtforms import SelectField


class DataForm(FlaskForm):
    """
    Form for inputting data into
    machine learning model
    """

    """
    bruises
    """
    bruises = SelectField('bruises', choices=[
        ('f', 'no'),
        ('t', 'bruises')
    ])
    
    """
    cap-color
    """
    cap_color = SelectField('cap-color', choices=[
        ('b', 'buff'),
        ('c', 'cinnamon'),
        ('e', 'red'),
        ('g', 'gray'),
        ('n', 'brown'),
        ('p', 'pink'),
        ('r', 'green'),
        ('u', 'purple'),
        ('w', 'white'),
        ('y', 'yellow')
    ])
    
    """
    cap-shape
    """
    cap_shape = SelectField('cap-shape', choices=[
        ('b', 'bell'),
        ('c', 'conical'),
        ('f', 'flat'),
        ('k', 'knobbed'),
        ('s', 'sunken'),
        ('x', 'convex')
    ])
    
    """
    cap-surface
    """
    cap_surface = SelectField('cap-surface', choices=[
        ('f', 'fibrous'),
        ('g', 'grooves'),
        ('s', 'smooth'),
        ('y', 'scaly')
    ])
    
    """
    gill-attachment
    """
    gill_attachment = SelectField('gill-attachment', choices=[
        ('a', 'attached'),
        ('d', 'descending'),
        ('f', 'free'),
        ('n', 'notched')
    ])
    
    """
    gill-color
    """
    gill_color = SelectField('gill-color', choices=[
        ('b', 'buff'),
        ('e', 'red'),
        ('g', 'gray'),
        ('h', 'chocolate'),
        ('k', 'black'),
        ('n', 'brown'),
        ('o', 'orange'),
        ('p', 'pink'),
        ('r', 'green'),
        ('u', 'purple'),
        ('w', 'white'),
        ('y', 'yellow')
    ])
    
    """
    gill-size
    """
    gill_size = SelectField('gill-size', choices=[
        ('b', 'broad'),
        ('n', 'narrow')
    ])
    
    """
    gill-spacing
    """
    gill_spacing = SelectField('gill-spacing', choices=[
        ('c', 'close'),
        ('d', 'distant'),
        ('w', 'crowded')
    ])
    
    """
    odor
    """
    odor = SelectField('odor', choices=[
        ('a', 'almond'),
        ('c', 'creosote'),
        ('f', 'foul'),
        ('l', 'anise'),
        ('m', 'musty'),
        ('n', 'none'),
        ('p', 'pungent'),
        ('s', 'spicy'),
        ('y', 'fishy')
    ])
    
    """
    population
    """
    population = SelectField('population', choices=[
        ('a', 'abundant'),
        ('c', 'clustered'),
        ('n', 'numerous'),
        ('s', 'scattered'),
        ('v', 'several'),
        ('y', 'solitary')
    ])
    
    """
    ring-number
    """
    ring_number = SelectField('ring-number', choices=[
        ('n', 'none'),
        ('o', 'one'),
        ('t', 'two')
    ])
    
    """
    ring-type
    """
    ring_type = SelectField('ring-type', choices=[
        ('c', 'cobwebby'),
        ('e', 'evanescent'),
        ('f', 'flaring'),
        ('l', 'large'),
        ('n', 'none'),
        ('p', 'pendant'),
        ('s', 'sheathing'),
        ('z', 'zone')
    ])
    
    """
    spore-print-color
    """
    spore_print_color = SelectField('spore-print-color', choices=[
        ('b', 'buff'),
        ('h', 'chocolate'),
        ('k', 'black'),
        ('n', 'brown'),
        ('o', 'orange'),
        ('r', 'green'),
        ('u', 'purple'),
        ('w', 'white'),
        ('y', 'yellow')
    ])
    
    """
    stalk-color-above-ring
    """
    stalk_color_above_ring = SelectField('stalk-color-above-ring', choices=[
        ('b', 'buff'),
        ('c', 'cinnamon'),
        ('e', 'red'),
        ('g', 'gray'),
        ('n', 'brown'),
        ('o', 'orange'),
        ('p', 'pink'),
        ('w', 'white'),
        ('y', 'yellow')
    ])
    
    """
    stalk-color-below-ring
    """
    stalk_color_below_ring = SelectField('stalk-color-below-ring', choices=[
        ('b', 'buff'),
        ('c', 'cinnamon'),
        ('e', 'red'),
        ('g', 'gray'),
        ('n', 'brown'),
        ('o', 'orange'),
        ('p', 'pink'),
        ('w', 'white'),
        ('y', 'yellow')
    ])
    
    """
    stalk-root
    """
    stalk_root = SelectField('stalk-root', choices=[
        ('?', 'missing'),
        ('b', 'bulbous'),
        ('c', 'club'),
        ('e', 'equal'),
        ('r', 'rooted'),
        ('u', 'cup'),
        ('z', 'rhizomorphs')
    ])
    
    """
    stalk-shape
    """
    stalk_shape = SelectField('stalk-shape', choices=[
        ('e', 'enlarging'),
        ('t', 'tapering')
    ])
    
    """
    stalk-surface-above-ring
    """
    stalk_surface_above_ring = SelectField('stalk-surface-above-ring', choices=[
        ('f', 'fibrous'),
        ('k', 'silky'),
        ('s', 'smooth'),
        ('y', 'scaly')
    ])
    
    """
    stalk-surface-below-ring
    """
    stalk_surface_below_ring = SelectField('stalk-surface-below-ring', choices=[
        ('f', 'fibrous'),
        ('k', 'silky'),
        ('s', 'smooth'),
        ('y', 'scaly')
    ])
    
    """
    veil-color
    """
    veil_color = SelectField('veil-color', choices=[
        ('n', 'brown'),
        ('o', 'orange'),
        ('w', 'white'),
        ('y', 'yellow')
    ])
    
    """
    veil-type
    """
    veil_type = SelectField('veil-type', choices=[
        ('p', 'partial'),
        ('u', 'universal')
    ])
    