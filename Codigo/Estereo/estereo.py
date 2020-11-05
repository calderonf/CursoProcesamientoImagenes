import numpy as np
import cv2

print ("Iniciando\n")

numBoards = 30  #how many boards would you like to find
board_w = 11#7
board_h = 6#6
square_size=40.0

board_sz = (board_w,board_h)
board_n = board_w*board_h

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Arrays to store object points and image points from all the images.
object_points = [] # 3d point in real world space
imagePoints1 = [] # 2d points in image plane.
imagePoints2 = [] # 2d points in image plane.

corners1 = []
corners2 = []

obj = np.zeros((np.prod(board_sz), 3), np.float32)
obj[:, :2] = np.indices(board_sz).T.reshape(-1, 2)
obj *= square_size


vidStreamL = cv2.VideoCapture(1)  # index of your left camera
vidStreamL.set(3,640)
vidStreamL.set(4,480)
vidStreamL.set(cv2.CAP_PROP_FPS,30)
vidStreamR = cv2.VideoCapture(0)  # index of your right camera
vidStreamR.set(3,640)
vidStreamR.set(4,480)
vidStreamR.set(cv2.CAP_PROP_FPS,30)
success = 0
k = 0
found1 = False
found2 = False
countimg=0

while (success < numBoards):

   retL, img1 = vidStreamL.read()
   height, width, depth  = img1.shape
   retR, img2 = vidStreamR.read()
   #resize(img1, img1, Size(320, 280));
   #resize(img2, img2, Size(320, 280));
   gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
   gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

   found1, corners1 = cv2.findChessboardCorners(gray1, board_sz)
   found2, corners2 = cv2.findChessboardCorners(gray2, board_sz)

   if (found1):
       cv2.cornerSubPix(gray1, corners1, (11, 11), (-1, -1),criteria)
       cv2.drawChessboardCorners(img1, board_sz, corners1, found1)

   if (found2):
       cv2.cornerSubPix(gray2, corners2, (11, 11), (-1, -1), criteria)
       cv2.drawChessboardCorners(img2, board_sz, corners2, found2)

   cv2.imshow('imageLeft_', img1)
   cv2.imshow('imageRight_', img2)

   k = cv2.waitKey(2)&0xFF
   print (k)
   if (k==ord('q')):# q
       break
   if ( k==ord('c') and found1 != 0 and found2 != 0):# (space)
       cv2.imwrite("ImagenL"+str(countimg)+".png",gray1)
       cv2.imwrite("ImagenR"+str(countimg)+".png",gray2)
       countimg=countimg+1
       imagePoints1.append(corners1);
       imagePoints2.append(corners2);
       object_points.append(obj);
       print ("Corners stored\n")
       success+=1
       k = cv2.waitKey(1500)&0xFF
       if (success >= numBoards):
           break

cv2.destroyAllWindows()
print ("Starting Stereo Calibration\n")
cameraMatrix1 = np.array([[987.6648212,0.,660.59255412],[0.,987.72551541,360.03842397],[0.,0.,1.]])
cameraMatrix2 = np.array([[987.6648212,0.,660.59255412],[0.,987.72551541,360.03842397],[0.,0.,1.]])

distCoeffs1 =  np.array([[ 0.08480433,0.37944639,-0.00166292,0.00301877,0.44198356]])
distCoeffs2 =  np.array([[ 0.08480433,0.37944639,-0.00166292,0.00301877,0.44198356]])

retval, cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, R, T, E, F = cv2.stereoCalibrate(object_points, imagePoints1, imagePoints2, cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, (width, height))
## , cv2.cvTermCriteria(cv2.CV_TERMCRIT_ITER+cv2.CV_TERMCRIT_EPS, 100, 1e-5),   cv2.CV_CALIB_SAME_FOCAL_LENGTH | cv2.CV_CALIB_ZERO_TANGENT_DIST)
#cv2.cv.StereoCalibrate(object_points, imagePoints1, imagePoints2, pointCounts, cv.fromarray(K1), cv.fromarray(distcoeffs1), cv.fromarray(K2), cv.fromarray(distcoeffs2), imageSize, cv.fromarray(R), cv.fromarray(T), cv.fromarray(E), cv.fromarray(F), flags = cv.CV_CALIB_FIX_INTRINSIC)
#FileStorage fs1("mystereocalib.yml", FileStorage::WRITE);
# fs1 << "CM1" << CM1;
#fs1 << "CM2" << CM2;
# #fs1 << "D1" << D1;
#fs1 << "D2" << D2;
#fs1 << "R" << R;
#fs1 << "T" << T;
#fs1 << "E" << E;
#fs1 << "F" << F;
print ("Done Calibration\n")
print ("Starting Rectification\n")
R1 = np.zeros(shape=(3,3))
R2 = np.zeros(shape=(3,3))
P1 = np.zeros(shape=(3,4))
P2 = np.zeros(shape=(3,4))

cv2.stereoRectify(cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2,(width, height), R, T, R1, R2, P1, P2, Q=None, flags=cv2.CALIB_ZERO_DISPARITY, alpha=-1, newImageSize=(0,0))

#fs1 << "R1" << R1;
#fs1 << "R2" << R2;
#fs1 << "P1" << P1;
#fs1 << "P2" << P2;
#fs1 << "Q" << Q;

print ("Done Rectification\n")
print ("Applying Undistort\n")



map1x, map1y = cv2.initUndistortRectifyMap(cameraMatrix1, distCoeffs1, R1, P1, (width, height), cv2.CV_32FC1)
map2x, map2y = cv2.initUndistortRectifyMap(cameraMatrix2, distCoeffs2, R2, P2, (width, height), cv2.CV_32FC1)

print ("Undistort complete\n")

while(True):
    retL, img1 = vidStreamL.read()
    retR, img2 = vidStreamR.read()
    imgU1 = np.zeros((height,width,3), np.uint8)
    imgU1 = cv2.remap(img1, map1x, map1y, cv2.INTER_LINEAR, imgU1, cv2.BORDER_CONSTANT, 0)
    imgU2 = cv2.remap(img2, map2x, map2y, cv2.INTER_LINEAR)
    cv2.imshow("imageL", img1);
    cv2.imshow("imageR", img2);
    cv2.imshow("image1L", imgU1);
    cv2.imshow("image2R", imgU2);
    k = cv2.waitKey(5);
    if(k==27):
        break;
