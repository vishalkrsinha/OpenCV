# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 22:41:07 2019

@author: VishalK
"""

import cv2
import numpy as np

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')

add = img1+img2
cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()

##########################
add1 = cv2.add(img1,img2)
cv2.imshow('cv2 Add',add1)
cv2.waitKey(0)
cv2.destroyAllWindows()
# (155, 211,79) +   (50, 170, 200) = 205, 381, 279 ....translated to (205, 255, 255)


########################## Weighted Image....
weightedImage = cv2.addWeighted(img1,0.6, img2,0.4,0)
cv2.imshow('Weighted Image',weightedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()


#################################################
img1 = cv2.imread('3D-Matplotlib.png')
img3 = cv2.imread('mainlogo.png')

rows,cols,channel = img3.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)

cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()


#################################################
img4 = cv2.imread('3D-Matplotlib.png')
img5 = cv2.imread('mainlogo.png')

rows,cols,channel = img5.shape
roi1 = img4[0:rows, 0:cols]
roi2 = np.zeros(img4.shape[:2],dtype=np.uint8)
# https://stackoverflow.com/questions/50957151/opencv-error-bitwise-and-throws-error-that-mask-and-image-are-not-same-size

img2gray1 = cv2.cvtColor(img5,cv2.COLOR_BGR2GRAY)
ret1, mask1 = cv2.threshold(img2gray1,220,255,cv2.THRESH_BINARY_INV)
mask_inv1 = cv2.bitwise_not(mask1)

img4_bg = cv2.bitwise_and(roi1,roi2,mask = mask_inv1) #https://stackoverflow.com/questions/50957151/opencv-error-bitwise-and-throws-error-that-mask-and-image-are-not-same-size
img5_fg = cv2.bitwise_and(img5,img5,mask = mask1)

dst1 = cv2.add(img4_bg,img5_fg)
img4[0:rows,0:cols] = dst1

cv2.imshow('res',img4)
cv2.imshow('mask_inv',mask_inv1)
cv2.imshow('img4_bg',img4_bg)
cv2.imshow('img5_fg',img5_fg)
cv2.imshow('dst',dst1)
cv2.waitKey(0)
cv2.destroyAllWindows()