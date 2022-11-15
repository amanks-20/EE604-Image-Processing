import cv2 as cv
import numpy as np

import sys

img_path = str(sys.argv[1])

img = cv.imread(img_path)

# img_new = cv.bilateralFilter(img, 30, 60, 300)
img_new = cv.bilateralFilter(img, 40, 100, 300)

cv.imwrite("denoised.jpg", img_new)

# cv.imshow("Image", img)
# cv.imshow("Image2", img_new)
# cv.waitKey(0)