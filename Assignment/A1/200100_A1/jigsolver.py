import cv2 as cv
import numpy as np

import sys

img_path = str(sys.argv[1])

img = cv.imread(img_path)

sub_img1 = img[0:200, 0:190].copy()
sub_img2 = img[200:410, 0:190].copy()
sub_img3 = img[150:330, 515:700].copy()
sub_img4 = img[370:, 370:].copy()

# part 1
img[202:402, 0:190, 0] = sub_img1[::, ::, 1]
img[202:402, 0:190, 1] = sub_img1[::, ::, 0]
img[202:402, 0:190, 2] = sub_img1[::, ::, 2]

# part 2
sub_img2 = sub_img2[::-1, ::]
img[0:210, 0:190] = sub_img2

# part 3
sub_img3 = sub_img3[::, ::-1]
img[150:330, 515:700] = sub_img3

# part 4
img[370:, 370:] = sub_img4[::-1, ::]

# part 5
temp = img[411:421, 0:190]
img[401:411, 0:190] = temp[::-1, ::]

cv.imwrite("jigsolved.jpg", img)
