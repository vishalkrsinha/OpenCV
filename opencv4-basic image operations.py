# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 22:21:54 2019

@author: VishalK
"""

import numpy as np
import cv2

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)
px1 = img[55,55]
print(px1)

########################################################
img[55,55] = [255,255,255] #White Color
px2 = img[55,55]
print(px2)

########  Sub-image of Image (Or, Region of Image)....
roi = img[100:150, 100:150]
print(roi)

img[100:150, 100:150] = [255,255,255] #White Color
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#########################################################
img[100:150, 100:150] = [255,255,255] #White Color

watch_face = img[37:111, 107:194]
img[0:74, 0:87] = watch_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()