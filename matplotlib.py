# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 18:51:05 2020

@author: Jmore
"""

'''
Matplotlib is a most popular plotting library for Python
It gives you control over every aspect of a figure
It was designed to have a similar feel to MatLab's(Which is another programming language) graphical plotting
https://matplotlib.org/
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x_arr = np.linspace(1,5,10)
y_arr = x_arr ** 2

print("X: {}".format(x_arr))
print("Y: {}".format(y_arr))

plt.plot(x_arr,y_arr)
plt.xlabel('X label')
plt.ylabel('Y label')
plt.title('Plot Title')
plt.show()

#Now, let try to multi plot on the same canvas
#First subplot
plt.subplot(1,2,1) #No.of rows, no.of columns, plot number
plt.plot(x_arr,y_arr,'r')

#Second subplot
plt.subplot(1,2,2)
plt.plot(y_arr,x_arr,'g')

### For ploting a single plot we are just passing the data, but for the subplots we are also 
### passing the no.of rows and columns to occupy in the image and then plotting it

########################## Object oriented matplotlib

fig = plt.figure()
axes1 = fig.add_axes([0.1,.2,.8,.8]) #left,bottom, width, height and all the dimensions have to be in %. so the values range between 0-1

axes1.plot(x_arr,y_arr,'g')
axes1.set_title("Object oriented Matplotlib")

axes2 = fig.add_axes([0.2,0.5,0.3,0.3])
axes2.plot(x_arr,y_arr, 'r')
axes2.set_title('Small one')
axes1.set_xlabel('X Axis Label')
axes1.set_ylabel('Y Axis Label')

######################### 
########  fig,axes = plt.subplots()  # by default the no.of rows and columns = 1

fig,axes = plt.subplots(nrows=1,ncols=5) #It divides the canvas into nrows and ncols also this subplots will automatically calls add_axes and returns the axes objects
#fig contains actual figure(i.e., canvas) and axes contains a list of axes objects
# As axes is an iterator, we can iterate through it or we can even index it

for cur_ax in axes:
    cur_ax.plot(x_arr,y_arr,'g*')

### OR we can index it like following

axes[0].plot(x_arr,y_arr,'r--')
axes[1].plot(y_arr,x_arr,'r--')

plt.tight_layout() #it make sure that the axes don't overlap 