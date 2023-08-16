# Tessarect
One of my project while working as Summer Intern in 2023.

# Problem
A old software for which we had no further support and API's. The system was being used to display any new alarms that are triggered and for monitoring.

# Goal
To be able to detect the alarm is triggered by monitoring the video feedback of the system and use OCR for detecting and processing the text displayed.

# Solution
Defined our Region Of Interest (ROI) using OpenCV.
Used pyautogui to capture screenshots from the video periodically and then use tessaract to extract and process the extracted data and display notifications.
