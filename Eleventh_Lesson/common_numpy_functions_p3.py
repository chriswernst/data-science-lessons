#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 17:22:18 2017

@author: ChrisErnst

Note: this includes functions from part 1 and 2 also. They can be found toward the top of the doc. 
Part 3 is toward the bottom!
"""

##### PART 1:

import numpy as np

# Square Root
np.sqrt(25)

# Pi
np.pi

# Sum
np.sum([3,5,8,20])

# Size
a=[12,15,0,9,8]
np.size(a, axis=0)

# Mean (Average)
np.mean(a)

# Exponential
np.exp(1)

# Arange (start, stop, step size)
theRange = np.arange(3,300,5)

# linspace (start, stop, number of steps)
equalSpacedList = np.linspace(3,5,10)

# Array
b = np.array([0,3,4])
type(b)

# Recast as Array
a=np.asarray(a)

# Matrix
matA = np.matrix([[0,1],[3,2]])
matB = np.matrix('0 1; 3 2')

# Shape
np.shape(matA)
np.shape(matB)

# Reshape
a=[12,15,0,9]
np.reshape(a, (2,2))

# NonZero
np.nonzero(a)

# Insert
newMatA = np.insert(matA, 2, [2,4], axis=1)

# Ones and Zeros Matrices
allOnesMatrix = np.ones([5,5])

allZerosMatrix = np.zeros([200,20])

# 'Empty'
np.empty([20,20])

# Append
a=[12,15,0,9]
a=np.append(a, [3,5,8,1,22,36,4])

# Where
a=a[0:5]
np.where(a>8)
a=np.where(a>8,-66,a)


# Flatten
allZerosArray = allZerosMatrix.flatten()

# Clip
b=[1,2,3,4,5,6,7,8,9,0]
np.clip(b, 1, 4)
# Out: 
array([1, 2, 3, 4, 4, 4, 4, 4, 4, 1])
    
    
# Concatenate
np.concatenate((a,allZerosArray,b))

# Trig Functions
np.sin(0)
np.cos(0)
np.tan(0)
np.arctan2(1)










##### PART 2:

# Size
a=[12,15,0,9,8]
np.size(a, axis=0)

# Array
b = np.array([0,3,4])
type(b)

# Matrix
matA = np.matrix([  [0,1],[3,2]  ])
matB = np.matrix('0 1; 3 2')

matA =  np.matrix([             [1,2,],
                                [2,3 ],
        [5,6]
        
        ])

# Shape
np.shape(matA)
np.shape(matB)


# Where
a = a[0:5]
a=np.asarray(a)


indices = np.where(a>=8)

a[indices]



a=np.where(a>=8,-66,a)



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

pil_im = Image.open('golden.jpg')
# Shows the image in a new window
imshow(pil_im)


pil_im_array = np.array(pil_im)

sizeInPixels = np.shape(pil_im_array)
# This will return the size of the photo in pixels


# Let's pull out an individual pixel from the sky:
pil_im_array[200,100]

skyPixel = pil_im_array[200,100]

box  = (0,0,1680,200)
region = pil_im.crop(box)
# Takes positional arguments (left, upper, right, lower)
imshow(region)



### Add up RGB values to become intensity

# Let's see our orignal image/matrix
pil_im_array
np.shape(pil_im_array)

height,width = sizeInPixels[0], sizeInPixels[1]
newImage = np.zeros((height, width))

blankImg = Image.fromarray(newImage)
plt.imshow(blankImg)
# Displays a black image

np.shape(blankImg)

for rows in range(height):
    for cols in range(width):
        
        newImage[rows,cols] = np.mean(pil_im_array[rows,cols])
        
        if i%100 == 0:            
            print('Currently on pixel',rows,', ',cols)

np.shape(newImage)

blankImg = Image.fromarray(newImage)
plt.imshow(blankImg)

img.save('myImage.png')








##### PART 3:

# Various ways to round numbers

np.floor(np.pi)

np.ceil(np.pi)

np.fix(np.pi)

round(np.pi)

hist -n
# A history of our commands
np.remainder(20,7)
20%7
# The two above are the same

