import pyautogui

from logger import log


def type_username(username):
        pyautogui.typewrite(username)
        log("Typed random username.")

def type_username_01():
        pyautogui.typewrite(MY_USERNAME)
        log("Typed random username bk20198.")