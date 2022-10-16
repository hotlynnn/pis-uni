# USAGE
# python basic_drawing.py

# import the necessary packages
import numpy as np
import cv2

# initialize our canvas as a 300x300 pixel image with 3 channels
# (Red, Green, and Blue) with a black background
# canvas = np.array((222, 242, 215, 3), dtype="uint8")
# cv2.imwrite('imagetry.png', canvas)
image = cv2.imread(r'C:\Users\EN133JJ\Downloads\GitHub\pis-uni\opencv-drawing\adrian.png')
print(image.shape[:2])
color = tuple(np.random.randint(0, high=256, size=(3,)))
print(color)
cv2.line(image, (0,0), (600, 450), (0, 0, 255))
cv2.line(image, (600,0), (0, 450), (0, 255, 255), 10)
cv2.rectangle(image, (600,0), (0, 450), (255, 0, 0), 3)

for r in range(0, 450, 50):

    cv2.circle(image, (300, 225), r, (0, 255, 0), 3)


cv2.imshow('numpyimage', image)
cv2.waitKey(0)

# draw a green line from the top-left corner of our canvas to the
