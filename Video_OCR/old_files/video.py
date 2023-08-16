import cv2
import pytesseract
import pyautogui
import numpy as np
import time
import os

# Set the path to the Tesseract data directory
tesseract_cmd = '/opt/local/share/tessdata'  # Update with your Tesseract path

# Define the region of interest (ROI) coordinates
roi_coordinates = (878, 689, 1646, 813)  # Update with your ROI coordinates


# Create the output_image folder if it doesn't exist
output_folder = os.path.expanduser("~/Desktop/output_image")
os.makedirs(output_folder, exist_ok=True)

# Wait for 3 seconds before starting
time.sleep(3)

# Initialize previous value
previous_value = None

while True:
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
    if previous_value is None:
        previous_value = text
    elif text != previous_value:
        print("Value changed! New value:", text)
        # Trigger your alert here (e.g., display alert box)

    # Save the ROI frame as an image in the output_image folder
    output_file = os.path.join(output_folder, f"frame_{time.time()}.png")
    cv2.imwrite(output_file, roi_frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

exit(1)

