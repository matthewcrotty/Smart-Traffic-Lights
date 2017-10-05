import numpy
import cv2
import os
import pickle

#Read all video files from input folder
filedir = [f for f in os.listdir("./inputframes") if ".png" in f]

#Create directory with video data
imgcontent = []
for f in filedir:
    cap = cv2.VideoCapture("./inputvideo/"+f)
    while(cap.isOpened()):
        success, frame = cap.read()
        if success:
            imgcontent.append(frame)
        else:
            break
    cap.release()

#Write to file
try:
    with open("./videodata/videodata", 'wb') as f:
        pickle.dump(imgcontent, f, pickle.HIGHEST_PROTOCOL)
except Exception as e:
    print('Unable to save data to file. Error:', e)
'''
cap = cv2.VideoCapture('563398107.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cap.release()

'''
