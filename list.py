#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 21:17:15 2020

@author: dogukan
"""
# %%
# list

liste = [1,2,3,4,5,6]
print (type (liste))
liste_str = ["pazartesi", "sali", "carsamba"]
type(liste_str)

value = liste [1]
print (value)

last_value = liste [-1]
print(last_value)
liste_divide = liste [0:3]
print (liste_divide)

liste.append(7)
liste.remove(7)
liste.reverse ()

liste2= [1,3,5,2,4]
liste2.sort()

string_int_liste = [1,2,3,"a","b"]


# %% tuple

t = (1,2,3,4,4,5,6)

t.count(4)

t.index(3)

# %% dictionary

dictionary = {"ali":32,"veli":45,"mehmet":65}

#ali, veli , metmet = keys
# 32,45,65 = values

def deneme():
    dictionary = {"ali":32,"veli":45,"mehmet":65}
    return dictionary
dic = deneme ()

# %% conditionals
# if else statement

var1  = 20
var2 = 20

if(var1 > var2):
    
    print ("var1 buyuktur var2"),
elif (var1==var2):
    print ("var1 eşittir var2")
else:
    print("var1 kucuktur var2")
    
liste = [1,2,3,4,5,]
value=3
if value in liste:
    print ("evet {} degeri listenin icinde".format(value))
else:
    print ("hayir yok")
    
    
dic = {"ali":32,"veli":45,"mehmet":65}
    
keys = dic.keys()
print (keys)
if "ali " in keys:
    print ("evet")
else:
    print("hayır")
    
# %% 
    
#  1640. yil == 17. yuzyil
# 109. yil == 2.yuzyil
# 2000.yil == 20.yuzyil
    
# metodyazin 
    #input integer yillar
    #output integer yuzyil
    
# input = year >> 1 <= year <= 2005
# syntax hatası veriyor!!
def year2century(year):
    """
    year to century
    """
    str_year = str(year)
    
    if (len(str_year)<3):
        return 1
    elif (len(str_year) == 3):
        if((str_year[1:3]) == "00") # 100,200,300.....
            return int (str_year[0])
        else:                   # 190,250,450......
            return int (str_year[0])+1
    else:                       # 1750,1700,1805
        if((str_year[2:4])=="00"): #1700,1800..
            return int(str_year[:2])
        else:                   # 1705,1805,1645
            return int( str_year[:2])+1
            
    
    
# %% Loops
# for loop

for each in range (1,11):
    print(each)
    
for each in "ankara ist":
    print(each)
    
for i in "ankara ist".split():
    print(i)
    
liste = [1,3,5,9,5,74,5,34,48534]
sum(liste)
count=0
for i in liste:
    print(i)
    count = count+i
    print(count)
    
    
# while loop
    
i = 0 
while(i<4):
    print(i)
    i=i+1
    
sinir = len (liste)
i = 0
count=0
while ( i< sinir):
    count = count+liste[i]
    i=i+1
print(i)

# %%
 liste = [1,2,35,458,34,564,-65,-63,-463,46,21]
 mini = 1000000
 for i in liste:
     if (i<mini):
         mini=i
     else:
         continue
print(mini)

    
    
    
    
    
    
    
    
    
    
    
    
    










