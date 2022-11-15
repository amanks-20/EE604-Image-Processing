import cv2 as cv
import numpy as np

import sys

img_pathY = str(sys.argv[1])
img_pathCb = str(sys.argv[2])
img_pathCr = str(sys.argv[3])


imgY = cv.imread(img_pathY, cv.IMREAD_GRAYSCALE)
imgCr = cv.imread(img_pathCr, cv.IMREAD_GRAYSCALE)
imgCb = cv.imread(img_pathCb, cv.IMREAD_GRAYSCALE)

imgCr = cv.pyrUp(cv.pyrUp(imgCr))
imgCb = cv.pyrUp(cv.pyrUp(imgCb))

img = np.zeros((imgY.shape[0], imgY.shape[1], 3), np.uint8)
img[::, ::, 0] = imgY
img[::, ::, 1] = imgCr[:imgY.shape[0], :imgY.shape[1]]
img[::, ::, 2] = imgCb[:imgY.shape[0], :imgY.shape[1]]

img = cv.cvtColor(img, cv.COLOR_YCR_CB2BGR)

cv.imwrite("flyingelephant.jpg", img)

# cv.imshow("Image1", imgY)
# cv.imshow("Image", img)
# cv.waitKey(0)