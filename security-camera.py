# security camera
# approach based on 
# http://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/

import os, sys
import datetime, time
import cv2

video = cv2.VideoCapture()
first_frame = None

while True:
    # start an endless loop for continual
    # processing

    occupied = False 
    (return_img, frame) = camera.read()
    
    if not return_img:
        break

    
    

