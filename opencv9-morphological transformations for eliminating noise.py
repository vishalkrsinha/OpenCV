# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 22:03:45 2019

@author: VishalK
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # hsv hue sat value
    lower_red = np.array([150,150,50])
    upper_red = np.array([180,255,150])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(mask,kernel,iterations = 1)
    dilation = cv2.dilate(mask,kernel,iterations = 1)
    
    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
    
#    # It is the difference between input image and opening of the image
#    cv2.imshow('Tophat',tophat)
#    
#    # It is the difference between the closing of the input image and input image
#    cv2.imshow('Blackhat',blackhat)
    
    cv2.imshow('frame',frame)
    cv2.imshow('res',res)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dilation',dilation)
    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)       
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()
cap.release()