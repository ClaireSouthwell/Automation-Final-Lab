#! /usr/bin/env python3

import requests
import os, sys 



url = 'http:<linux-instance-IP-address>/upload/'
#url = 'http://localhost/upload/'
folder = 'supplier-data/images/'

images =  os.listdir(folder)
for image in images:
    # Check that the extension is a jpeg
    if image.endswith('.jpeg'):
           with open(folder+image, 'rb') as opened:
            r = requests.post(url, files={'file': opened})

''' example_upload.py

# This example shows how a file can be uploaded using
# the Python Requests module  

url = 'http://localhost/upload'
with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
    r = requests.post(url, files={'file': opened})

In a similar way, you are going to write a script named
supplier_image_upload.py that takes the jpeg images from
the supplier-data/images directory that you've processed
previously and uploads them to the web server fruit catalog.'''
