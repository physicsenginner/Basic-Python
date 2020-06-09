#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 22:42:50 2020

@author: dogukan
"""

# matplotlib kutuphanesi
# gorsellestirma kutuphanesi
# line plot , scatter plot, bar polt , subplots, histogram

import pandas as pd

df = pd.read_csv("original.csv")

print (df.columns)

print(df.Species.unique())

print(df.info())

print (df.describe())

setosa = df[df.Species== "Iris-setosa"]

versicolor = df[df.Species == "Iris-versicolor"]
print(setosa.describe())
print(versicolor.describe())

# %%  

import matplotlib.pyplot as plt
df1 = df.drop(["Id"],axis=1)

#df1.plot()
#plt.show()


setosa = df[df.Species== "Iris-setosa"]

versicolor = df[df.Species == "Iris-versicolor"]

virginica =  df[df.Species == "Iris-virginica"]
plt.plot(setosa.Id,setosa.PetalLengthCm, color = "red", label= "setosa",)
plt.plot(versicolor.Id,versicolor.PetalLengthCm, color = "green", label= "versicolor" )

plt.plot(virginica.Id,virginica.PetalLengthCm, color = "blue", label= "verginica" )

plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()

plt.show()

df1.plot(grid=True, linestyle = ":") # line cesidi
plt.show()


df1.plot(grid=True, alpha=0.3) # saydamlık
plt.show()

# %% scatter plot


setosa = df[df.Species== "Iris-setosa"]

versicolor = df[df.Species == "Iris-versicolor"]

virginica =  df[df.Species == "Iris-virginica"]

plt.scatter(setosa.PetalLengthCm, setosa.PetalWidthCm, color="red",label="setosa")
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm, color = "green", label= "versicolor" )

plt.scatter(virginica.PetalLengthCm, virginica.PetalWidthCm, color = "blue", label= "verginica" )
plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("scatter plor")
plt.show()

# %% histogram 

plt.hist(setosa.PetalLengthCm, bins=15)
plt.xlabel("PetalLengthCm values")
plt.ylabel("frekans")
plt.title("hist")
plt.show()


# %% bar plot

import numpy as np 

x = np.array([1,2,3,4,5,6,7])
a=["turkey","usa","germany","japan","england","brazil","portugal"]
y = x*2+5
plt.bar(a,y)
plt.title("bar plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


# %% sub plots

df1.plot(grid=True, alpha=0.3,subplots=True)
plt.show() 



setosa = df[df.Species== "Iris-setosa"]

versicolor = df[df.Species == "Iris-versicolor"]

virginica =  df[df.Species == "Iris-virginica"]

plt.subplot(2,1,1)
plt.plot(setosa.Id,setosa.PetalLengthCm, color = "red", label= "setosa",)
plt.ylabel("setosa-PetalLengthCm")

plt.subplot(2,1,2)
plt.plot(versicolor.Id,versicolor.PetalLengthCm, color = "green", label= "versicolor" )
plt.ylabel("versicolor-PetalLengthCm")

plt.plot()




















