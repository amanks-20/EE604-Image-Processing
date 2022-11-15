import numpy as np
import cv2 as cv

import sys

docking_station_number = int(sys.argv[1])

digit_codes = {
"0" : [
    [1, 1, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 1, 1]
], 
"1" : [
    [1 ,1 , 0],
    [0 ,1 , 0],
    [0 ,1 , 0],
    [0 ,1 , 0],
    [1 ,1 , 1]
],
"2" : [
    [1 ,1 , 1],
    [0 ,0 , 1],
    [1 ,1 , 1],
    [1 ,0 , 0],
    [1 ,1 , 1]
],
"3" : [
    [1 ,1 , 1],
    [0 ,0 , 1],
    [1 ,1 , 1],
    [0 ,0 , 1],
    [1 ,1 , 1]
],
"4" : [
    [1 ,0 , 1],
    [1 ,0 , 1],
    [1 ,1 , 1],
    [0 ,0 , 1],
    [0 ,0 , 1]
],
"5" : [
    [1 ,1 , 1],
    [1 ,0 , 0],
    [1 ,1 , 1],
    [0 ,0 , 1],
    [1 ,1 , 1]
],
"6" : [
    [1 ,1 , 1],
    [1 ,0 , 0],
    [1 ,1 , 1],
    [1 ,0 , 1],
    [1 ,1 , 1]
],
"7" : [
    [1 ,1 , 1],
    [0 ,0 , 1],
    [0 ,0 , 1],
    [0 ,0 , 1],
    [0 ,0 , 1]
],
"8" : [
    [1 ,1 , 1],
    [1 ,0 , 1],
    [1 ,1 , 1],
    [1 ,0 , 1],
    [1 ,1 , 1]
],
"9" : [
    [1 ,1 , 1],
    [1 ,0 , 1],
    [1 ,1 , 1],
    [0 ,0 , 1],
    [1 ,1 , 1]
]
}

img = np.zeros((300, 500))

WHITE = 255

cursor_pos = [50, 0]

for c in str(docking_station_number):
    digit_code = digit_codes[c]
    for i in range(5):
        for j in range(3):
            if digit_code[i][j]:
                posn = (
                    25 + j*50+(j+1)*(50//6) + cursor_pos[0], 
                    25 + i*50+(i+1)*(50//6) + cursor_pos[1]
                )
                cv.circle(img, posn, 25, WHITE, -1)
    cursor_pos[0] += 200 + 50//3

cv.imwrite("dotmatrix.jpg", img)
cv.waitKey(0)