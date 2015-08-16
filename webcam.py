from cv2 import VideoCapture, waitKey, imshow, imwrite, namedWindow, destroyWindow, \
  CV_WINDOW_AUTOSIZE

# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    namedWindow("cam-test", CV_WINDOW_AUTOSIZE)
    imshow("cam-test", img)
    waitKey(0)
    destroyWindow("cam-test")
    imwrite("filename.jpg", img) #save image
