
import os

import pyautogui
import time
import winsound  # Use playsound or similar for non-Windows systems

# Path to the image you want to detect
target_image = 'target.png'
found_sound = 'Sonic Ring.wav'

nodeFound = False

while True:
    # confidence requires 'opencv-python' installed
    try:
    # proceed with actions
        location = pyautogui.locateOnScreen(target_image, confidence=0.8)
        if location and not nodeFound:
            print("Image detected!")
            winsound.PlaySound(found_sound, winsound.SND_FILENAME | winsound.SND_ASYNC)
            nodeFound = True
            time.sleep(5)  # Wait for 5 seconds before checking again
    except pyautogui.ImageNotFoundException:
        nodeFound = False
    time.sleep(1) # Check every second