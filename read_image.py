#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 01:58:59 2020

@author: Yancarlo Ojeda
"""


import cv2 

"""
with cv2.imread we can read any image. The function receive two parameters. 
Fist is the path to teh image, and second specifies the way image should be read.
"""
image = cv2.imread('/home/yan/image.jpeg')

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
