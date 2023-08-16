#The following program is configured for HH:MM:SS format only. The alarm would be triggered only when the format is met.

import cv2
import pytesseract
import pyautogui
import numpy as np
import time
import os
import threading
import subprocess
import re  # Import the re module for regular expressions

# Set the path to the Tesseract data directory
tesseract_cmd = '/opt/local/share/tessdata'  # Update with your Tesseract path

def display_notification(title, message):
    subprocess.run(['osascript', '-e', f'display notification "{message}" with title "{title}"'])

# Define the region of interest (ROI) coordinates
roi_coordinates = (785, 779, 2075, 1049)  # Update with your ROI coordinates

# Create the output_image folder if it doesn't exist
#output_folder = os.path.expanduser("~/Desktop/output_image")
# os.makedirs(output_folder, exist_ok=True)

# Wait for 3 seconds before starting
time.sleep(3)

# Initialize previous value
previous_value = None
running = True

def capture_and_process():
    global previous_value, running

    while running:
        # Capture a screenshot of the screen
        screenshot = pyautogui.screenshot()

        # Convert the screenshot to a numpy array
        frame = np.array(screenshot)

        # Convert RGB to BGR (OpenCV format)
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Crop the frame to the ROI
        roi_frame = frame_bgr[roi_coordinates[1]:roi_coordinates[3], roi_coordinates[0]:roi_coordinates[2]]

        # Perform OCR on the cropped ROI frame
        text = pytesseract.image_to_string(roi_frame, lang="eng")
        text = text.strip()

        # Extract time values in HH:MM:SS format using a regular expression [Can set own "regular expression" for matching the format of alarm.]
        time_pattern = re.compile(r'\d{2}:\d{2}:\d{2}')
        matched_time = time_pattern.search(text)

        if matched_time:
            extracted_time = matched_time.group()
            if previous_value is None or extracted_time != previous_value:
                print("Time changed! New Alert:", extracted_time)

                # Display a macOS notification [Need to be configured if Operating System is changed.]
                notification_title = "Alert!"
                notification_message = f"New Message: {extracted_time}"
                display_notification(notification_title, notification_message)
                previous_value = extracted_time

        #Save the ROI frame as an image in the output_image folder
        #output_file = os.path.join(output_folder, f"frame_{time.time()}.png")
        #cv2.imwrite(output_file, roi_frame)

def exit_program():
    global running
    input("Press Enter to exit the program...")
    running = False

# Create a separate thread for capturing and processing frames
capture_thread = threading.Thread(target=capture_and_process)
capture_thread.start()

# Start the exit thread
exit_thread = threading.Thread(target=exit_program)
exit_thread.start()

# Wait for the capture thread to finish
capture_thread.join()

print("Program has stopped.")
