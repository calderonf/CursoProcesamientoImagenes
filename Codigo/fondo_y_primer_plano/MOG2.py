#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 08:49:06 2019
@author: Francisco Calderon
"""
import cv2
import numpy as np

METODO=8# 1,2... 10
 
cap = cv2.VideoCapture("DJI_00096.MP4")
#subtractor = cv2.createBackgroundSubtractorMOG2(history=20, varThreshold=25, detectShadows=True)
if METODO==1:
    subtractor = cv2.createBackgroundSubtractorKNN()
    print ("metodo = cv2.createBackgroundSubtractorKNN()")
elif METODO==2:
    subtractor = cv2.createBackgroundSubtractorMOG2()
    print ("metodo = cv2.createBackgroundSubtractorMOG2()")
elif METODO==3:
    subtractor=cv2.bgsegm.createBackgroundSubtractorLSBP(nSamples=20, LSBPRadius=16,Tlower=2.0,Tupper=32.0,Tinc=1.0,Tdec=0.05,Rscale=10.0,Rincdec= 0.005,LSBPthreshold=8)# parametros 'LSBP-quality'
    print ("metodo = cv2.bgsegm.createBackgroundSubtractorLSBP('LSBP-quality')")
elif METODO==4:
    subtractor = cv2.bgsegm.createBackgroundSubtractorGMG()
    print ("metodo = cv2.bgsegm.createBackgroundSubtractorGMG()")
elif METODO==5:
    subtractor=cv2.bgsegm.createBackgroundSubtractorMOG()
    print ("metodo = cv2.bgsegm.createBackgroundSubtractorMOG()")
elif METODO==6:
    subtractor=cv2.bgsegm.createBackgroundSubtractorCNT()
    print ("metodo = cv2.bgsegm.createBackgroundSubtractorCNT()")
elif METODO==7:
    subtractor=cv2.bgsegm.createBackgroundSubtractorGSOC()
    print ("metodo = cv2.bgsegm.createBackgroundSubtractorGSOC()")
elif METODO==8:
    subtractor=cv2.bgsegm.createBackgroundSubtractorGSOC(mc=1)# mas lento pero con camera compensation
    print ("metodo = cv2.bgsegm.createBackgroundSubtractorGSOC(mc=1)")
elif METODO==9:
    subtractor=cv2.bgsegm.createBackgroundSubtractorLSBP(nSamples=10, LSBPRadius=16,Tlower=2.0,Tupper=32.0,Tinc=1.0,Tdec=0.05,Rscale=10.0,Rincdec= 0.005,LSBPthreshold=8)# parametros 'LSBP-speed'
    print ("metodo = cv2.bgsegm.createBackgroundSubtractorLSBP('LSBP-speed')")
elif METODO==10:
    subtractor=cv2.bgsegm.createBackgroundSubtractorLSBP(nSamples=20, LSBPRadius=4,Tlower=2.0,Tupper=200.0,Tinc=1.0,Tdec=0.05,Rscale=5.0,Rincdec= 0.05,LSBPthreshold=8)# parametros 'LSBP-vanilla'
    print ("metodo = cv2.bgsegm.createBackgroundSubtractorLSBP('LSBP-vanilla')")
else:
    print("método no implementado se toma createBackgroundSubtractorMOG2")
    subtractor = cv2.createBackgroundSubtractorMOG2()
    print ("metodo cv2.createBackgroundSubtractorMOG2()")

while True:
    _, frame = cap.read()
 
    mask = subtractor.apply(frame)
    
    if METODO==1 or METODO==2 or METODO==3 or METODO==6 or METODO==7 or METODO==8 or METODO==9 or METODO==10:
        bgimg=subtractor.getBackgroundImage()
        cv2.imshow("bg",bgimg)
    
    
    cv2.imshow("Frame", frame)
    cv2.imshow("mask", mask)
 
    key = cv2.waitKey(1)&0xFF
    if key == 27:
        break
 
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)
