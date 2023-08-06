import pyautogui

from logger import log


def held_mouse_down(values):
    target_image, start_x, start_y = values
    start_x += target_image.shape[1] // 2
    start_y += target_image.shape[0] // 2
    destination_x = start_x
    destination_y = start_y + 600
    pyautogui.mouseDown(x=start_x, y=start_y)
    pyautogui.moveTo(destination_x, destination_y, duration=1.0)
    pyautogui.mouseUp()
    log("Held Mouse Down action performed successfully.")