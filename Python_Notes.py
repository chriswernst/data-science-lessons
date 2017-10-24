'''
PYTHON 3.5 NOTES

Last Updated 10/19/2017

Might want to use Spyder 3.5 or iPython in order to have access to all libraries
  - and DON'T use pip3 to update libraries when using Anaconda

http://stackoverflow.com/questions/33851379/pyaudio-installation-on-mac-python-3

'''

#################### BASIC FUNCTIONALITIES ####################

"""
OR
'''
is meant for documentation 

"""
# is a regular comment

import os
import numpy
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
# make calls to different .py documents -- 'libraries' or 'modules'

from extra_functions import function1, function2, var1, var3

import numpy
from numpy import *

from scipy import *
# the 'from libName import *' allows the module to be used without the prefix. For example:
from numpy import *
pi
Out[2]: 3.141592653589793 # Output

# shorten/nickname library names
import numpy as np
np.pi 

import webbrowser as wb
wb.open('http://google.com')
# to import using shorthand

import os
os.getcwd()
# imports relevant lib and gets working directory

os.chdir('C:\\Users\\NYCCE\\Documents\\Python 3.5\\Programs') # Windows Directory
os.chdir('/Robotics Nanodegree - Udacity/Term 1/Project 1 - Search and Sample') # OSX Directory
# sets the directory

dir(modulename)
#lists the variables in named module
locals()
#gives all the variables avail.. typically locals() > dir()
globals()
#gives all of the vars avail... often locals() == globals()

sys.path
# gives the available paths

who
# gives defined vars and 'shortcuts'

whos
# lists the modules that are activated

win.close()
#closes window

del
# deletes vars

clear
# clears console


myList = [0,1,2,3]
# Generate a list

len(myList)
# Gives length of list

myList.extend([4])
# add on an element

myList.insert(4,'e')
# add an element to the 4th position

myNewList = [8,12,16,20]
# Create a new list

myList.append(myNewList)
# add using append

myList.extend(myNewList)
#add using extend

# enumerate - number the elements of a list
a=['t','j','k','f','b','n']

for i in enumerate(a, 3): # if no second positional argument is given, it will start at 0.
  print(i)

# OUTPUTS
(3, 't')
(4, 'j')
(5, 'k')
(6, 'f')
(7, 'b')
(8, 'n')


# continues to the next line without executing '\
above_thresh = (yellowPixels[:,:,0] > rgb_thresh[0]) \
                & (yellowPixels[:,:,1] > rgb_thresh[1]) \
                & (yellowPixels[:,:,2] < rgb_thresh[2])


# To run Python in Command Line(Terminal)
chmod +x NameofScript.py
./NameofScript.py

# makes the make beep sound
print('\a')    

# prints a blank line after writing hello
print('Hello\n')

# takes an int input from user
interval = eval(input("Please enter the interval length in seconds: "))

# allows for substitution from SymPy
YZ_intrinsic_num = YZ_intrinsic_sym.evalf(subs={q1: 45*dtr, q2: 60*dtr})

# takes a str input from user
name = input("Please enter name: ")

# formatting strings
'%.8f' % (1/3.0)
# outputs '0.33333333' - 8 decimal places

# Set the separate rows to different variables:
b
# output is:
  Out[225]: 
  array([[3, 4, 5],
         [6, 7, 8]])

b1, b2 = b

b1
# output is:
  Out[227]: array([3, 4, 5])

b2
# output is:
  Out[228]: array([6, 7, 8])


#################### MODULES / LIBRARIES ########################

import numpy
import scipy
import math
import matplotlib
import pylab
import os
import io
import webbrowser
import requests
import datetime
import time
import bs4
import openpyxl # Python to excel module pg.277 of Automate Boring things
import pyautogui #CH.18 'automate the Boring...' manipulate mouse & keyboard
import pyglet # a music / sounds module
import wave
import pyaudio
import sqlite3
import tkinter
import sympy


####################### Package Management ########################

# from the OS terminal to include python packages in Anaconda
conda install packageName

# If you're using regular python package manager
pip3 install serial
# OR
sudo pip3 install modulename


###################### BASIC PYTHON LISTS, TUPLES #################

# Lists - can be changed
# Tuples - cannot be changed (immutable)

# Lists
A=[1,2,3,4]
A[0]
Out[138]: 1   # First object in the list is a 1.
# Remember Python is a indexed at 0

