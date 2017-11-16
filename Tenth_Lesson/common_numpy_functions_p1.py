#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 19:00:42 2017

@author: ChrisErnst
"""

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

# Arange
theRange = np.arange(3,300,5)

# linspace
np.linspace(3,5,10)

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