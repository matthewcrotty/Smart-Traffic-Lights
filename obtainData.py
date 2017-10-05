import cv2
import os
import pickle
import shutil
import numpy as np
import json
from pprint import pprint
import urllib.request
from pycocotools.coco import COCO

jsonFolder = "./cocodataset/"
outputfolder = "./cocoimages/"

# with open(jsonFolder+'instances_train2017.json') as data_file:    
#     data = json.load(data_file)

# print(data.keys())
# print(data["images"][0]);
# print(data["annotations"][0]);

# resp = urllib.request.urlopen(data["images"][0]['coco_url'])
# image = np.asarray(bytearray(resp.read()), dtype="uint8")
# image = cv2.imdecode(image, cv2.IMREAD_COLOR)
# cv2.imshow('image',image)

coco=COCO(jsonFolder+'instances_train2017.json')

# cats = coco.loadCats(coco.getCatIds())
# nms=[cat['name'] for cat in cats]
# print('COCO categories: \n{}\n'.format(' '.join(nms)))

catIds = coco.getCatIds(catNms=['person'])
catIds2 = coco.getCatIds(catNms=['vehicle'])
imgIds = coco.getImgIds(catIds=catIds ) + coco.getImgIds(catIds=catIds2 )

imgs = coco.loadImgs(imgIds)
for img in imgs:
	resp = urllib.request.urlopen(img['coco_url'])
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)

	cv2.imwrite(outputfolder+str(img['id'])+'.png',image)
	edges = cv2.Canny(image,100,100)
	cv2.imwrite(outputfolder+"e"+str(img['id'])+'.png',edges)

# annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
# anns = coco.loadAnns(annIds)
# print(anns)



            
# coco.showAnns(anns);