A[0]=2
Out[145]: [2, 2, 3, 4]  # replaces the '1' with a 2

# Tuples
a=(1,2,3,4)
a[0]
Out[163]: 1

a=((1,2),(3,4))
# Generates a 2x2 tuple matrix

a[0]=2
# the output generates an error
# TypeError: 'tuple' object does not support item assignment

red_channel[:,:,[1, 2]] = 0 # Zero out the green and blue channels
# can be read as, all rows, all columns, items 1 and two of the 3-tuple


########## FOR LOOPS

#INPUT CODE
count=0
while(count<5):
    print (count)
    count +=1
else:
    print ("count value reached %d" %(count))

#OUTPUTS THE FOLLOWING	
0
1
2
3
4
count value reached 5
#

for i in range(10):
    pag.moveTo(100, 100, 0.25)
    pag.moveTo(200, 100, 0.25)
    pag.moveTo(200, 200, 0.25)
    pag.moveTo(100, 200, 0.25)



# Meaning of %d and %s
They are used for formatting strings. %s acts a placeholder for a string while 
%d acts as a placeholder for a number. Their associated values are passed 
in via a tuple using the % operator.



#####################   MATRICES    #################

# Transpose function

import numpy
from numpy import *

a = [1,2,3,4,5]
aT = matrix(a).transpose()

# transpose output
Out[46]: 
matrix([[1],
        [2],
        [3],
        [4],
        [5]])


# Reshaping function

c=[1,2,3,4,5,6]
cT = numpy.reshape(c,(2,3))

# reshaping output
Out[60]: 
array([[1, 2, 3],
       [4, 5, 6]])


# Get the total number of units in a matrix
# or a vector. Output = rows X columns

size(matrix name, axis=0 or 1) #axis is optional. 0=rows, 1=columns

# gives the matrix dimensions
numpy.shape(matrix name)


# Increment
X+=1
# Decrement
X

-=1


# manipulating / altering matrices
matrix_name[row, column]

green_channel[:,:,[0, 2]] = 0 # Zero out the red and blue channels

# in a large matrix, with multiple items per positions, this tells the program to include, all rows ':', all columns ':', and items 0 and 2 in the list
# items R G B - zero referencing the RED, 2 referencing the blue

# create a Matrix

numpy.zeros((rows, columns))

numpy.matrix([[1, 2],[3, 4]])
# outputs
		matrix([[1, 2],
        [3, 4]])


# use of a for loop

for row in range(0,np.size(blue_channel,0)): #this goes across the rows
    for col in range(0,np.size(blue_channel,1)): #this goes across the columns
        if(blue_column[row,col] > 45):
            blue_channel_test[row,col] = 1
        else:
            blue_channel_test[row,col] = 0

# now display the grayscale image

plt.imshow(blue_channel_test, cmap='gray')
# plt is matplotlib.pyplot

# From SYMPY - See the Sympy Module section
a = Matrix([[1,1,2],[3,4,5],[6,7,8]])



######################################################## CLASSES ########################################################

class Databucket():
    def __init__(self):
    	# The __init__ function is called a constructor, or initializer, and is automatically called when you create a new instance of a class.
        self.images = csv_img_list  
        # the quoted names below are column headers in the csv file
        self.xpos = df["X_Position"].values
        self.ypos = df["Y_Position"].values
        self.yaw = df["Yaw"].values
        self.count = -2 # This will be a running index, setting to -1 is a hack
                        # because moviepy (below) seems to run one extra iteration
        self.worldmap = np.zeros((200, 200, 3)).astype(np.float)
        self.ground_truth = ground_truth_3d # Ground truth worldmap

# Instantiate a Databucket().. this will be a global variable/object
# that you can refer to in the process_image() function below
data = Databucket()

# We can now make calls to this class since we instantiated it with 'data':

data.count += 1 # Keeps track of the index in the Databucket() by incrementing

data.yaw[data.count] # calls the current yaw position from the Databucket()



####################################### EXCEPTION HANDLING #############################

### Example 1:
# Runs through the list and executes the command even if there is an error
for i in range(len(emailList)):
    
    try:
        outputWriter.writerow([emailList[i]])

    except UnicodeEncodeError:
        pass
    
# can also use an except clause without specifying the error name:
    
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise



### Example 2:
  # A nice way to set up a program to handle errors:

