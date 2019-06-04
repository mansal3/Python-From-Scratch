#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 07:10:55 2019

@author: manpreetsaluja
"""

#TUPLES OPERATIONS


#tuples are immutable data type
#that means it cannot edit,update,change etc
#once after creasting the tuple you cannot do any change in that

#tuples represent by round brackets

tuple1=('wdff','wdwdsf','qa',213213,4,'hgfd')
print(tuple1)

print(tuple1[1])
#ouput wdwdsf

print(tuple1[1:5])

tuple2=('a','b','c','d','e')
tuple3=tuple1+tuple2

print(tuple3)
#ouut ('wdff', 'wdwdsf', 'qa', 213213, 4, 'hgfd', 'a', 'b', 'c', 'd', 'e')

del(tuple3)
 print(tuple3)
#NameError: name 'tuple3' is not defined
 
 len(tuple2)
 #5
 
 tuple2.count('a')
 #1
 
 tuple2.index('a')
 #0
 
 max(tuple2)
 #e
 
 min(tuple2)
 #a
 