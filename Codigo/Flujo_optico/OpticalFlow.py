#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 21:50:28 2019

@author: francisco
"""

import numpy as np
import cv2 
#cap = cv2.VideoCapture("../../Semana_10/DJI_00096.MP4")#)#"../../Semana_10/DJI_00096.MP4"
cap = cv2.VideoCapture(1)#)#"../../Semana_10/DJI_00096.MP4"
# params for ShiTomasi corner detection
PointsMax=300
feature_params = dict( maxCorners = PointsMax,
                       qualityLevel = 0.01,
                       minDistance = 7,
                       blockSize = 7 )
# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
# Create some random colors
color = np.random.randint(0,255,(PointsMax,3))
# Take first frame and find corners in it
ret, old_frame = cap.read()
#old_frame = cv2.resize(old_frame_o, (1920,1080), interpolation = cv2.INTER_AREA)
old_gray= cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params) # ver https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
#usa algoritmo de shi tomassi Good Features to Track. Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition
# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)

    
for i in range (0,299):
    ret,frame = cap.read()
    
while(1):
    ret,frame = cap.read()
    #frame = cv2.resize(frame_o, (1920,1080), interpolation = cv2.INTER_AREA)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # calculate optical flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    # ver https://docs.opencv.org/4.0.0/dc/d6b/group__video__track.html#ga473e4b886d0bcc6b65831eb88ed93323
    # Select good points
    good_new = p1[st==1]
    good_old = p0[st==1]
    # draw the tracks
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
        frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
    img = cv2.add(frame,mask)
    cv2.imshow('frame',img)
    cv2.imshow('mask',mask)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
    # Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1,1,2)
    if k== ord('n') or k== ord('N'):
        p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
        mask = np.zeros_like(old_frame)


cv2.destroyAllWindows()
cv2.waitKey(1)
cap.release()