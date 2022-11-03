import os
import cv2
import pickle
import numpy as np
from matplotlib import pyplot as plt
import imageio

save_gif = True
step = 7
video_names = ['Escalator', 'Fields', 'Track']
video_name = video_names[2]


color_MIL = (255, 0, 0)
color_KCF = (0, 255, 0)
color_CSRT = (0, 0, 255)

def drow_text(img):
    cv2.putText(img,"MIL", (5,25), cv2.FONT_HERSHEY_DUPLEX, 1, color_MIL, 3)
    cv2.putText(img,"KCF", (5,50), cv2.FONT_HERSHEY_DUPLEX, 1, color_KCF, 3)
    cv2.putText(img,"CSRT", (5,75), cv2.FONT_HERSHEY_DUPLEX, 1, color_CSRT, 3)

def ReadEscalatorVideo():
    vidcap = cv2.VideoCapture('data/Escalator.mp4')
    x1,y1,w,h = 785, 277, 58, 107
    return vidcap, (x1, y1, w, h)

def ReadFieldsVideo():
    vidcap = cv2.VideoCapture('data/Fields.mp4')
    x1,y1,w,h = 634, 397, 47, 39
    return vidcap, (x1, y1, w, h)

def ReadTrackVideo():
    vidcap = cv2.VideoCapture('data/Track.mp4')
    x1,y1,w,h = 23, 207, 173, 93
    return vidcap, (x1, y1, w, h)

def drow_rectangle(img, bbox, color):
    x1, y1 = bbox[0], bbox[1]
    width, height = bbox[2], bbox[3]
    cv2.rectangle(img, (x1, y1), (x1+width, y1+height), color, 2)

if video_name == video_names[0]:
    video_capture, bbox = ReadEscalatorVideo()

if video_name == video_names[1]:
    video_capture, bbox = ReadFieldsVideo()

if video_name == video_names[2]:
    video_capture, bbox = ReadTrackVideo()

trackerMIL = cv2.TrackerMIL_create()
trackerKCF = cv2.TrackerKCF_create()
trackerCSRT = cv2.TrackerCSRT_create()

success, image = video_capture.read()

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# # Initialize tracker
ok_MIL = trackerMIL.init(image, bbox)
ok_KCF = trackerKCF.init(image, bbox)
ok_CSRT = trackerCSRT.init(image, bbox)

drow_rectangle(image, bbox, (255, 0, 0))
drow_text(image)

imshow = plt.imshow(image)

frames = []
frames.append(image)
frame_number = 1

plt.ion()

# Tracking loop
while success:
    success, image = video_capture.read()
    frame_number += 1
    if image is None:
        break

    if frame_number % step != 0:
        continue

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)    
        
    ok_MIL, bbox_MIL = trackerMIL.update(image)
    ok_KCF, bbox_KCF = trackerKCF.update(image)
    ok_CSRT, bbox_CSRT = trackerCSRT.update(image)
    # print(ok, bbox)

    # Show the tracker working
    drow_rectangle(image, bbox_MIL, color_MIL)
    drow_rectangle(image, bbox_KCF, color_KCF)
    drow_rectangle(image, bbox_CSRT, color_CSRT)
    drow_text(image)
    imshow.set_data(image)
    frames.append(image)
    plt.pause(0.00000001)
        
plt.ioff() # due to infinite loop, this gets never called.
plt.show()

if save_gif:
    fr = [cv2.resize(img, None, fx=0.5, fy=0.5) for img in frames]
    imageio.mimsave(('results/result2_%s_%d.gif' % (video_name, step)), fr, fps=4)