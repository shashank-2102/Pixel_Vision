import cv2 as cv
import numpy as np
import os
import pyautogui
from time import time

os.chdir(os.path.dirname(os.path.abspath(__file__))) #change to cwd

loop_time = time()

while(True):
    screenshot_raw = pyautogui.screenshot()
    screenshot_unc = np.array(screenshot_raw)
    screenshot = cv.cvtColor(screenshot_unc, cv.COLOR_RGB2BGR)

    cv.imshow('Comp Vision', screenshot) 

    print(f"FPS{1/(time()-loop_time)}")
    loop_time = time()

    if cv.waitKey(1) == ord('o'):#wait and exit key for loop
        cv.destroyAllWindows()
        break

