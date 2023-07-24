from flask import Flask, render_template, request, redirect, url_for, jsonify
import cv2
import numpy as np
import pyautogui
import time
import threading

app = Flask(__name__)

# Define the list of states and their corresponding images, actions, and IDs
states = [
         {
        "id": 0,
        "image_path": "", 
        "action": "No action",
        "duration": 5,  
        "next_state": 1  
    },
    {
        "id": 1,
        "image_path": "C:\\Users\\BK2O198\\Documents\\Workstation\\automation\\image-to-click.jpg",
        "action": "Click",
        "duration": 1,  
        "next_state": 2  
    },
    {
        "id": 2,
        "image_path": "C:\\Users\\BK2O198\\Documents\\Workstation\\automation\\image-to-click.jpg",
        "action": "Click",
        "duration": 1,
        "next_state": 1  
    },
    {
        "id": 99,
        "image_path": "",  
        "action": "End automation",
        "duration": 0,  
        "next_state": -1 
    }
]

# Global variable to keep track of the automation thread
automation_thread = None
stop_automation_flag = False

def find_and_click(image_path):
    if image_path:
        try:
            if not image_path:
                raise ValueError("Image path is empty. No action performed for this state.")
        
            target_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            if target_image is None:
                raise FileNotFoundError(f"Image not found or invalid format: {image_path}")

            # Get the screen resolution
            screen_width, screen_height = pyautogui.size()
