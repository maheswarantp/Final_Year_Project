import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
from tqdm import tqdm
import shutil

# Video file
VIDEO_SRC = 'video.mp4'

# Read video src
if os.path.exists('images'):
    shutil.rmtree('images')

if not os.path.exists('images'):
    os.mkdir('images')

cap = cv2.VideoCapture(VIDEO_SRC)

frame_count = 0
while cap.isOpened():     
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(f'images/{frame_count}.jpg', frame)
        frame_count += 1
        cv2.imshow('Frame', frame)         
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()