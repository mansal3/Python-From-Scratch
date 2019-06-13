#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 07:29:44 2019

@author: manpreetsaluja
"""

#DATA ANALYSIS PYTHON

#NUMPY
#numpy is used to perform all the mathematical operational and statistical operation

list=[1,2,3,4,5,6,7]
#now if i want to multiple all the datapoint of list with a variable say by 2 
list*2
#so rather than increementing the value it will replicate te same
#so for that operation we need to use numpy

import numpy as np
arrayy=np.array(list)
print(arrayy*2)
#[ 2  4  6  8 10 12 14]

#type o
type(arrayy) 

#Shape()
arrayy.shape
#give dimension of array

#Size
arrayy.size

#DataType
arrayy.dtype
#int64

twothree=np.zeros((2,3))
#matrix of 2,3

oneall=np.ones((3,4))
oneall
#matrix of 1 all

full=np.full((2,3),7)
#matrix of all 7

eye=np.eye((2))
#identity matrix

randomrandom=np.random.random((3,3))
randomrandom[2,2]


#reshape
eye
eye.shape
eyenew=np.reshape(2,1)