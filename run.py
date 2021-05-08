'''Write a Python script named run.py to process the text files (001.txt,
003.txt ...) from the supplier-data/descriptions directory. The script should
turn the data into a JSON dictionary by adding all the required fields,
including the image associated with the fruit (image_name), and uploading it to
http://[linux-instance-external-IP]/fruits using the Python requests library.'''

#! /usr/bin/env python3

import os, requests, sys 

path = 'supplier-data/descriptions/'
descriptions = os.listdir(path)

for description in descriptions:
    if description.endswith('.txt'): 
    # Read lines in txt file and convert to dictionary
        desc = {}
        with open(path + description, 'r') as d:
            desc['name'] = d.readline()
            desc['weight'] = int(d.readline().split()[0])
            desc['description'] = d.readline()
            desc['image_name'] = os.path.splitext(description)[0] + '.jpeg'

            # Use the POST method to upload the data to the URL
            # http://[linux-instance-external-IP]/fruits

            response = requests.post('http://<IP address>/fruits/', json = desc)
