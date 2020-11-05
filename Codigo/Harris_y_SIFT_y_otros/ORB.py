#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 21:54:35 2019

@author: francisco
"""
import numpy as np
import cv2
import time

img = cv2.imread('mariposa.jpg',0)

orb = cv2.ORB_create(50)

start = time.time()
key_points, description = orb.detectAndCompute(img, None)
end = time.time()
print((end - start)*1000)

imgkeypoints_2 = cv2.drawKeypoints(img, key_points, img, flags=cv2 .DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("FeatureORB",imgkeypoints_2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)