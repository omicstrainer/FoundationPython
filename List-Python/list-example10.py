#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on TUE 15/12/2020 23:22
File name: list-example10.py
@author: Abhishek Kumar
Purpose - Test1 
"""

#Create a list of your five friends 

Friend = ['A1', 'A2', 'A3', 'A4', 'A5']
print(Friend)

#Insert B3 before A3
Friend.insert(2, 'B3')
print(Friend)


#Append Friend using C1
Friend.append('C1')
print(Friend)

#delete A4
Friend.remove('A4')
print(Friend)

#Sort Friend
Friend.sort()
print(Friend)

#delete A4
Friend.remove('A4')
print(Friend)

#replace A3 by X3
x = Friend.index('x')
print(x)
Friend[x]='X3'
print(Friend)
