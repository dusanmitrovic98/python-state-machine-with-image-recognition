from flask import Flask, render_template, request, redirect, url_for, jsonify
import cv2
import numpy as np
import pyautogui
import time
import threading
import os

from states import states
from index import INDEX_PAGE

app = Flask(__name__)

# Global variable to keep track of the automation thread
automation_thread = None
stop_automation_flag = False

def find_and_click(image_path):
    try:
        if not image_path:
            raise ValueError("Image path is empty. No action performed for this state.")
        
        target_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if target_image is None:
            raise FileNotFoundError(f"Image not found or invalid format: {image_path}")

        # Get the screen resolution
        screen_width, screen_height = pyautogui.size()

        # Take a screenshot of the screen and convert it to grayscale
        screenshot = pyautogui.screenshot(region=(0, 0, screen_width, screen_height))
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

        # Perform template matching to find the target image on the screen
        result = cv2.matchTemplate(screenshot, target_image, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

