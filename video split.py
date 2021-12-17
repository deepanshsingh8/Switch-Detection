# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 14:25:45 2021

@author: deepa
"""
# create a folder to store extracted images
import os
folder = 'C:\\Users\\deepa\\OneDrive\\Desktop\\SWITCH RECOG\\test'  
os.mkdir(folder)
# use opencv to do the job
import cv2
print(cv2.__version__)  # my version is 3.1.0
vidcap = cv2.VideoCapture('C:\\Users\\deepa\\OneDrive\\Desktop\\SWITCH RECOG\\Input\\Provenio Switch.mp4')
count = 0
while True:
    success,image = vidcap.read()
    if not success:
        break
    cv2.imwrite(os.path.join(folder,"frame{:d}.jpg".format(count)), image)     # save frame as JPEG file
    count += 1
print("{} images are extacted in {}.".format(count,folder))
    