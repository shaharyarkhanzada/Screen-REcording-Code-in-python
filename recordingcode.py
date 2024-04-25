import cv2
import numpy as np
import pyautogui

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (1920, 1080))

try:
    while True:
        # Capture screenshot
        img = pyautogui.screenshot()

        # Convert the screenshot to a numpy array
        frame = np.array(img)

        # Convert RGB to BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Write the frame
        out.write(frame)

        # Stop recording when 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break
except KeyboardInterrupt:
    pass

# Release everything if job is finished
out.release()
cv2.destroyAllWindows()
