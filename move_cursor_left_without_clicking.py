import pyautogui

from logger import log

def move_cursor_left_without_clicking(values):
    x, y = values
    x -= 140
    pyautogui.moveTo(x, y)
    log("Move cursor left action performed successfully.")