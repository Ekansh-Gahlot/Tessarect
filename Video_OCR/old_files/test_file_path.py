import cv2
import pytesseract
import numpy as np

import os
os.environ['TESSDATA_PREFIX'] = '/opt/local/share/tessdata'


# Set the path to the Tesseract data directory
tesseract_cmd = r'/opt/local/share/tessdata'  # Update with your Tesseract path
# Load the video using OpenCV
video_path = '/Users/ekanshgahlot/Downloads/IMG_0877.MOV'  # Replace with your video's path
cap = cv2.VideoCapture(video_path)

# Define the region of interest (ROI) coordinates
roi_coordinates = (641, 499, 1874, 792)  # Update with your ROI coordinates

# Initialize previous value
previous_value = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Crop the frame to the ROI
    roi_frame = frame[roi_coordinates[1]:roi_coordinates[3], roi_coordinates[0]:roi_coordinates[2]]

    # Perform OCR on the cropped ROI frame
    text = pytesseract.image_to_string(roi_frame, lang="eng")

    # Compare the extracted text with the previous value
    if previous_value is None:
        previous_value = text
    elif text != previous_value:
        print("Value changed! New value:", text)
        # Trigger your alert here (e.g., display alert box)

    # Display the ROI frame
    cv2.imshow("ROI Frame", roi_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
