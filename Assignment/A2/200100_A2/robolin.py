import cv2 as cv
import sys
img_path = str(sys.argv[1])

img_org = cv.imread(img_path)
img = cv.cvtColor(img_org, cv.COLOR_BGR2GRAY)
img = cv.GaussianBlur(img, (5, 5), 1.5)
img = cv.Canny(img, 200, 100)
img = cv.dilate(img, (10, 20), iterations=2)
img_org[::, ::, 2][img==255] = 255
cv.imwrite("robolin-"+img_path, img_org)