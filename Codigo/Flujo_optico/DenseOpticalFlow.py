#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 22:43:34 2019

@author: francisco
"""

import cv2 as cv2
import numpy as np
cap = cv2.VideoCapture("../../Semana_10/DJI_00096.MP4")
#cap = cv2.VideoCapture(2)
ret, frame1 = cap.read()
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255
while(1):
    ret, frame2 = cap.read()
    next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    
    flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5,3, 15, 3, 5, 1.2, 0)

    #Para visualizar
    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])#promero y y luego x
    hsv[...,0] = ang*180/np.pi/2
    hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
    bgr = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

    cv2.imshow('frame2',bgr)
    cv2.imshow('Video',frame2)
    k = cv2.waitKey(1) & 0xff
    if k == 27:#Sale con escape
        break
    elif k == ord('s'):
        cv2.imwrite('opticalfb.png',frame2)
        cv2.imwrite('opticalhsv.png',bgr)
    prvs = next

print(type(flow))
print(flow.shape)

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)