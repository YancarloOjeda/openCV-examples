#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:26:20 2020

@author: Yancarlo Ojeda 
"""


import cv2 
import numpy as np
from matplotlib import pyplot as plt

#gray scale
image = cv2.imread('/home/yan/image.jpeg', 0)

plt.hist(image.ravel(),256,[0,256])
plt.show()

#for each RGB value
# image = cv2.imread('/home/yan/image.jpeg')
# color = ('b','g','r')
# for i,col in enumerate(color):
#     histr = cv2.calcHist([image],[i],None,[256],[0,256])
#     plt.plot(histr,color = col)
#     plt.xlim([0,256])
# plt.show()