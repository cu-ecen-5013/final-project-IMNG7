from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import cv2
import numpy as np 
import imutils
import argparse


ap=argparse.ArgumentParser()
ap.add_argument("-i","--images",required=True,help="path to images directory")
args = vars(ap.parse_args)

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

