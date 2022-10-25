import cv2
import matplotlib.pyplot as plt
import numpy as np


# Template for now will be the the following 
template_img = cv2.imread('images/0.jpg')[300:400, 170:270,:]
w, h, _ = template_img.shape
cap = cv2.VideoCapture('video.mp4')


# result = cv2.VideoWriter('filename.avi', 
#                          cv2.VideoWriter_fourcc(*'MJPG'),
#                          10, (int(cap.get(3)), int(cap.get(4))))


while cap.isOpened():

    ret, frame = cap.read()

    if ret:
        res = cv2.matchTemplate(frame, template_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(frame, top_left, bottom_right, 255, 2)
        # result.write(frame)
        cv2.imshow('frame', frame)
    else:
        break

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
