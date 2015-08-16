# security camera
# approach based on
# https://realpython.com/blog/python/fingerprinting-images-for-near-duplicate-detection/

from PIL import Image, ImageOps
from scipy import spatial
import imagehash
import os, sys

def keep_dissimilar(image1, image2, threshold):
  # takes 2 PIL Image objects
  # threshold is the max acceptable Hamming distance
  # returns image2 only if dissimilar enough
  image1_hash = list(str(imagehash.dhash(image1)))
  image2_hash = list(str(imagehash.dhash(image2)))
  print image1_hash
  print image2_hash
  dist = spatial.distance.hamming(
          image1_hash, image2_hash)
  print dist
  if dist >= threshold:
    return image2
  else:
    return False

im = Image.open("serval.jpg")
im2 = Image.open("serval.jpg").rotate(45)

file = keep_dissimilar(im, im2, 2)
