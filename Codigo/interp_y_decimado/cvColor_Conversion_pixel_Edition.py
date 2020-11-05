#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 21:12:25 2020

@author: francisco
"""
import numpy as np
import cv2
img = cv2.imread('barn_owl.jpg')
imgGRAY=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#cv2.namedWindow ("Original",banderas)

cv2.imshow("Original",img)
cv2.imshow("RGB",imgRGB)
cv2.imshow("GRAY",imgGRAY)

cv2.waitKey(0)

pixel=img[0,0,0]
print(pixel)



