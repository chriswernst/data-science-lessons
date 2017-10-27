#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:48:20 2017

@author: ChrisErnst
"""

############## VARIABLES ########################

a=2
a=a+1
print(a)

def multipleOutputFunction(c,d):
    product = c*d
    sum1 = c+d
    quotient = c/d
    return product, sum1, quotient

type(6//2)
type(6/2)
# Modulus helps determine if a number is even or odd
remainder = 6%2

multipleOutputFunction(6,3)

product, sum1, quotient = multipleOutputFunction(190,8)


############### KEYWORDS #########################
# To get a list of keywords:
import keyword
print(keyword.kwlist)
# OUTPUTS

['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 
'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']



############# BUILT IN FUNCTIONS ########################
# To generate a list of functions and errors
builtIns = dir(__builtins__)
builtInFunctions =  builtIns[79:]
errors = builtIns[:70]


# Some useful functions in action:
testList = [1,4,8,9,10,9,4]
type(testList)
setTest = set(testList)
# Gives back just the distinct values
{1, 4, 8, 9, 10}

subList = [1,9,4,4]
subSet = set(subList)

# Finding Subsets in Sets
subSet <= setTest 
# Will return TRUE