#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 22:23:47 2019

@author: francisco
"""

import numpy as np
import cv2 as cv
import time
filename = 'mariposa.jpg'
img = cv.imread(filename)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

start = time.time()
corners = cv.goodFeaturesToTrack(gray,50,0.01,10)
corners = np.int0(corners)
print(len(corners))
for i in corners:
    x,y = i.ravel()
    cv.circle(img,(x,y),3,255,-1)

end = time.time()
print((end - start)*1000)
cv.imshow('dst',img)

cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)