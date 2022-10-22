import cv2
import argparse
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="newimage.jpg",
	help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
print(image.shape)
cv2.waitKey(0)

mask = np.zeros(image.shape[:2], dtype = 'uint8')
mask = cv2.rectangle(mask, (50,100), (600, 600), (255, 255, 255), -1)
cv2.imshow("Mask", mask)
cv2.waitKey(0)

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Masked", masked)
cv2.waitKey(0)
