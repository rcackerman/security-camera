# security-camera
Bespoke security camera

> brew install opencv

May need to do something like:
ln -s /usr/local/Cellar/opencv/2.4.10/lib/python2.7/site-packages/cv.py cv.py
ln -s /usr/local/Cellar/opencv/2.4.10/lib/python2.7/site-packages/cv2.so cv2.so


Then keep going:

> mkvirtualenv camera --no-site-packages
> pip install - r requirements.txt

