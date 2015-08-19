from time import sleep

from cv2 import VideoCapture, imshow, imwrite
import Image
import imagehash
from scipy import spatial

MIN_SUSPICIOUS_DIFF = 0.1
pastPhotos = [] # Queue(maxsize=5)

cam = VideoCapture(0)   # 0 -> index of camera

def take_photo():
    # initialize the camera
    s, img = cam.read()
    if s:    # frame captured without any errors
        print "Took a photo"
        pil_im = Image.fromarray(img)

        if len(pastPhotos) > 1:
            image1_hash = list(str(imagehash.dhash(pil_im)))
            image2_hash = list(str(imagehash.dhash(pastPhotos[len(pastPhotos) - 1])))

            dist = spatial.distance.hamming(image1_hash, image2_hash)
            # print dist

            if dist > MIN_SUSPICIOUS_DIFF:
                print "Cockroach detected!"

        pastPhotos.append(pil_im)

    sleep(0.1)
    take_photo()

take_photo()


'''
If arr is a color image (3D array), convert it to grayscale (2D array).
'''
def to_grayscale(arr):
    if len(arr.shape) == 3:
        return average(arr, -1)  # average over the last axis (color channels)
    else:
        return arr

