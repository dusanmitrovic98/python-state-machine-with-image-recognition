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
