
import os

import pyautogui
import time
import winsound  # Use playsound or similar for non-Windows systems

# Path to the image you want to detect
target_image = 'target.png'

nodeFound = False

while True:
    print(os.getcwd())
    # confidence requires 'opencv-python' installed
    try:
    # proceed with actions
        location = pyautogui.locateOnScreen(target_image, confidence=0.8)
        if location and not nodeFound:
            print("Image detected!")
            winsound.Beep(1000, 1000)  # Frequency 1000Hz, Duration 1000ms
            nodeFound = True
            time.sleep(5)  # Wait for 5 seconds before checking again
    except pyautogui.ImageNotFoundException:
        print("Image not found on screen!.")
        nodeFound = False
    time.sleep(1) # Check every second