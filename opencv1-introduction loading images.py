# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 22:36:02 2019

@author: VishalK
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
#IMREAD_GRAYSCALE = 0
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1

#OpenCV is BGR
#matplotlib is RGB

########Plotting image with OpenCV................
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('watchGray.png',img)

########Plotting image with matplotlib................
#plt.imshow(img,cmap='gray',interpolation='bicubic')
#plt.plot([50,100],[80,100],'c',linewidth=5)
#plt.show()