def main():  
  try:

    # Your primary code here...
      
  except UnboundLocalError:
      plt.savefig(imageDirectory + imageName[0:-4] +'faceDetect.jpg')
      # Save the file
      print("Make sure there are faces and eyes in your image!")
      # Exception for an image without faces and/or eyes
      
  except FileNotFoundError:
      print("Image not found. Verify the file name and path!")
      # Exception for bad image path
main()



######################################################    MODULES   ##################################################################


######################################################    MODULES   ##################################################################


######################################################    MODULES   ##################################################################


######################################################    MODULES   ##################################################################


######################################################    MODULES   ##################################################################


######################################################    MODULES   ##################################################################


######################################################    MODULES   ##################################################################


######################################################    MODULES   ##################################################################


######################################################    MODULES   ##################################################################


######################################################    MODULES   ##################################################################


######################################################    MODULES   ##################################################################


######################################################    MODULES   ##################################################################


######################################################    MODULES   ##################################################################


######################################################    MODULES   ##################################################################


######################################################    MODULES   ##################################################################


######################################################    MODULES   ##################################################################


######################################################    MODULES   ##################################################################


######################################################    MODULES   ##################################################################





################################################ MATPLOTLIB MODULE ############################


import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Define the filename, read and plot the image

filename = 'camera_test_image.jpg'

image = mpimg.imread(filename)
# the mpimg.imread transfers the image file into a 3tuple numerical array

plt.imshow(image)
#displays the given jpg image in the command line
plt.show()

%matplotlib inline
# brings windows back into the console
# this can also be set from the preferences menu and changed from "inline" to automatic

plt.close()
#closes the opened window

# some plyplot functions to generate multiple images on one window, draw an arrow, etc
fig = plt.figure(figsize=(12,9))
plt.subplot(221)
# The 22X naming convention means the figure will be broken into that many rows and columns
plt.imshow(image)
plt.subplot(222)
plt.imshow(warped)
plt.subplot(223)
plt.imshow(colorsel, cmap='gray')
plt.subplot(224)
plt.plot(xpix, ypix, '.')
plt.ylim(-160, 160)
plt.xlim(0, 160)
arrow_length = 100
x_arrow = arrow_length * np.cos(avg_angle)
y_arrow = arrow_length * np.sin(avg_angle)
plt.arrow(0, 0, x_arrow, y_arrow, color='red', zorder=2, head_width=10, width=2)
plt.show()




################################################## NUMPY MODULE ############################

import numpy as np

np.mean(yellowPixels[:,:,0])
# gives the average of all rows, all columns, and the first of the tuples. This is for an RGB average. Specifically, "Red"


blueMin = np.min(yellowPixels[:,:,2])
redMax = np.max(yellowPixels[:,:,0])
# min / max functions

np.size(var, which_axis)
np.size(image, 0)
# returns the number of rows

# has the same effect as:
var.shape[0]
image.shape[1]
# returns the number of columns

np.shape(image)
# gives use the size of the matrix


numpy.nonzero()
image.nonzero()
# determines values that are non-zero

np.reshape(list, (rows,cols))
np.reshape(a, (2,2))

np.clip(a, a_min, a_max, out=none)
# truncates values
# example:
b=[1,2,3,4,5,6,7,8,9,0]
np.clip(b, 1, 4)
Out[33]: array([1, 2, 3, 4, 4, 4, 4, 4, 4, 1])
# replaces values above 4 with 4; and replaces values less than 1 with 1.
# How is this useful? See below for use with the rover:

steering = np.clip(avg_angle_degrees, -15, 15)
# our avg_angle_degrees turns out to be 39, but we can only turn a maximum of 15 degrees at a time


degrees = angle_in_radians * 180/np.pi
# converts radians to degrees

yaw_rad = yaw * np.pi / 180
# converts degress to radians


dist = np.sqrt(x_pixel**2 + y_pixel**2)
# above is pythagorean's theorem
# dist is C, or hypoteneuse
# Calculate angle away from vertical for each pixel
angles = np.arctan2(y_pixel, x_pixel)


area = np.concatenate((redcol, greencol, bluecol), axis=2)
# joins the three columns(160,320,1) together as a (160, 320, 3) array

np.isfinite(Rover.vel)
# returns a boolean value for if the inputted value is finite




######################################### SYMPY MODULE - MATRIX MANIPULATION ############################

# "SymPy is a full-featured computer algebra system (CAS) that will enable you to construct and 
# manipulate matrices symbolically and then numerically evaluate them when needed."
# Learn more at: http://docs.sympy.org/latest/tutorial/matrices.html

