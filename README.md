# Tessarect
One of my project while working as Summer Intern in 2023 at MTR, Hong Kong.

# Problem
A old software for which we had no further support and API's. The old system was being used to display any new triggered alarms on to a screen which was used by ground personnel for monitoring. The screen required continuos manual monitoring by staff to see if any alarm are being triggered. 

# Goal
To be able to automatically detect the alarm is triggered by capturing the video feedback of the system and using OCR for detection and processing the relevant text displayed.

# Solution
Defined our Region Of Interest (ROI).
Used pyautogui to capture screenshots from the video periodically and then use tessaract to extract and process the extracted data and display notifications.
Used libraries OpenCV for image processing (cropping (within ROI) and changing the color space from RGB to BGR) and then feed it to tessarect for extracting the intended text from the captured image.


# How They Work Together:
OpenCV captures a screenshot and crops it to a specific region.
OpenCV converts the color format of the image, which might make it easier for Tesseract to recognize the characters.
Tesseract receives the clean, cropped, and well-formatted image from OpenCV and extracts the text from it.

# Benefits of Using Both:
Better OCR accuracy: By preprocessing the image (cropping, filtering, etc.) using OpenCV, you give Tesseract a cleaner input, leading to better text recognition.
Control over regions: OpenCV allows to select only the region where you expect the text (ROI), which reduces unnecessary processing and increases efficiency.
Real-time processing: OpenCV enables capturing real-time screenshots, while Tesseract continuously extracts and compares text to detect changes.

# Result
The program was able to solve the long standing problem faced by MTR Hong Kong in monitoring of the alarms from different sources. It also had feature of removing the obsolete screen capture in order to improve the effeciency and performance. 

- OpenCV is used for capturing and manipulating the image (e.g., cropping the region of interest).
- Tesseract is used for reading the text from that specific image region.

 This combination ensures high accuracy and efficiency in your text extraction process.

