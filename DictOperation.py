#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 07:29:34 2019

@author: manpreetsaluja
"""

#DICTIONARies
#Dictonieries are mutable datatype
#works on key value pair

dict1={'1':'nancy','2':'manpreet','3':'rishi'}
#defining dict

print(dict1['1'])
#nancy

#update operation

dict1['1']='pal'
print(dict1)
#{'1': 'pal', '2': 'manpreet', '3': 'rishi'}

#DELETE OPERATION

del(dict1['1'])
print(dict1)
#{'2': 'manpreet', '3': 'rishi'}