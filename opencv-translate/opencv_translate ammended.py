# USAGE
# python opencv_translate.py

# import the necessary packages
import numpy as np
import argparse
import imutils
import cv2

image = cv2.imread(r'C:\Users\EN133JJ\Downloads\GitHub\pis-uni\opencv-translate\newimage.jpg')

translated_image = imutils.translate(image, 250, -150)
cv2.imshow('transimage', translated_image)
cv2.waitKey(0)