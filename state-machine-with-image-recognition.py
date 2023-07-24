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
