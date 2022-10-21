# USAGE
# python image_arithmetic.py

# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="grand_canyon.png",
	help="path to the input image")
args = vars(ap.parse_args())



# load the original input image and display it to our screen
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
print('original array: ', image.shape)
print('\n')
cv2.waitKey(0)

# increasing the pixel intensities in our input image by 100 is
# accomplished by constructing a NumPy array that has the *same
# dimensions* as our input image, filling it with ones, multiplying
# it by 100, and then adding the input image and matrix together

M = np.ones(image.shape, dtype='uint8')*100
print('lighter array: ', M.shape)
print('\n')
lighter = cv2.add(image, M)
cv2.imshow('Lighter', lighter)
cv2.waitKey(0)


N = np.ones(image.shape, dtype='uint8')*75
print('darker array', N.shape)
darker = cv2.subtract(image, N)
cv2.imshow('Darker', darker)
cv2.waitKey(0)












# M = np.ones(image.shape, dtype="uint8") * 100
# added = cv2.add(image, M)
# cv2.imshow("Lighter", added)

# # similarly, we can subtract 50 from all pixels in our image and make it
# # darker
# M = np.ones(image.shape, dtype="uint8") * 50
# subtracted = cv2.subtract(image, M)
# cv2.imshow("Darker", subtracted)
# cv2.waitKey(0)