#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 19:09:07 2020

@author: dogukan
"""

# 1) pandas hizli ve etkili for dataframes
# 2) csv ve text dosyalarinda kolay islem
# 3) NONE value missing value kolay cozum
# 4) reshape yapip data daha etkili kullanilir
# 5) slicing indexing easy
# 6) time series data analizinde cok yardimci
# 7) en onemlisi hiz pandas hizli bir kutuphane

import pandas as pd 

dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],
              "AGE":[15,65,65,78,241,45],
              "SALARY":[564,341,645,341,46,313]}


dataFrame1 = pd.DataFrame(dictionary)

head = dataFrame1.head()

tail = dataFrame1.tail()
# %%
# pandas basic method

print (dataFrame1.columns)

print(dataFrame1.info())
print(dataFrame1.dtypes)

print(dataFrame1.describe()) # numerik features = columns (age,maas)

# %% indexing and slicing

print (dataFrame1["NAME"])

print (dataFrame1["AGE"])

print(dataFrame1.AGE)

dataFrame1["yeni_feature"] = [-1,-2,-3,-4,-5,-6]

print(dataFrame1.yeni_feature)

print(dataFrame1.loc[:,"AGE"])


print(dataFrame1.loc[:3,"AGE"])


print(dataFrame1.loc[:3,["AGE","NAME"]])

print(dataFrame1.loc[::-1,:])


print(dataFrame1.loc[:,:"NAME"])

print(dataFrame1.loc[:,"NAME"])

print(dataFrame1.iloc[:,2])

# %% filtering

filtre1 = dataFrame1.SALARY > 200

filtrelenmis_data = dataFrame1[filtre1]

filtre2 = dataFrame1.AGE < 20

dataFrame1[filtre1 & filtre2]

print(dataFrame1[dataFrame1.AGE > 40])


# %% list comprehension
import numpy as np
ortalama_maas = dataFrame1.SALARY.mean ()

ortalama_maas_np = np.mean(dataFrame1.SALARY)

dataFrame1["maas_seviyesi"] = ["dusuk "if ortalama_maas > i else "yuksek"for i in dataFrame1.SALARY]

#for i in dataFrame1.SALARY:
#    if (ortalama_maas > i):
#        print("yuksek")
#    else:
#        print(""dusuk)


dataFrame1.columns = [i.lower() for i in dataFrame1.columns]

# syntax error
#dataFrame1.columns = [i.split()[0]+ "_"i.split()[1] if len(i.split())>1 for i in dataFrame1.columns]


# %%  drop and concatenating

dataFrame1.drop(["yeni feature"], axis=1, inplace = True)

data1  = dataFrame1.head()
data2 = dataFrame1.tail()

# vertical

data_concat = pd.concat([data1,data2],axis=0)

# horizontal

maas=dataFrame1.salary
age= dataFrame1.age

data_h_concat =  pd.concat([maas,age],axis=1)

# %% transforming data

dataFrame1["lsit_comp"] = [i*2 for i in dataFrame1.age]

# apply()

def multiply (age):
    return age*2
dataFrame1["apply_metodu"]= dataFrame1.age.apply(multiply)










 