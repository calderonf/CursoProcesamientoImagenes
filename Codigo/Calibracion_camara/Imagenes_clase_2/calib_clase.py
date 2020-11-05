#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:38:57 2019

@author: francisco
"""

import numpy as np
import cv2 as cv2
import glob
DIMX=8
DIMY=5
square_size=25

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)

objp = np.zeros((DIMY*DIMX,3), np.float32)
objp[:,:2] = np.mgrid[0:DIMX,0:DIMY].T.reshape(-1,2)
objp *= square_size
print("se crea los puntos origen note la escala que es 1 en este caso aca se multiplica por el tamanio del rectangulo en milimetros, metros, centimetros o bananos")
print(objp)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('*.bmp')

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (DIMX,DIMY),None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (DIMX,DIMY), corners2,ret)
        cv2.imshow('img',img)
        cv2.waitKey(3  )

cv2.destroyAllWindows()
cv2.waitKey(1)
print(imgpoints)


ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

print(mtx)
print(type(mtx))
print(dist)
print(type(dist))
# termina la calibración




# Inicia etapa de usuario

img = cv2.imread('2020-09-21_17-57-45.bmp')
h,  w = img.shape[:2]
newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),0,(w,h))
# undistort
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

# crop the image
x,y,w,h = roi
dst = dst[y:y+h, x:x+w]
cv2.imwrite('calibresult1.png',dst)

# undistort
mapx,mapy = cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)
dst = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)

# crop the image
x,y,w,h = roi
#dst = dst[y:y+h, x:x+w]
cv2.imwrite('calibresult2.png',dst)
mean_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i],imgpoints2, cv2.NORM_L2)/len(imgpoints2)
    mean_error += error

print ("total error: ", mean_error/len(objpoints))

print ("matriz inversa ")
mtx_inv=np.linalg.inv(mtx)


