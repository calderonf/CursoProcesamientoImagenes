# -*- coding: utf-8 -*-
"""
Created on Fri May 03 05:21:09 2019

@author: franc
"""

import numpy as np
import cv2


vidStreamL = cv2.VideoCapture(0)  # index of your left camera
vidStreamL.set(3,320)
vidStreamL.set(4,240)
vidStreamL.set(cv2.CAP_PROP_FPS,5)
vidStreamR = cv2.VideoCapture(1)  # index of your right camera
vidStreamR.set(3,320)
vidStreamR.set(4,240)
vidStreamR.set(cv2.CAP_PROP_FPS,5)




while (1):
    
    retL, img1 = vidStreamL.read()
    height, width, depth  = img1.shape
    retR, img2 = vidStreamR.read()
    cv2.imshow('image1', img1)
    cv2.imshow('image2', img2)
   
    k = cv2.waitKey(5) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()
cv2.waitKey(5) 
