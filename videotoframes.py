import numpy
import cv2
import os
import pickle
import shutil
import numpy as np

inputfolder = "./inputvideo/"
outputfolder = "./inputframes/"

#Read all video files from input folder
filedir = [f for f in os.listdir(inputfolder) if ".mp4" in f]

if os.path.exists(outputfolder):
    shutil.rmtree(outputfolder)

if not os.path.exists(outputfolder):
    os.makedirs(outputfolder)

#Create directory with video data
counter = 0;
for f in filedir:
    cap = cv2.VideoCapture(inputfolder+f)
    while(cap.isOpened()):
        success, frame = cap.read();
        if(counter > 10):
            # break
            pass
        if success:
            counter+=1
            cv2.imwrite(outputfolder+str(counter)+'.png',frame);
            edges = cv2.Canny(frame,10,60)
            cv2.imwrite(outputfolder+"e"+str(counter)+'.png',edges);
        else:
            break
    cap.release()
