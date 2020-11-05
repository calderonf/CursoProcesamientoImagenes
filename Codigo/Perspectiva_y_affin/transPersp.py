# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:51:28 2019

@author: Francisco Calderon
"""

# import the necessary packages
import numpy as np
import cv2
 
def order_points(pts):
	# initialzie a list of coordinates that will be ordered
	# such that the first entry in the list is the top-left,
	# the second entry is the top-right, the third is the
	# bottom-right, and the fourth is the bottom-left
	rect = np.zeros((4, 2), dtype = "float32")
 
	# the top-left point will have the smallest sum, whereas
	# the bottom-right point will have the largest sum
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]
 
	# now, compute the difference between the points, the
	# top-right point will have the smallest difference,
	# whereas the bottom-left will have the largest difference
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]
 
	# return the ordered coordinates
	return rect

def four_point_transform(image, pts):
	# obtain a consistent order of the points and unpack them
	# individually
	rect = order_points(pts)
	(tl, tr, br, bl) = pts
	rect=pts
	# compute the width of the new image, which will be the
	# maximum distance between bottom-right and bottom-left
	# x-coordiates or the top-right and top-left x-coordinates
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = int(np.round(1*max(int(widthA), int(widthB))))
 
	# compute the height of the new image, which will be the
	# maximum distance between the top-right and bottom-right
	# y-coordinates or the top-left and bottom-left y-coordinates
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = int(np.round(1*max(int(heightA), int(heightB))))
 
	# now that we have the dimensions of the new image, construct
	# the set of destination points to obtain a "birds eye view",
	# (i.e. top-down view) of the image, again specifying points
	# in the top-left, top-right, bottom-right, and bottom-left
	# order
	offsetx=maxWidth*2
	offsety=maxHeight*2
	dst = np.array([
		[0+offsetx, 0+offsety],
		[maxWidth - 1+offsetx, 0+offsety],
		[maxWidth - 1+offsetx, maxHeight - 1+offsety],
		[0+offsetx, maxHeight - 1+offsety]], dtype = "float32")
	print(dst)
	# compute the perspective transform matrix and then apply it
	M = cv2.getPerspectiveTransform(rect, dst)
	print(M)
	warped = cv2.warpPerspective(image, M, (5*maxWidth, 5*maxHeight))
 
	# return the warped image
	return warped


#imagen="chessSnake.jpg"           
#pts = np.array([(239, 230), (514,173), (615,337), (274, 431 )], dtype = "float32")
 
imagen="imagen2.jpg"
pts = np.array([(137, 744), (458,571), (708,707), (389, 956 )], dtype = "float32")
 
image = cv2.imread(imagen)
# apply the four point tranform to obtain a "birds eye view" of
# the image
warped = four_point_transform(image, pts)
 
# show the original and warped images
cv2.imshow("Original", image)
cv2.imshow("Warped", warped)

cv2.waitKey(10000000)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)



