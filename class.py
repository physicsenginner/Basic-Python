#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 22:36:49 2020

@author: dogukan
"""

class Calisan:
    zam_orani=1.5
    counter=0
    def _init_(self,isim,soyisim,maas): # constructor
        self.isim=isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim+soyisim+"@asg.com"
        Calisan.counter = Calisan.counter+1
    def giveNameSurname (self):
        return self.isim+" "+self.soyisim
    def zam_yap(self):
        self.maas = self.maas + self.maas*self.zam_orani
        

#isci1 = Calisan ("ali","veli",100)
#print (isci1.giveNameSurname())
#print(isci1.maas)

# class variable

calisan1= Calisan("ali","veli",100)
print("ilk maas:",calisan1.maas)
calisan1.zam_yap()
print("yeni maas",calisan1.maas) 
calisan2 = Calisan ("ayse","hatice",2060)
calisan3 = Calisan ("ayse2","hatice2",2050)
calisan4 = Calisan ("ayse3","hatice3",2006)

# class exapmle
liste = [calisan1,calisan2,calisan3,calisan4]

maxi_maas = -1 
for i in liste:
    if (i.maas > maxi_maas):
        maxi_maas = i.maas
        index = i
print(maxi_maas)
print(index.giveNameSurname())













