# Tessarect
One of my project while working as Summer Intern in 2023 at MTR, Hong Kong.

# Problem
A old software for which we had no further support and API's. The old system was being used to display any new triggered alarms on to a screen which was used by ground personnel for monitoring. The screen required continuos manual monitoring by staff to see if any alarm are being triggered. 

# Goal
To be able to automatically detect the alarm is triggered by capturing the video feedback of the system and using OCR for detection and processing the relevant text displayed.

# Solution
Defined our Region Of Interest (ROI).
Used pyautogui to capture screenshots from the video periodically and then use tessaract to extract and process the extracted data and display notifications.
Used libraries OpenCV for image processing and then feed it to tessarect for extracting the intended text from the captured image.

# Result
The program was able to solve the long standing problem faced by MTR Hong Kong in monitoring of the alarms from different sources. It also had feature of removing the obsolete screen capture in order to improve the effeciency and performance. 
