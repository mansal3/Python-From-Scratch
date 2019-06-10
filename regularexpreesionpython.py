#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 07:39:29 2019

@author: manpreetsaluja
"""

#REGULAR EXPRESSION
#A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern. Regular expressions are widely used in UNIX world.

#The module re provides full support for Perl-like regular expressions in Python. The re module raises the exception re.error if an error occurs while compiling or using a regular expression.

#We would cover two important functions, which would be used to handle regular expressions. But a small thing first: There are various characters, which would have special meaning when they are used in regular expression. To avoid any 
#
#confusion while dealing with regular expressions, we would use Raw Strings as r'expression'.


#re is package of regular experession
import re
#message
msg="i am Nancy my age is 13 and my sister Kawaldeep age is 20"
#finding age using re
age=re.findall(r'\d{1,3}',msg)
print(age)
#name in 
name=re.findall(r'[A-Z][a-z]*',msg)
print(name)

agedict={}
x=0

for eachname in name:
    agedict[eachname]=age[x]
    x=x+1
    
    print(agedict)
    
#FINDALL
    import re
    msg1="my name is nikhil find my name print my name"
    name=re.findall("name",msg1)
    print(name)
    count=0
    for eachname in name:
        count=count+1
        
        print(count)
        
        
#FIND Iterator
        
    import re
    msg1="my name is nikhil find my name print my name"

    for eachname in re.finditer("name",msg1):
      pos=eachname.span()    
      print(pos)
      
      
#FIND PATTERN
      
      import re
      msg2="amm,bam,cam,pam,tam,ram,dham,kam"
      
      name1=re.findall(r"[a-z]am",msg2)
      print(name1)
      
#REPLACE STRING
      
      import re
      msg3="Am,Ram,Zam"
      names=re.compile(r"[R]am")
      name=names.sub("Rama",msg3)
      print(name)
      
      
#DIVIDING SPECIAL<ALPHABETIC and NUMBERS
      
     import re
     msg4="hi 4609isuhsds hdwbdssjkSBU#$%^#^&@#^*@#()"
     re.sub("[A-Za-z]"," ",msg4)
       
     re.sub("[^A-Za-z]"," ",msg4)
     
#another example
     
     import re
     msg5="""my
             Name
             is
             Nancy"""
   regex=re.compile("\n")
   withoutspace=regex.sub("",msg5)
   withoutspace
   
#NUMBERS
   import re
   nsentence="e52786529bdhwdhe9329729hdwed27082702"
   numbers=re.findall("\d",nsentence)
   nsentence
   

   