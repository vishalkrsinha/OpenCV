# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 23:34:37 2019

@author: VishalK
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('opencv-python-foreground-extraction-tutorial.jpg')
mask = np.zeros(img.shape[:2],np.uint8)

bgModel = np.zeros((1,65),np.float64)
fgModel = np.zeros((1,65),np.float64)

rect = (50,50,300,500)

cv2.grabCut(img,mask,rect,bgModel,fgModel,5,cv2.GC_INIT_WITH_RECT)
mask2=np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()