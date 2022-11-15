import cv2 as cv
import numpy as np

import sys

img_path = str(sys.argv[1])

img = cv.imread(img_path)

l1 = np.array([114.26327160493827, 112.22777777777777, 107.86697530864197]) #b
l2 = np.array([186.36271766169153, 197.79337686567163, 213.43547885572139]) #r
l3 = np.array([ 55.363575117898044, 86.98944531776331,  75.66067819447564]) #g

l = np.array([np.average(img[::, ::, i]) for i in range(3)])

e1 = np.linalg.norm(l-l1)
e2 = np.linalg.norm(l-l2)
e3 = np.linalg.norm(l-l3)
e = min(e1, e2, e3)

if(e == e1):
    print(1)
elif(e == e2):
    print(3)
elif(e == e3):
    print(2) 