import pyautogui

from logger import log


def type_username(username):
        pyautogui.typewrite(username)
        log("Typed random username.")

def type_username_01():
        pyautogui.typewrite("bk20198")
        log("Typed random username bk20198.")