#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:52:36 2017

@author: ChrisErnst
"""


### for LOOPS - Definite

# range with a single argument(the stopping point)
for i in range(20):
    print(i)


# Import the time module so our program can sleep
import time

# range with both arugments(start, stop) Note, it doesn't include the last value
for i in range(90,100):
    time.sleep(0.5)
    print(i)


# for loop over a list
manyItemList = ['a','b',5,7,'n']
len(manyItemList)
for i in manyItemList:
    print(i)






### while LOOPS - Indefinite - Remember to alter the value in the conditional statement!

x=20
while x>10:
    time.sleep(0.25)
    print(x)
    x=x-1

    






### for loops -  more advaced
    
from sympy import Matrix

colVector = Matrix([[3,3,4]])

rowVector =  Matrix([[3],[3],[4]])

colVector[2]

# Create a Matrix
B = Matrix([[6,8,9,0,15],
           [3,1,17,22,18],
           [1,5,4,3,1],
           [7,5,1,0,6],
           [3,1,8,8,9]])
    
    
import numpy as np
np.shape(B)
np.size(B, axis=0)
np.size(B, axis=1)

rows = np.size(B, axis=0)

cols = np.size(B, axis=1)


for i in range(rows):
    for j in range(cols):
        B[i,j] = B[i,j]+1
        print('\n',B, '\n')
        time.sleep(0.25)





### while loops - more advanced


# Import a random integer generator

def randListGen():
    import random as rd # Remember how we nickname libraries
    start = time.time()
    
    randNumber = rd.randint(1,100)
    myList=[]
    # create an empty list
    while randNumber <98:
        randNumber = rd.randint(1,100)
        myList.extend([randNumber])
        print(myList,'\n')
        time.sleep(0.25)
        
        if randNumber >=98:
            time.sleep(1)
            print()
            print()
            print('\n','Your List is ', len(myList) , ' Elements Long')
            print('The average is: ' , np.mean(myList))
            end=time.time()
            timeElapsed = round(end - start, 4)
            print('\nThat took ', timeElapsed, 'seconds')
            print('\nComputation time was ', timeElapsed - len(myList)*0.25, ' seconds')

randListGen()






















