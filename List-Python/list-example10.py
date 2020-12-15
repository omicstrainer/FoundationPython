#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on TUE 15/12/2020 23:22
File name: list-example10.py
@author: Abhishek Kumar
Purpose - Test1 
"""

#Create a list of your five Friends 

Friend = ['A1', 'A2', 'A3', 'A4', 'A5']
print(Friend)

#Insert B3 before A3
Friend.insert(2, 'B3')
#Print Friend
print(Friend)

#Append Friend using C1
Friend.append('C1')
#Print Friend
print(Friend)

#delete A4
Friend.remove('A4')
#Print Friend
print(Friend)

#Sort Friend
Friend.sort()
#Print Friend
print(Friend)

#replace A3 by D3
i=Friend.index('A3')
Friend[i]='D3'
#Print Friend
print(Friend)
