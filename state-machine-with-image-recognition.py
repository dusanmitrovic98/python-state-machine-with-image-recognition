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

        # Set a threshold for a good match (you can adjust this as needed)
        threshold = 0.5 

        if max_val >= threshold:
            # Get the coordinates of the best match
            x, y = max_loc

            # Move the mouse to the center of the matched image and click
            x += target_image.shape[1] // 2
            y += target_image.shape[0] // 2
            pyautogui.moveTo(x, y)
            pyautogui.click()
            print("Click action performed successfully.")
        else:
            print("Target image not found on the screen.")
    except ValueError as ve:
        print("ValueError:", ve)
    except FileNotFoundError as fe:
        print("FileNotFoundError:", fe)
    except Exception as e:
        print("An unexpected error occurred:", e)

def automate_states(states):
    global stop_automation_flag

    current_state_id = 0  

    while True:
        if stop_automation_flag:
            print("Automation stopped.")
            break

        # Find the current state based on the ID
        current_state = next((state for state in states if state["id"] == current_state_id), None)

        if current_state is None:
            print(f"State with ID {current_state_id} not found.")
            break

        image_path = current_state["image_path"]
        action = current_state["action"]
        duration = current_state["duration"]
        next_state_id = current_state["next_state"]

        print(f"State ID: {current_state_id} -> Image: {image_path} -> Action: {action}")
        time.sleep(1)  # Wait for 1 second before starting the countdown

        for remaining_time in range(duration, 0, -1):
            if stop_automation_flag:
                print("Automation stopped.")
                break

    global stop_automation_flag

    current_state_id = 0  

    while True:
        if stop_automation_flag:
            print("Automation stopped.")
            break

        # Find the current state based on the ID
        current_state = next((state for state in states if state["id"] == current_state_id), None)

        if current_state is None:
            print(f"State with ID {current_state_id} not found.")
            break

        image_path = current_state["image_path"]
        action = current_state["action"]
        duration = current_state["duration"]
        next_state_id = current_state["next_state"]

        print(f"State ID: {current_state_id} -> Image: {image_path} -> Action: {action}")
        time.sleep(1)  # Wait for 1 second before starting the countdown

        for remaining_time in range(duration, 0, -1):
            if stop_automation_flag:
                print("Automation stopped.")
                break

            print(f"Next action in {remaining_time} seconds...")
            time.sleep(1)

        if not stop_automation_flag:
            find_and_click(image_path)

        # Move to the next state based on the next_state ID
        current_state_id = next_state_id

        if current_state_id == -1:
            print("End state reached. Automation stopped.")
            break

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return redirect(url_for("start_automation"))
    # return render_template("index.html")
    return INDEX_PAGE

@app.route("/start")
def start_automation():
    global automation_thread, stop_automation_flag

    # Set stop_automation_flag to False before starting automation
    stop_automation_flag = False

    # Start the automation in a new thread
    automation_thread = threading.Thread(target=automate_states, args=(states, ))
    automation_thread.start()

    return jsonify({"status": "success", "message": "Automation started."})

@app.route("/stop")
def stop_automation():
    global automation_thread, stop_automation_flag

