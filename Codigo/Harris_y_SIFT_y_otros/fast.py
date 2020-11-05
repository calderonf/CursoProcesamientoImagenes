#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 22:29:53 2019

@author: francisco
"""

import numpy as np
import cv2 as cv
import time

img = cv.imread('mariposa.jpg',0)
# Initiate FAST object with default values
fast = cv.FastFeatureDetector_create()
# find and draw the keypoints



start = time.time()
kp = fast.detect(img,None)
end = time.time()
print((end - start)*1000)
print(len(kp))
#img2 = cv.drawKeypoints(img, kp, None, color=(255,0,0))
for marker in kp:
	img = cv.drawMarker(img, tuple(int(i) for i in marker.pt), color=(0, 255, 0))

cv.imshow('dst',img)

cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)