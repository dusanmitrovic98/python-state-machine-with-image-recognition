import numpy as np
import pyautogui
import cv2

from config import THRESHOLD
from logger import log

def recognize_image(state):
    try:
        state.on_enter()
        for index, image in enumerate(state.images):
            if image is None:
                continue
            print("Image path: " + state.image_paths[index])
            screenshot = pyautogui.screenshot()
            screenshot_np = np.array(screenshot)
            screenshot_cv2 = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
            result = cv2.matchTemplate(screenshot_cv2, image, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)
            locations = np.where(result >= THRESHOLD)
            if locations[0].size > 0:
                state.execute_action(max_loc, index)
                log("Recognized image with index: " + str(index))
                return (True, index)
            log("Image not recognized with index: " + str(index))
        return (False, -1)
    except ValueError as ve:
        print("ValueError:", ve)
    except FileNotFoundError as fe:
        print("FileNotFoundError:", fe)
    except Exception as e:
        print("An unexpected error occurred:", e)