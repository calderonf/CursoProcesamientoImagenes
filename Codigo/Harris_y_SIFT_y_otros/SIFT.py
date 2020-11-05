#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 07:54:06 2019

@author: francisco
"""

import numpy as np
import cv2
import time
img = cv2.imread('mariposa.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#sift = cv2.xfeatures2d.SIFT_create(50)#nfeatures=50
sift = cv2.SIFT_create(50)#nfeatures=50


start = time.time()
kp,des = sift.detectAndCompute(gray,None)
end = time.time()
print((end - start)*1000)



img=cv2.drawKeypoints(gray,kp,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


cv2.imshow("FeatureSIFT",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)