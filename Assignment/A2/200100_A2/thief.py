import cv2 as cv
import numpy as np

import sys

img_path = str(sys.argv[1])

img = cv.imread(img_path)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_eq = cv.equalizeHist(img_gray)
img_blur = cv.GaussianBlur(img_eq, (3, 3), 1.5)
cv.imwrite("enhanced-"+img_path, img_blur)
