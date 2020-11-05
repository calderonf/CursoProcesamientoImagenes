#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2
cap = cv2.VideoCapture(2)# 0 es la primera camara listada en su sistema

kernel=np.ones((3,3),np.float32)
kernel[0,0]=1
kernel[0,1]=0
kernel[0,2]=-1
kernel[1,0]=2
kernel[1,1]=0
kernel[1,2]=-2
kernel[2,0]=1
kernel[2,1]=0
kernel[2,2]=-1
while(True):
	ret, frame = cap.read()# por favor revise que el cuadro es valido, si no es valido termine el loop usando break.
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	dst1 = cv2.filter2D(frame,-1,kernel)# jugamos con ese -1 cv2.CV_8U
	
	sobel= cv2.Sobel(frame, cv2.CV_16S,1,0)
	sobel2= cv2.Sobel(frame, cv2.CV_16S,0,1)
	sobel3=np.absolute(sobel)
	sobel4=np.absolute(sobel2)
	sobel5=cv2.add(sobel3,sobel4)


	sobel6=np.uint8(sobel5)
	cv2.imshow('frame',frame)


	cv2.imshow('Sobelx_solopositivo',dst1)
	cv2.imshow('sobel_function',sobel6)

	if cv2.waitKey(3) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)# en sistemas posix (linux/mac) es necesario hacer esto para que funcione destroyAllWindows
