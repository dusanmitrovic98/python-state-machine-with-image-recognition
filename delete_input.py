import pyautogui
import time

def delete_input(times):
    for _ in range(times):
        pyautogui.press('backspace')
        time.sleep(0.05)