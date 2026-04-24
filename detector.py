import cv2
import time
from timer import check_focus

is_running = False
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Could not open webcam.")
    exit()


def start_detector():
    global is_running
    is_running = True
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("ERROR: Could not open webcam.")
        return

    while is_running:
        ret, frame = cap.read()
        if not ret:
            print("ERROR: Failed to read frame.")
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)
        if len(faces) > 0:
            check_focus(True)
        else:
            check_focus(False)
        time.sleep(1)

    cap.release()


def stop_detector():
    global is_running
    is_running = False