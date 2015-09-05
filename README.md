# security-camera
Bespoke security camera

## Installation instructions

1. install cv2
    ```
    brew tap homebrew/science
    brew install opencv
    ```
2. install required packages
    ```
    pip install -r requirements.txt
    ```

Note: as long as you use python installed via Homebrew, opencv should work automatically. If you use another version, you will have to look for your pythonpath and symlink opencv.
```
ln -s /usr/local/Cellar/opencv/2.4.9/lib/python2.7/site-packages/cv.py <PYTHONPATH>/cv.py
ln -s /usr/local/Cellar/opencv/2.4.9/lib/python2.7/site-packages/cv2.so <PYTHONPATH>/cv2.so
```

If you have used a virtualenv, you can use the following directions:
```
cd ~/.virtualenvs/security-camera/lib/python2.7/site-packages
ln -s /usr/local/Cellar/opencv/2.4.12/lib/python2.7/site-packages/cv.py cv.py
ln -s /usr/local/Cellar/opencv/2.4.12/lib/python2.7/site-packages/cv2.so cv2.so
```
