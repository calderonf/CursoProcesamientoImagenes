#!/usr/bin/env python.
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:52:57 2019

@author: francisco
"""
import numpy as np
import datetime as dt
fps=30
Tiempom3dB=10#segundos para que la salida caiga a 3 dB con respecto a la entrada
fcorte=1/Tiempom3dB
print("polo en :", 2*np.pi*fcorte)
alpha=1-np.exp(-2*np.pi*fcorte*(1/fps))#e^(-(constante)*Ts) donde constante esta en radianes/seg y Ts esta en segundos
import cv2
import numpy as np
c = cv2.VideoCapture(2)# "DJI_00096.MP4", "vehicular.avi" 
_,f = c.read()
avg1 = np.float32(f)
while(1):
    n1=dt.datetime.now()
    imext,f = c.read()
    if not imext:
        break
    cv2.accumulateWeighted(f,avg1,alpha)#cambiar este valor multiplicando o dividiendo por un factor constante ej 2, 1.5 a 0.01
    res1 = cv2.convertScaleAbs(avg1)
    cv2.imshow('img',f)
    cv2.imshow('avg1',res1)
    resta	=	cv2.absdiff(	f, res1)
    cv2.imshow('resta',resta)


    n2=dt.datetime.now()
    halted=int(1000*(1/fps)-(n2-n1).microseconds/1000)#aquí mido el tiempo que toma el proceso, y este se lo resto al tiempo correcto de reproducción de video, esto para reproducir en tiempo real el video.
    if halted<=0:#si el tiempo de proceso es mayor del tiempo del video uso un halted positivo 
        halted=1
    k = cv2.waitKey(halted)&0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cv2.waitKey(2)
c.release()
cv2.waitKey(2)