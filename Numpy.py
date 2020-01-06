# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 16:34:39 2019

@author: Jmore
"""
#Udemy
#Numpy exercise

import numpy as np
#1. Create an array of 10 zeros
zero_arr = np.zeros(10)
print("an array of 10 zeros: {}".format(zero_arr))

#2. Create an array of 10 ones
ones_arr = np.ones(10)
print("an array of 10 ones: {}".format(ones_arr))

#3. Create an array of 10 Fives
fives_arr = ones_arr * 5
print("an array of 10 Fives: {}".format(fives_arr))

#4. Create an array of integers from 10 to 50
arr_ten_fifty = np.arange(10,51)
print("an array of integers from 10 to 50: \n{}".format(arr_ten_fifty))

#5. Create a 3X3 matrix with values ranging from 0 to 8
zero_eight_3_3 = np.arange(0,9).reshape(3,3)
print("a 3X3 matrix with values ranging from 0 to 8:\n{}".format(zero_eight_3_3))

#6. Create a 3X3 identity matrix
identity_3_3 = np.eye(3)
print("a 3X3 identity matrix:\n{}".format(identity_3_3 ))

#7. Random number
import numpy.random
rand_num = numpy.random.rand()
print("Numpy Random number: {}".format(rand_num))

#8. 25 random numbers from standard normal distribution
rand_num_sd = np.random.randn(25)
print("Numpy 25 random numbers from standard normal distribution:\n{}".format(rand_num_sd))
print("and its length: {}".format(len(rand_num_sd)))

#9. Matrix
mat = np.arange(1,101)/100
print(mat)

#10. 20 linearly spaced points
linsp = np.linspace(0,1,20)
print("20 linearly spaced points: {}".format(linsp))

#11. Numpy indexing and selection is same as list/any other data structure
#you can slice a Numpy array same as a list

f_f = np.arange(1,26).reshape(5,5)
print(f_f)
print("Print the 2nd row and 3rd row(starting from 0) {} ".format(f_f[2:4]) )
print("slicing 11, 16 from the matrix:\n {}".format(f_f[2:4,0:1]))
print("Slice 14, 15, 19 and 20 from the matrix:\n{}".format(f_f[2:4,3:]))

#12. Sum of all elements of an array
print("Sum of 5X5 matrix above: {}".format(np.sum(f_f)))

#13. Standard deviation
print("Numpy Standard deviation of 5X5 matrix above: {}".format(np.std(f_f)))

#14. Get sum of all the columns
print("Column wise sum of above 5X5 matrix: \n{}".format(np.sum(f_f,axis=0)))

####If you want row-wise sum then axis=1