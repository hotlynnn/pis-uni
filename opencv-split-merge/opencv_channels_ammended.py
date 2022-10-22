# USAGE
# python opencv_channels.py

# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="opencv_logo.png",
	help="path to the input image")
args = vars(ap.parse_args())

# load the input image and grab each channel -- note how OpenCV
# represents images as NumPy arrays with channels in Blue, Green,
# Red ordering rather than Red, Green Blue
image = cv2.imread(args["image"])
(B, G, R) = cv2.split(image)

# show each channel individually
cv2.imshow("Red", R)
print(R.shape)
cv2.imshow("Green", G)
print(G.shape)
cv2.imshow("Blue", B)
print(B.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()

# merge the image back together again
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)

ones = np.ones(image.shape[:2], dtype = 'uint8')*255
cv2.imshow('Zeros', ones)
cv2.waitKey(0)
red_merged = cv2.merge([ones, ones, R])
cv2.imshow('Red_merged', red_merged)
cv2.waitKey(0)
