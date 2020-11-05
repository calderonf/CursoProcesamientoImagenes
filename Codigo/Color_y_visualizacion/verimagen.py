import numpy as py
import cv2 as cv
img=cv.imread('ejemplos/lena.jpg')

if img is not None:
    print('La imagen fue cargada correctamente')
    cv.imshow('Ventana',img)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print('La imagen no fue cargada correctamente.')
print('Saliendo')