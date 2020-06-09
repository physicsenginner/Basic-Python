#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 23:17:08 2020

@author: dogukan
"""

# %% syntax error
print (9)
#print 9
int (10.0)
#int 10.0

i=0
while (i<10):
    print(i)
    i=i+1
    
# %% exceptions
    
a= 10
b="2"
liste = [1,2,3]
print(sum(liste))
#print(a+b)
print(str(a)+b)
k=10
zero=0
print(k)
#a=k/zero #hata

if(zero==0):
    a=0
else:
    a=k/zero


try:
    a=k/zero
except ZeroDivisionError:
    a=0


# index error

liste1=[1,2,3,4]
liste1[15]

#module not found error

import numpyy

#file not found error

import pandas as pd
pd.read_csv("asd")

# type error
"2"+2

#value error
int ("1asd")


try:
    1/0
except:
    print("except")
else:
    print("else")
finally:
    print("done")


a= "zaa"
b= "maa"
print("aa" in 2*(a+b))


a={1:"A",2:"B"}
for i,j in  a.items():
    print(i,j,end ="-")



if True or False and True:
    print("a")
else:
    print("e")



c=1
while True:
    if c%3==0:
        break
    print(c)
    c=c+1











