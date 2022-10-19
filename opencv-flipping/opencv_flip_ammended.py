# USAGE
# python opencv_flip.py

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="opencv_logo.png",
	help="path to the input image")
args = vars(ap.parse_args())

# load the original input image and display it to our screen
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

flipped1 = cv2.flip(image, -1)
cv2.imshow("Flipped", flipped1)
cv2.waitKey(0)

flipped2 = cv2.flip(image, 0)
cv2.imshow("Flipped", flipped2)
cv2.waitKey(0)

