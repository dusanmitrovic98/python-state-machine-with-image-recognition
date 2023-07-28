import pyautogui

from logger import log


def type_username(username):
        pyautogui.typewrite(username)
        log("Typed random username.")