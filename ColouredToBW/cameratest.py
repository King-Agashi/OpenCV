import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame and store each frame in frame
    ret, frame = cap.read()

    # Change each frame to b/w and store it in grey
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the original feed (frame) and converted feed (grey)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    # Function to break/stop by pressing key q for 20ms
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture, and close cv2
cap.release()
cv2.destroyAllWindows()
