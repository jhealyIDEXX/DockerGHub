#!/usr/bin/env python

from PIL import Image
from PIL import ImageDraw
import numpy as np
import cv2
import dicom
import sys
import glob 
import os

def greyscaleConversion(filepath):
    
      for filename in glob.glob(filepath + r'/*.jpg'):
        filename = os.path.realpath(filename);
        img = Image.open(filename);
        img = img.convert(mode='RGB')
        img.save(filename);
        print("SAVED: " + filename);