import cv2

# Initialize variables to store clicked points
clicked_points = []

# Mouse click callback function
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append((x, y))
        if len(clicked_points) >= 2:
            cv2.rectangle(image, clicked_points[-2], clicked_points[-1], (0, 255, 0), 2)
            cv2.imshow('Image', image)

# Load the image
image_path = '/Users/ekanshgahlot/Desktop/Screenshot 2023-08-16 at 1.53.27 PM.png'  # Replace with the actual path to your image
image = cv2.imread(image_path)

if image is not None:
    cv2.imshow('Image', image)
    cv2.setMouseCallback('Image', mouse_callback)
    
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('p') and len(clicked_points) == 2:
            x1, y1 = clicked_points[0]
            x2, y2 = clicked_points[1]
            roi_coordinates = (x1, y1, x2, y2)
            print("ROI Coordinates:", roi_coordinates)
            break

    cv2.destroyAllWindows()
else:
    print("Image not found or couldn't be read.")
