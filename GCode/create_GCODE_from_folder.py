# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 14:09:59 2021

@author: zradlicz
"""

import cv2
import numpy as np
import glob



FOLDER_NAME = 'contour_layers'


img_array = []
for filename in sorted(glob.glob('C:/Users/zradlicz/Desktop/Misc Art/raytracing/'+FOLDER_NAME+'/*.png')):
    img = cv2.imread(filename)
    print(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)

contour_array = []
for img in img_array:

    #dist = cv2.absdiff(gray1, gray2)
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)#img=np.zeros((2000,2000))
    img
    gray_img = cv2.resize(gray_img, (2000,2000), interpolation = cv2.INTER_AREA)
    ret,thresh_img = cv2.threshold(gray_img,10,255,cv2.THRESH_BINARY)
    thresh_img = np.uint8(thresh_img)
    #img = cv2.circle(img,(1000,1000),5,(1,1,1),-1)
    contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour_array.append(contours)
    

#cnt = contours[100]
#test = np.zeros((2000,2000,3))
#test = cv2.drawContours(test, contours, -1, (255,255,255), 1)

#cv2.imshow('test',test)


code = []
count = 1
contour_count = 1
for contours in contour_array:
    for cnt in contours:
        code.append('Z1') #pen up
        first = True
        for val in cnt:
            x = round((val[0][0]/2000)*200,2)
            y = round((val[0][1]/2000)*200,2)
            if first:
                code.append('Z1')
                code.append('N'+str(count*10)+ ' X'+str(x)+' Y'+str(y)+' Z1')
                count+=1
                code.append('N'+str(count*10)+ ' X'+str(x)+' Y'+str(y)+' Z1')
                count+=1
                code.append('N'+str(count*10)+ ' X'+str(x)+' Y'+str(y)+' Z1')
                count+=1
                code.append('N'+str(count*10)+ ' X'+str(x)+' Y'+str(y)+' Z1')
                count+=1
                first = False
            code.append('N'+str(count*10)+ ' X'+str(x)+' Y'+str(y)+' Z0')
            count+=1
        code.append('Z0') #pen down
        contour_count+=1
    code.append('Z1')
    code.append('!')
        
f = open(FOLDER_NAME+"_gcode.nc", "w")


for line in code:
    f.write(line+'\n')
    
        