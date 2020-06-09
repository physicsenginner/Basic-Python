#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 18:09:17 2020

@author: dogukan
"""

#importing
import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])  # 1*4   vector

print(array.shape)

a= array.reshape(3,5)
print("shape:",a.shape)
print("dimension:",a.ndim)

print("data type:",a.dtype.name)
print("size:",a.size)

print("type:",type(a))

array1= np.array([[1,23,4],[3,31,3],[6,5,3]])

zeros = np.zeros((3,4))
zeros[0,0]=5
print(zeros)

np.ones((3,4))

np.empty((2,3))

a=np.arange(10,50,5)

print (a)

a2= np.linspace(10,50,20)
print(a2)


# %% numpy basic operations

a=np.array([1,2,3])
b=np.array([3,4,5])
print(a+b)
print(a-b)
print(a**2)

print(np.sin(a))

print(a < 2)

a1= np.array([[1,2,3],[4,5,6]])
b2= np.array ([[1,2,3],[4,5,6]])

#element wise product

print(a1*b2)

# matrix product

a1.dot(b2.T)

print(np.exp(a1))

a3 = np.random.random((5,5))
print(a3.sum())
print(a3.max())
print(a3.min())
print(a3.sum(axis=0))
print(a3.sum(axis=1))

print(np.sqrt(a3))
print(np.square(a3))  # a**2

print(np.add(a3,a3))


# %% indexing and slicing

array = np.array([1,2,3,4,5,6,7])  # vector dimension=1
print(array[0])
print(array[0:4])

reverse_array= array[::-1]
print(reverse_array)

array5 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(array5)

print(array5[1,1])

print(array5[:,1])

print(array5[1,1:4])

print(array5[-1,:])

print(array5[:,-1])

# %% shape manipulation

array = np.array([[1,2,3],[4,5,6],[7,8,9]])

# flatten

a = array.ravel()

array2= a.reshape(3,3)

array3 = array2.T 

print (array3.shape)


array5= np.array([[1,2],[3,4],[4,5]])

# %% stacking arrays

array1 = np.array ([[1,2],[3,4]])
array2 = np.array ([[-1,-2],[-3,-4]])

array3 = np.vstack((array1,array2)

array4 = np.hstack((array1,array2))


# %%  convert and copy

liste =[1,2,3,4]
array=np.array (liste)


liste2= list(array)

a = np.array([1,2,3,4])
b=a
b[0] = 5
c=a


d = np.array([1,2,3,4])

e = d.copy()
f=d.copy()


























