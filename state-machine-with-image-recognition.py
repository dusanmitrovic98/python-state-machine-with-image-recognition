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
