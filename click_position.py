import pyautogui

from logger import log


def click(values):
    target_image, x, y = values
    x += target_image.shape[1] // 2
    y += target_image.shape[0] // 2
    pyautogui.moveTo(x, y)
    pyautogui.click()
    log("Click action performed successfully.")