from sympy import symbols, cos, sin, pi, simplify, eye, zeros, ones, diag
from sympy.matrices import Matrix


# examples:

# standard square matrix

a = Matrix([[1,1,2],[3,4,5],[6,7,8]])


# column vector:
colVec = Matrix([1,2,3,4,5])

# Matrix
P = Matrix([[ ],
            [ ],
            []])

# returns the shape of the matric
a.shape
colVec.shape

# returns the selected row or column
a.row(0)

a.col(0)

# inverse of a matrix
a**-1

# Transpose of a matrix
a.T

# Create the identity matrix
eye(3)

# Create an empty matrix
zeros(3,2)

# Create a matrix with ones
ones(4,2)

# Creates a square matrix with only the diagonal elements filled in
diag(2,2,2,2,2)

# To compute the determinant, use det
M = Matrix([[1, 0, 1], [2, -1, 3], [4, 3, 2]])

M.det()

# Conversions between radians to degrees
rtd = 180./np.pi # radians to degrees
dtr = np.pi/180. # degrees to radians

# Now we create the rotation matrices for elementary rotations about the X, Y, and Z axes, respectively.

# The about Z rotation matrix is derived on page 45


R_x = Matrix([[ 1,              0,        0],
              [ 0,        cos(q1), -sin(q1)],
              [ 0,        sin(q1),  cos(q1)]])
# Rotation about X axis

R_y = Matrix([[ cos(q2),        0,  sin(q2)],
              [       0,        1,        0],
              [-sin(q2),        0,  cos(q2)]])
# Rotation about Y axis

R_z = Matrix([[ cos(q3), -sin(q3),        0],
              [ sin(q3),  cos(q3),        0],
              [ 0,              0,        1]])
# Rotation about Z axis

offset =  Matrix([[offsetX],
                  [offsetY],
                  [offsetZ]])


T_x = Matrix([[ 1,            0,         0,   offset[0]],
              [ 0,      cos(q1),  -sin(q1),   offset[1]],
              [ 0,      sin(q1),   cos(q1),   offset[2]],
              [ 0,            0,           0,       1]])    
# Homogenous Transform about the X axis

T_y = Matrix([[cos(q2),        0,  sin(q2),   offset[0]],
            [       0,         1,        0,   offset[1]],
            [-sin(q2),         0,  cos(q2),   offset[2]],
            [       0,         0,        0,          1]])    
# Homogenous Transform about the Y axis

T_z = Matrix([[cos(q3),   -sin(q3),       0,  offset[0]],
            [  sin(q3),    cos(q3),       0,  offset[1]],
            [        0,          0,       1,  offset[2]],
            [        0,          0,       0,         1]])    
# Homogenous Transform about the Z axis


alpha = rtd * atan2(R_XYZ[1,0], R_XYZ[0,0]) 
beta  = rtd * atan2(-R_XYZ[2,0], sqrt(R_XYZ[0,0]**2 + R_XYZ[1,0]**2) )
gamma = rtd * atan2(R_XYZ[2,1], R_XYZ[2,2])

    
# Numerically Evaluate the matrices 

print("Rotation about the X-axis by 45-degrees")
print(R_x.evalf(subs={q1: 45*dtr}))
print("Rotation about the y-axis by 45-degrees")
print(R_y.evalf(subs={q2: 45*dtr}))
print("Rotation about the Z-axis by 30-degrees")
print(R_z.evalf(subs={q3: 30*dtr}))
# Evaluates as a floating point number


# Row Join:
Ra = Matrix([[1, 0, 0],
             [0, 1, 0],
             [0, 0, 1]])
    
Ta = Ra.row_join(Matrix([[0],  
                         [0],
                         [0]]))

				# OUTPUT:
				Matrix([
				[1, 0, 0, 0],
				[0, 1, 0, 0],
				[0, 0, 1, 0]])


bottomRow = Matrix([[0,0,0,1]])
# Make a row vector

# Column join:
Tb_a = Rb_a.row_join(tb_a).col_join(bottomRow)


######################################################### PILMODULE ############################

from PIL import Image

pil_im = Image.open('chrysler.jpg')
grey_im = Image.open('chrysler.jpg').convert('LA')
# Converts to greyscale
imshow(grey_im)
grey_im.save('greyChrysler.png')

