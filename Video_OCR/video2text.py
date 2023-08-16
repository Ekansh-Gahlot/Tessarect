import cv2
import pytesseract
import pyautogui
import numpy as np
import time
import os
import threading
import subprocess  # Import the subprocess module

# Set the path to the Tesseract data directory
tesseract_cmd = '/opt/local/share/tessdata'  # Update with your Tesseract path

def display_notification(title, message):
    # Use subprocess to execute the osascript command
    subprocess.run(['osascript', '-e', f'display notification "{message}" with title "{title}"'])

# Define the region of interest (ROI) coordinates
roi_coordinates = (785, 779, 2075, 1049)  # Update with your ROI coordinates

# Create the output_image folder if it doesn't exist
output_folder = os.path.expanduser("~/Desktop/output_image")
os.makedirs(output_folder, exist_ok=True)


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

        # Compare the extracted text with the previous value
        if previous_value is None or text.strip() != previous_value.strip():
            if(text.strip() !=""):
                print("Value changed! New value:", text)

                # Display a macOS notification
                notification_title = "New ALERT!"
                notification_message = f"New value: {text}"
                display_notification(notification_title, notification_message)
                previous_value = text.strip()  # Update the previous value
            
        # Save the ROI frame as an image in the output_image folder
        output_file = os.path.join(output_folder, f"frame_{time.time()}.png")
        cv2.imwrite(output_file, roi_frame)

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
