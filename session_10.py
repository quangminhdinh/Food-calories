import cv2
import numpy as np

# Create an object capture
cap = cv2.VideoCapture(0)
# Create an identify object
classhar = cv2.CascadeClassifier("E:\\AI files\\C4T_main_module\\haarcascade_frontalface_alt2.xml")
# load mask
mask = cv2.imread("E:\\AI files\\C4T_main_module\\1.jpg")

while True:

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # Detect face
    faces = classhar.detectMultiScale(gray)

    x_max = 0
    y_max = 0
    w_max = 0
    h_max = 0
    for x, y, w, h in faces:
        if (w * h) > (w_max * h_max):
            x_max = x
            y_max = y
            w_max = w
            h_max = h
    if w_max > 0:
        new_mask = cv2.resize(mask, (w_max, h_max))
        frame[y_max:y_max + h_max, x_max:x_max + w_max] -= new_mask

    cv2.imshow("img", frame)

    k = cv2.waitKey(30)

    if k == 27:
        cap.release()
        break
    elif k == ord('s') & 0xFF:
        cv2.imwrite('img.jpg', frame)
        cap.release()
        break
# kalman filter tracking face