plt.figure()
plt.gray()
gryChrysler = plt.contour(gray_pil_im, origin='image')
axis('equal')
axis('off')
plt.savefig('grayContourChrysler.png')

# Greyscale is roughly: Y = 0.299 R + 0.587 G + 0.114 B 


R = pil_im[:,:,0]
G = pil_im[:,:,1]
B = pil_im[:,:,2]

grey_pil_im = 0.299*R + 0.587*G + 0.114*B 
imshow(grey_pil_im)

# color List = b,g,r,c,m,y,k,w

######################################################### OPEN CV MODULE ############################


import cv2

cv2.getPerspectiveTransform() 
cv2.warpPerspective()
# Used in our first project in Udacity Nanodegree

face_cascade = cv2.CascadeClassifier('/Users/UserName/anaconda/envs/py35/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/Users/UserName/anaconda/envs/py35/share/OpenCV/haarcascades/haarcascade_eye.xml')
# Used in face and eye recognition 'facialRecognition.py'

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
for (x,y,w,h) in faces:
    face = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]


eyes = eye_cascade.detectMultiScale(roi_gray)
        
for (ex,ey,ew,eh) in eyes:
    eye = cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)



######################################################### PYLAB CV MODULE ############################

import pylab
pylab.savefig('filename.png')
pylab.savefig('filename.png', bbox_inches='tight')
class matplotlib.figure.Figure(figsize=None, dpi=None, facecolor=None, edgecolor=None, linewidth=0.0, frameon=None, subplotpars=None, tight_layout=None)
# saves file as .png




########################################################## PANDAS MODULE ############################




import pandas as pd
# Change the path below to your data directory
# If you are in a locale (e.g., Europe) that uses ',' as the decimal separator
# change the '.' to ','
df = pd.read_csv('../test_dataset/robot_log.csv', delimiter=';', decimal='.')







########################################################## TIME MODULE ############################

import time

time.sleep(2)
# waits 2 seconds

time.ctime()
# Outputs 'Tue Jan 17 17:54:05 2017'

start = time.time()

end =  time.time()

print(end -  start)
# time elapsed



##########################################################  DATE TIME MODULE ######################

import datetime

datetime.datetime.now().time()
# outputs just time

datetime.datetime.now()
# outputs the date and time

str(datetime.datetime.now())
# makes it human readable

datetime.datetime.utcnow()
# gives universal time zone



######################################################## SQLite3 MODULE ####################

from sqlite3 import connect
conn = connect(r'/Users/ChrisErnst/temp.db')
# generates a .db file

curs = conn.cursor()

curs.execute('create table emp (who, job, pay)')

prefix = 'insert into emp values '
curs.execute(prefix + "('Bob', 'dev', 100)")
curs.execute(prefix + "('Sue', 'dev', 120)")

curs.execute("select * from emp where pay > 100")
for (who, job, pay) in curs.fetchall():
    print(who, job, pay)

payscale = curs.execute("select * from emp where pay > 90")
payscale.fetchall()
# outputs all employees making > 90





############################################################### GLOB MODULE ##########################
import glob
import os

os.chdir('path/to/image/folders/')

images = glob.glob('*.jpg')
# Creates a list of images from the given directory that end in .jpg

cars = []
notcars = []
for image in images:
    if 'image' in image or 'extra' in image:
        notcars.append(image)
    else:
        cars.append(image)
# a useful classifier



############################################################### SKLEARN MODULE ##########################
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split # OR
from sklearn.model_selection import train_test_split # >V0.18 Scikit-learn

# see more on svm.py and svm_image_classifier.py

# It must be one of ‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’ or a callable
svc = svm.SVC(kernel='linear').fit(X, y)

# READ THE DOCS: http://scikit-learn.org/stable/modules/classes.html#module-sklearn.svm
# http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html





############################################################### CSV MODULE ##########################



# Send to CSV
import csv

# Open an existing csv/ or create one if not existing
outputFile = open('testcontacts.csv', 'w', newline='')

# Write to that csv
outputWriter = csv.writer(outputFile)

outputWriter.writerow(list1)

outputFile.close()



# Writes to three separate rows

outputWriter.writerow([list1[0]])

outputWriter.writerow([list1[1]])

outputWriter.writerow([list1[2]])






################################################################### GUI AUTOMATION MODULE #############



import pyautogui as pag

pag.PAUSE = 1  
# sets the pause between commands to one second

