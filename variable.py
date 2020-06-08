# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
# %%
#variable(degisken)

#variable
#function
#object

var1=10#integer
var2=15

gun = "pazartesi"  #string

var3=10.0 # double (float)

# 5var=10 kodu hatasyntax hatası verir

# %%
#string

s="bugun gunlerden pazartesi"

variable_type = type (s) #str = string

print (s)

var1 = "ankara"
var2= "ist"
var3= var1+var2
print (var3)

var4= "100"
var5 ="200"
var6=var4+var5
print(var6)

uzunluk = len(var6)
 #var6[3] 
 
 
 
 
 
 
 
 # %% numbers
 
 # int double
integer_deneme = -50
 
 # double = float = ondalıklı sayı
 
float_deneme = -30.7

# %% built in functions

str1= "deneme"

float1 = 10.6

#int (float1) 10 a tamamlar
#round (float1) 11 e tamamlar
str2 ="1005"

# output = type (parametre(input))

# %%  user defined functions

var1 = 10
var2 = 100
output = (((var1+var2)*50)/100)*var1/var2



var3 = 105
var4 = 1006
output2 = (((var3+var4)*50)/100)*var3/var4
# fonksiyon parametresi = input
def benim_ilk_func(a,b):
    """ bu benim ilk denemem
        parametre:
        
        return:
    """
    output = (((a+b)*50)/100)*a/b
    return output

            
sonuc = benim_ilk_func(var1,var2)

#var1 = a , var2 = b

def deneme2 ():
    print ("bu benim ikinci denemem")

# %% default ve flexible functions
    
# cemberin cevre uzunlugu = 2*pi*r
def cember_cevresi_hesapla(r,pi=3.14):
    
    """
    cember cevresi hesapla
    input (parametre): r, pi
    output =cemberin cevresi
    """
    
    output = 2*pi*r
    return output    
# pi yi default  olarak tanımladık.
    
# %% flexible 
    
def hesapla(boy,kilo,*args):
    print((args))
    output = (boy+kilo)*args[0]
    return output

#def hesapla (boy,kilo,yaş):
#    output = (boy+kilo)*yaş
#    return output

def ssap(x, y=2):
    c=2
    for i in range (y):
        c = c+x
    return c
 

# %% QUİZ

# int variable yas
# string name isim
#function
#  function print(typr(),len,float())
# *args soyisim
#default parameter ayakkabi numarasi

yas = 10
name = "ali"
soyisim = "veli"
def function1 (yas,name,*args,ayakkabi_numarasi=35):
    print("Cocugun ismi:",name,"yasi:",yas,"ayak numarasi:",ayakkabi_numarasi)
    print(type(name))
    print(float(yas))
    output = args[0]*yas
    return output
sonuc=function1 (yas,name,soyisim)
print ("args[0]*yas:",sonuc)
    
# %% 
#lambda function

def hesapla (x):
    output = x*x
    return output

sonuc = hesapla (3) 

sonuc2 = lambda x : x*x

print (sonuc2(3))











































 
 
 
 
 
 
 
 
 