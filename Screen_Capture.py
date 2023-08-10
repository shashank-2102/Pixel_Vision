import numpy as np
import mss

class ScreenCapture:
    def __init__(self):
        self.monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}  # Adjust these values

    def get_screenshot(self):
        with mss.mss() as sct:
            screenshot = sct.shot(mon=1)  # Capture the primary monitor
            img = np.array(screenshot)
            return img

# Example usage
if __name__ == "__main__":
    screen_capture = ScreenCapture()
    screenshot = screen_capture.get_screenshot()
    # Now you can use the 'screenshot' numpy array as needed
