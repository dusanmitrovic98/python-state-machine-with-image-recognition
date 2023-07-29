import pyautogui
import random

from logger import log


def move_cursor(values):
    x, y = values
    x -= 60
    pyautogui.moveTo(x, y)
    log("Move cursor action performed successfully.")