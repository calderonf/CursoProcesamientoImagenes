#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
remitirse a 
https://docs.opencv.org/4.0.1/da/d54/group__imgproc__transform.html#ga5bb5a1fea74ea38e1a5445ca803ff121
para ver las banderas de interpolación y sus características.
"""

import numpy as np
import cv2 as cv
img = cv.imread('small_owl.jpg')
scalex = 3
scaley = 3
res = cv.resize(img,None,fx=scalex, fy=scaley, interpolation = cv.INTER_NEAREST)

cv.imshow("peque",img)
cv.imshow("interpolado",res)
cv.waitKey(0)

cv.destroyAllWindows()

img2 = cv.imread('barn_owl.jpg')

# otro método de hacer lo mismo, simplemente cambia el llamado de la sobrecarga de la función. 
height, width = img2.shape[:2]#equivalente a 0:2 retorna elementos 0 y 1
scalefactor=0.5
res2 = cv.resize(img2,(int(scalefactor*width), int(scalefactor*height)), interpolation = cv.INTER_NEAREST)

cv.imshow("Original",img2)
cv.imshow("decimado",res2)
cv.waitKey(0)


cv.destroyAllWindows()

# Tarea: 
#
# 1. del link (https://en.wikipedia.org/wiki/Bicubic_interpolation) haga un resumen de por lo menos 60 palabras de los métodos:
# INTER_NEAREST, INTER_LINEAR, INTER_CUBIC.
# 2. Cambiar los métodos de interpolado y comparar el resultado con TODOS los posibles listados en el link. (INTER_NEAREST, INTER_LINEAR, INTER_CUBIC, INTER_AREA, INTER_LANCZOS4,INTER_LINEAR_EXACT)
#   Use imwrite(filename, img[, params]) para guardar imágenes .png del resultado, (use PNG no jpg por aquello de la pérdida)
#   compare todos los métodos mediante una tabla o similar y con por lo menos un párrafo de 25 palabras por imágen.
# 3. ¿por qué INTER_AREA es el método preferido para decimación (30 palabras)? ¿Explique el fenómeno de moiré(30 palabras)?
# 4. Corra los 3 ejemplos de umbralización en la web 
# https://docs.opencv.org/3.4.0/d7/d4d/tutorial_py_thresholding.html
# Use una imagen propia tomada con la cámara de su celular de un recorte de periodico para separar las letras del fondo, que método es el mejor para este objetivo.
