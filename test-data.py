import dictionary
import yaml

with open('data/dictionary.yaml') as f:
    d = yaml.full_load(f)
    print(d)