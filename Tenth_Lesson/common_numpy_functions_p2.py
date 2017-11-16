#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 19:00:42 2017

@author: ChrisErnst

Note: this includes functions from part 1 also. They can be found toward the bottom of the doc
"""

import numpy as np

##### Review important functions

# Size
a=[12,15,0,9,8]
np.size(a, axis=0)

# Array
b = np.array([0,3,4])
type(b)

# Matrix
matA = np.matrix([[0,1],[3,2]])
matB = np.matrix('0 1; 3 2')

# Shape
np.shape(matA)
np.shape(matB)


# Where
a=a[0:5]
a=np.asarray(a)
np.where(a>=8)
a=np.where(a>=8,-66,a)


##### New Functions


# Append
a=[12,15,0,9]
a=np.append(a, [3,5,8,1,22,36,4])


## Let's build a for loop to append the elapsed time to the end of an array
# Here are a few useful functions:
import time

start =  time.time()
end = time.time()

total = end - start

myNewArray = np.array([])

# Enter your code here:

    

   
    
    
### END


# Insert
newMatA = np.insert(matA, 2, [2,4], axis=1)

# Flatten
allZerosArray = allZerosMatrix.flatten()

# Concatenate
np.concatenate((a,allZerosArray,b))

# NonZero
np.nonzero(a)


# When do we use matrices???

##### Matrix Exercise on images

import os
from PIL import Image
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


os.chdir('/Users/ChrisErnst/Development/Python/computerVision/Image_Manipulation/')

pil_im = Image.open('chrysler.jpg')
# Shows the image in a new window
imshow(pil_im)


pil_im_array = np.array(pil_im)

sizeInPixels = np.shape(pil_im_array)
# This will return the size of the photo in pixels


# Let's pull out an individual pixel from the sky:
pil_im_array[200,100]

skyPixel = pil_im_array[200,100]

box  = (200,100,201,101)
region = pil_im.crop(box)
# Takes positional arguments (left, upper, right, lower)
imshow(region)



### Add up RGB values to become intensity

# Let's see our orignal image/matrix
pil_im_array
np.shape(pil_im_array)

h,w = sizeInPixels[0], sizeInPixels[1]
newImage = np.zeros((h, w))

blankImg = Image.fromarray(newImage)
plt.imshow(blankImg)
# Displays a black image

np.shape(blankImg)

for i in range(h):
    for j in range(w):
        
        newImage[i,j] = np.mean(pil_im_array[i,j])
        
        if i%100 == 0:            
            print('Currently on pixel',i,', ',j)

np.shape(newImage)

blankImg = Image.fromarray(newImage)
plt.imshow(blankImg)

img.save('myImage.png')




##### Functions from Part 1:

# Arange
theRange = np.arange(3,300,5)

# linspace
np.linspace(3,5,10)

# Square Root
np.sqrt(25)

# Pi
np.pi

# Sum
np.sum([3,5,8,20])

# Mean (Average)
np.mean(a)

# Exponential
np.exp(1)

# Recast as Array
a=np.asarray(a)

# Reshape
a=[12,15,0,9]
np.reshape(a, (2,2))

# Ones and Zeros Matrices
allOnesMatrix = np.ones([5,5])

allZerosMatrix = np.zeros([200,20])

# 'Empty'
np.empty([20,20])

# Clip
b=[1,2,3,4,5,6,7,8,9,0]
np.clip(b, 1, 4)
# Out: 
    array([1, 2, 3, 4, 4, 4, 4, 4, 4, 1])

# Trig Functions
np.sin(0)
np.cos(0)
np.tan(0)
np.arctan2(1)