pag.FAILSAFE = True 
# allows a cease of the program if the mouse if navigated
# to the upper left hand corner of the screen

pag.size() 
# outputs the size of the current working screen
screenWidth, screenHeight = pag.size()
# sets vars from outputs


pag.moveTo(100, 200, 2)
# moves the mouse pointer to the indicated location (X, Y, time in seconds to complete)

pag.moveRel(0, -200, 2)
# moves the cursor relative to current position (positive-up, neg-down)


pag.hotkey('command', ' ')
# opens the spotlight on OSX

pag.typewrite('write this string')
#types the string

pag.confirm(text='', title='', buttons=['OK', 'Cancel'])
#creates a dialog box

# a loop to move mouse in a square
for i in range(10):
    pag.moveTo(100, 100, 0.25)
    pag.moveTo(200, 100, 0.25)
    pag.moveTo(200, 200, 0.25)
    pag.moveTo(100, 200, 0.25)
    
    
# Navigates to file save, and saves file    
pag.moveTo(126, 7, 2)
pag.click()
pag.moveTo(137, 120, 1.5)
pag.click()



# opens chrome and searches the words below
import time
pag.hotkey('command', ' ')
pag.press('c')
pag.press('h')
pag.press('r')
time.sleep(2)
pag.press('enter')

pag.hotkey('command', 't')

time.sleep(1)
pag.typewrite('puppers')

pag.press('enter')

# finds an image on the screen


button7location = pag.locateOnScreen('calc7key.png')
button7location
(1416, 562, 50, 41)
button7x, button7y = pag.center(button7location)
button7x, button7y
(1441, 582)
pyautogui.click(button7x, button7y)  
# clicks the center of where the 7 button was found




# 
import time
pag.hotkey('command', ' ')
pag.press('c')
pag.press('h')
pag.press('r')
time.sleep(2)
pag.press('enter')

pag.hotkey('command', 't')

time.sleep(1)
pag.typewrite('images.google.com')

pag.press('enter')

pag.typewrite('apple')

pag.press('enter')

time.sleep(1)2
list(pag.locateAllOnScreen('lookslikethis.jpg'))


# prints mouse position constantly
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')




# Verify dependencies are installed with:
    sudo pip3 install pyobjc-framework-Quartz, sudo pip3 install pyobjc-core
    # then
    sudo pip3 install pyobjc

# If the GUI automation gets out of hand, use:

    # command-shift-option-q 
    
# To pause the program:

import time
import pyautogui as pag
pag.PAUSE = 1 
# sets the pause to 1 sec between commands
pag.FAILSAFE = True  
#Enables the failsafe feature




# Moving the Mouse:
    
    # Upper left corner is 0,0
    
pag.size()  
# gets the display size

width, height = pag.size() 
# sets the width and height

pag.moveTo(100,100, duration=0.25)  
# moves the mouse to 100,100, and takes 1/4 sec

pag.moveTo(width, height)
# moves mouse instantaneously

pag.moveRel(0,-200)
# moves the mouse up relatively from where it is now

pag.position()
#outputs the current position of the mouse

pag.scroll(200)
# scrolls up

pag.screenshot()
#returns a screenshot in idle, might want to use command shift 3






# Clicking the Mouse

pag.click()
#clicks the left button of the mouse

pag.click(100,200, button='right')
# clicks the right button at x=100, y=200

pag.mouseDown()
pag.mouseUp()
# clicks up and down

pag.doubleClick()
# double clicks the left mouse





# Typing from the keyboard

pag.typewrite('message')
# types this out

pag.KEYBOARD_KEYS
# lists the keyboard keys

pag.keyDown('shift')
pag.press('4')
pag.keyUp('shift')
# Will type a dollar sign

pag.hotkey('a', 'shift', '4')
# types these and releases them in order

pag







################################################################## WEB SCRAPING - REQUESTS MODULE #############


import requests

page1 = requests.get('http://automatetheboringstuff.com/files/rj.txt')

print(page1.text[:200])
# returns the text from that page


import requests, bs4
weather = requests.get('http://forecast.weather.gov/MapClick.php?lat=34.0017&lon=-118.432#.WHgOSbYrJE4')
weather.raise_for_status()
weatherPage = bs4.BeautifulSoup(weather.text)

tempNum = weatherPage.select('.myforecast-current-lrg')
# selects the exact piece of html (page 246 of automate the boring stuff)

