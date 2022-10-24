import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil

IMAGE_SRC = 'images'

# Created sorted frames array
image_lis = sorted(os.listdir('images'), 
                key=lambda x:int(x.split('.')[0]))

# Create groups of two for image matching
tup_list = []
try:
    for i in range(len(image_lis)):
        tup_list.append((image_lis[i], image_lis[i+1]))
except:
    pass

# orb = cv2.ORB_create()

# kp1, des1 = orb.detectAndCompute(img0,None)
# kp2, des2 = orb.detectAndCompute(img1,None)

# bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# matches = bf.match(des1,des2)
# matches = sorted(matches, key = lambda x:x.distance)

# img3 = cv2.drawMatches(img0,kp1,img1,kp2,matches[:20],None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

orb = cv2.ORB_create()

def keypoint_matching(img1_path, img2_path):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
    matches = bf.match(des1,des2)
    matches = sorted(matches, key = lambda x:x.distance)

    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    return img3


for index, (img1, img2) in enumerate(tup_list):
    img = keypoint_matching(f'images/{img1}', f'images/{img2}')
    cv2.imwrite(f'output/{index}.jpg', img)

