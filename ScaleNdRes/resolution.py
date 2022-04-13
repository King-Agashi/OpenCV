import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# ---------------------------------------------------
# Functions to change resolution of feed


def make_1080p():
    # 3 is parameter for width, and 4 is for height
    cap.set(3, 1920)
    cap.set(4, 1080)


def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)


def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)


def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)
# ---------------------------------------------------
# Function to rescale frames instead of whole capture window


def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
# ---------------------------------------------------


while(True):
    # Capture frame-by-frame and store each frame in frame
    ret, frame = cap.read()
    frame2 = rescale_frame(frame, percent=30)

    # Display the frames
    cv2.imshow('frame', frame)
    cv2.imshow('frame2', frame2)

    # Function to break/stop by pressing key q for 20ms
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture, and close cv2
cap.release()
cv2.destroyAllWindows()