tempNum[0].getText()
# should generate the current temp from the weather channel






######################################################################### TWILIO LIBRARY ##########################


import requests, bs4, time, datetime
from twilio.rest import TwilioRestClient


accountSID = 'ACdc4349031e6b84317d5094068c68e1e8'
authToken = 'bb2c8170acf11297272709a35b1fea25'

twilioCli = TwilioRestClient(accountSID, authToken)

myTwilioNumber = '+13109058114'
# Required to send outgoing texts. This is foregone if unused for 30days

myCellPhone = '+13104334826'
#myCellPhone = '+12138840477'


message = twilioCli.messages.create(body=
                    ('\n\n\n' + 'Surf Report:' + '\n\n' + waveHeight + ', Water Temp:' + waterTemp + 
                     ', Wave Direction: '+ meanWaveDirection
                     + '\n\n' + tide1Time + ' ' + tide1Type + tide1Height
                     + '\n' + tide2Time + ' ' + tide2Type + tide2Height
                     + '\n' + tide3Time + ' ' + tide3Type + tide3Height 
                     + '\n' + tide4Time + ' ' + tide4Type + tide4Height + 
                     '\n\n' + update[0:14]+'Buoy '+ update[14:39]+ ', '+ update[50:61]), 
                    from_=myTwilioNumber, to=myCellPhone)
                    
# Write a SMS text with the waveheight, waterTemp, and waveDirection





######################################################################### BEAUTIFUL SOUP LIBRARY ##########################


surf = requests.get('http://www.ndbc.noaa.gov/station_page.php?station=46221')
tides = requests.get('https://tidesandcurrents.noaa.gov/noaatidepredictions.html?id=9410840&legacy=1')
# completes the http request        

soupSurfPage = bs4.BeautifulSoup(surf.text, "lxml")
soupTidePage = bs4.BeautifulSoup(tides.text, "lxml")        
# creates a beautiful soup object in lxml format







######################################################################### GRAPHICS LIBRARY ##########################


import graphics
#imports John Zeele's Graphics Lib

from graphics import *
#this is vital

win = GraphWin('Supply & Demand', 320, 240)

#draws a '0' on the graph. REMINDER: The window is indexed from the upper left corner.
Text(Point(20, 230), '0').draw(win)

#full text of Y axis below
win = GraphWin('Supply & Demand', 320, 240)
Text(Point(20, 230), '0').draw(win)
Text(Point(20, 30), '$15').draw(win)
Text(Point(20, 96.68), '10').draw(win)
Text(Point(20, 163.34), '5').draw(win)

#draw two different bars
bar = Rectangle(Point(25, 230),Point(40,100))
bar.setFill("green")
win.setBackground("white")
bar.draw(win)

#bar 2 of 2
bar1 = Rectangle(Point(40,230), Point(55,90));
bar1.setFill("blue");
bar1.draw(win)

#new wider bar
bar2 = Rectangle(Point(55,230), Point(70,90));
bar2.setFill("blue");
bar2.draw(win)

#Draw lines
#Option 1, set points
p1=Point(70,90)
p2=Point(105,90) 
line1=Line(p1, p2)
line1.draw(win)

#Option 2, describe points
line2 = Line(Point(105,90),Point(105,75))
line2.draw(win)

line3 = Line(Point(105,75),Point(130,75))
line3.draw(win)

#Sets the line color
line3.setFill("red")

#Color options -- those I could think of

>>> line3.setFill("red")
>>> line3.setFill("green")
>>> line3.setFill("brown")
>>> line3.setFill("yellow")
>>> line3.setFill("black")
>>> line3.setFill("blue")
>>> line3.setFill("cyan")
>>> line3.setFill("purple")
>>> line3.setFill("magenta")
>>> line3.setFill("pink")
>>> line3.setFill("orange")
>>> line3.setFill("tan")
>>> line3.setFill("grey")

#Code below is for drawing a graph#

import os

import graphics

#Code below is for drawing a graph#

# 4:3 proportioned window
win = GraphWin('Supply & Demand', 800, 600)

#lines for axes
xaxis = Line(Point(20, 560), Point(780,560))
xaxis.draw(win)

yaxis = Line(Point(40,20), Point(40,580))
yaxis.draw(win)

#draw axes labels

# Y Axis
Text(Point(20, 15), '$').draw(win)

# X Axis
Text(Point(780,585), 'MW').draw(win)




