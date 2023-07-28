import pyautogui
import random

from logger import log


def move_cursor(values):
    x, y = values
    if random.randint(1, 2) is 1:
        x -= 140
    else:
        x += 140
    pyautogui.moveTo(x, y)
    pyautogui.click()
    log("Move cursor action performed successfully.")