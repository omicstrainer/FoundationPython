#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on TUE 15/12/2020 22:43
File name: list-example.py
@author: Abhishek Kumar
Purpose - Example Shallow copy - assignment of one list to another and then changes in one list will be seen in other also. 
"""
#Create list1
list1 = [11, 22, 33, 44, 55, 66, 77]
#print list1
print (list1)

#List assignment of  list1 to list2
list2 = list1

#print list2
print (list2)

list1[0]=110

#print list1
print (list1)

#print list2
print (list2)

#Removing 44 from list2
list2.pop(3)


#print list1
print (list1)

#print list2
print (list2)

#Reverse list1
list1.reverse()


#print list1
print (list1)

#print list2
print (list2)
