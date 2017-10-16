#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:44:45 2017

@author: ChrisErnst

THIS IS DOCUMENTATION SPACE
DATE:
NAME OF PROGRAM:
AUTHOR:
NOTES ON IMPLEMENTATION:
"""

# This is a comment, and won't be executed by Python

# We're going to learn about functions!


# Define the function
def myPythonFunction(requirement1,requirement2):
	req3 = requirement1 + requirement2
	return req3

# Call the function without requirements - This will throw an error
myPythonFunction()

# Call the function with requirements
myPythonFunction(5,2)


# Define the function
def multiplyNumbers(a=10, b=7):
    product=a*b
    return product

# Call the function with defaults
multiplyNumbers()

# Call the function with new parameters
multiplyNumbers(a=20, b=10)

# Define a function
def happyBirthday(name='Jen'):
    print('Happy Birthday to you')
    print('Happy Birthday to you')
    print('Happy Birthday Dear ' + name)
    print('Happy Birthday to you')
# defined the function - what's different about this function?
    

happyBirthday()
# call the function with the default values

happyBirthday('name=Monica')
# call the function with a special value



def farenheitToCelsius(humidity, name='Jeff', farenheit=32):
        celsius = str(round(((farenheit - 32) * 5/9),1))
        print('\n')
        print("Hey " + name +",")
        print('\n')
        print("The temperature in Celsius is: " + celsius)
        print('The humidity is ' + str(humidity)+'%\n')
        print('Have a great day!\n')

farenheitToCelsius(32)

farenheitToCelsius(55, name='Mark')

farenheitToCelsius(60, name='Jeff', farenheit=90)





