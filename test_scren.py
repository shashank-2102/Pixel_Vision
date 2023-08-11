import dxcam
import time 
import cv2 as cv
import numpy as np
import os
import time
from Screen_Capture_copy import ScreenCapture
from PIL import Image

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

camera = dxcam.create() 
frame = camera.grab()

camera.start()  # Optional argument to capture a region
camera.is_capturing  # True
Image.fromarray(frame).show()
time.sleep(5)
camera.stop()
camera.is_capturing  # False

