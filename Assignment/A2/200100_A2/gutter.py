import cv2 as cv
import numpy as np

import sys

img_path = str(sys.argv[1])

img = cv.imread(img_path)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_dilated = cv.dilate(img_gray, np.ones((7, 7), np.uint8))
img_bg = cv.medianBlur(img_dilated, 21)
img_diff = 255-cv.absdiff(img_gray, img_bg)
img_norm = cv.normalize(img_diff, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
cv.imwrite("cleaned-"+img_path, img_norm)
