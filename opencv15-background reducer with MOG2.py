# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 01:27:49 2019

@author: VishalK
"""

import cv2
import numpy as np

cap = cv2.VideoCapture('people-walking.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    
    cv2.imshow('original',frame)
    cv2.imshow('fgmask',fgmask)
    
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
    