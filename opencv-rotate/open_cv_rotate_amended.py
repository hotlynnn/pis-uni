import cv2
import imutils
import argparse


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True,
                help= 'location and name of image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
rotate1 = imutils.rotate(image, -45)
rotate2 = imutils.rotate(image, -45, (50,50))
rotate3 = imutils.rotate(image, 180)




cv2.imshow('read_image', rotate1)
cv2.waitKey(0)
cv2.imshow('read_image', rotate2)
cv2.waitKey(0)
cv2.imshow('read_image', rotate3)
cv2.waitKey(0)