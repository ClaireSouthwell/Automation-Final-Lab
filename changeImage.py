#! /usr/bin/env python3

import os, sys
from PIL import Image 

# read .TIF files from ~/supplier-data/images

path = 'supplier-data/images/'
images = os.listdir(path)

for image in images:

    if os.path.splitext(image)[1] == '.tiff':
        image_name = os.path.splitext(image)[0]
        outfile = path + image_name + '.jpeg'

        try:
            Image.open(path + image).convert('RGB').resize((600,400)).save(outfile, 'JPEG')            
        except IOError:
            print('cannot convert', image)
