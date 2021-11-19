# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 14:09:59 2021

@author: zradlicz
"""

import cv2
import numpy as np

colors = np.load('color_list.npy')

NAME = 'color_contour'
filename = NAME+'.jpg'


    
def closest(colors,color):
    #colors = np.array(colors)
    #color = np.array(color)
    distances = np.sqrt(np.sum((colors-color)**2))
    index_of_smallest = np.where(distances==np.amin(distances))
    smallest_distance = colors[index_of_smallest]
    return smallest_distance 

img = cv2.imread(filename)

#dist = cv2.absdiff(gray1, gray2)
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)#img=np.zeros((2000,2000))
img
gray_img = cv2.resize(gray_img, (2000,2000), interpolation = cv2.INTER_AREA)
ret,thresh_img = cv2.threshold(gray_img,10,255,cv2.THRESH_BINARY)
thresh_img = np.uint8(thresh_img)
#img = cv2.circle(img,(1000,1000),5,(1,1,1),-1)
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

'''
test = np.zeros((2000,2000,3))
for contour in contours:
    color = img[contour[0][0][0],contour[0][0][1]]
    closest_color = closest(colors,color)
    closest_color = (int(closest_color[0][0]),int(closest_color[0][1]),int(closest_color[0][2]))
    test = cv2.drawContours(test, [contour], -1, closest_color, 1)
test = test/255
'''
    

#cnt = contours[100]
test = np.zeros((2000,2000,3))
test = cv2.drawContours(test, contours, -1, (255,255,255), 1)

cv2.imshow('test',test)


code = []
count = 1
contour_count = 1
for cnt in contours:
    code.append('Z1') #pen up
    for val in cnt:
        if count == 1:
            code.append('Z1')
        x = round((val[0][0]/2000)*200,2)
        y = round((val[0][1]/2000)*200,2)
        code.append('N'+str(count*10)+ ' X'+str(x)+' Y'+str(y)+' Z0')
        count+=1
    code.append('Z0') #pen down
    contour_count+=1
        
f = open(NAME+"_gcode.nc", "w")


for line in code:
    f.write(line+'\n')
    
        