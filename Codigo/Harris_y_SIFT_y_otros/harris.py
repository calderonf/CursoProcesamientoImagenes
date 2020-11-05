#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 22:13:32 2019

@author: francisco
"""
import numpy as np
import cv2 as cv
import time

filename = 'mariposa.jpg'
img = cv.imread(filename)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)


start = time.time()
gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)#gray,2,3,0.04
#result is dilated for marking the corners, not important
#dst = cv.dilate(dst,None)
# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.1*dst.max()]=[0,0,255]

end = time.time()
print((end - start)*1000)
immin=np.min(dst)
immax=np.max(dst)
dst=((dst-immin)/(immax-immin))*255
cv.imshow("harris",cv.convertScaleAbs(dst))
cv.imshow('dst',img)

cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)
print((end - start)*1000)
