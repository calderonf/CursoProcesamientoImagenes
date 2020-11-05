import cv2
import numpy as np

BLUE = [255,0,0]

img1 = cv2.imread('ejemplos/opencv-logo2.png')

replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

cv2.imshow('ORIGINAL',img1)
cv2.imshow('REPLICATE',replicate)
cv2.imshow('REFLECT',reflect)
cv2.imshow('REFLECT_101',reflect101)
cv2.imshow('WRAP',wrap)
cv2.imshow('CONSTANT',constant)
cv2.waitKey(0)
cv2.destroyAllWindows()