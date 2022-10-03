import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', default = 'adrian.png', type = str,
                help = 'image to analyze its pixels')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
h, w = image.shape[:2]
print(h, w)

(b, g, r) = image[50, 30]
print('r: {}, g: {}, b: {}'.format(r,g,b))

# image[10, 400] = (0, 0, 255)
# image[10, 401] = (0, 0, 255)
# image[10, 402] = (0, 0, 255)
# image[11, 400] = (0, 0, 255)
# image[11, 401] = (0, 0, 255)
# image[11, 402] = (0, 0, 255)
# image[12, 400] = (0, 0, 255)
# image[12, 401] = (0, 0, 255)
# image[12, 402] = (0, 0, 255)
# image[13, 400] = (0, 0, 255)
# image[13, 401] = (0, 0, 255)
# image[13, 402] = (0, 0, 255)

(cx, cy) = (w // 2, h // 2 )

image1 = image[0:cy, 0:cx]
image2 = image[cy:h, cx:w]
image3 = image[0:cy, cx:w]
image4 = image[cy:h, 0:cx]

image[0:cy, 0:cx] = (0, 0, 255)

cv2.imshow('image2see', image)
cv2.waitKey(0)