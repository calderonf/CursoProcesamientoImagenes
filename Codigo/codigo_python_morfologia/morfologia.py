#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 08:03:54 2019

@author: francisco
"""

import cv2
import numpy as np

imagen='imagen_negativo.jpg'
#imagen='imagen.jpg' # compare los resultados del gradiente morfologico de esta con la anterior
#imagen='paris.jpg'
#imagen='lena.jpg'


img = cv2.imread(imagen,0)# importarla en escala de grices.
#img = cv2.imread(imagen,1)# importarla en color "no todas las operaciones lo soportan, ver cv.MORPH_HITMISS ".
print(img.shape)
if img is None:
    print("error en imagen")
    exit()


shape=cv2.MORPH_CROSS
ksize=(5,5)
kernel=cv2.getStructuringElement(shape,ksize)#ancla en centro por defecto.
"""
Para usar un kernel por defecto usar funcion getStructuringElement:
    https://docs.opencv.org/4.0.0/d4/d86/group__imgproc__filter.html#gac342a1bb6eabf6f55c803b09268e36dc


Los tipos de formas morfologicas soportadas por defecto:
    https://docs.opencv.org/4.0.0/d4/d86/group__imgproc__filter.html#gac2db39b56866583a95a5680313c314ad
    
O se puede crear a mano por ejemplo:
kernel = np.ones((5,5),np.uint8)
"""
erosion = cv2.erode(img,kernel,iterations = 1)

dilation = cv2.dilate(img,kernel,iterations = 1)

"""
Ademas de erosion y dilatacion que tienen sus propias funciones,
también están soportadas otras por una funcion independiente de morfologia llamada morphologyEx:
    https://docs.opencv.org/4.0.0/d4/d86/group__imgproc__filter.html#ga67493776e3ad1a3df63883829375201f

los tipos de operaciones morfologicas optimizadas soportadas por morphologyEx son:
    
    https://docs.opencv.org/4.0.0/d4/d86/group__imgproc__filter.html#ga7be549266bad7b2e6a04db49827f9f32
"""


opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

that = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)


hitmiss = cv2.morphologyEx(img, cv2.MORPH_HITMISS, kernel)


cv2.imshow("Original",img)

cv2.imshow("erosion",erosion)

cv2.imshow("dilation",dilation)


cv2.imshow("opening",opening)

cv2.imshow("closing",closing)

cv2.imshow("gradient",gradient)

cv2.imshow("tophat",that)

cv2.imshow("blackhat",blackhat)

cv2.imshow("hitmiss",hitmiss)





cv2.waitKey(0)

cv2.destroyAllWindows()