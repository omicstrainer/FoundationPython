#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:22:12 2020
@author: Abhishek Kumar
@Purpose: Training
"""
## Create a list of European countries
Europe = ["Russia", "Ukraine", "France", "Spain", "Sweden", "Norway", "Germany", "Finland", "Poland", "Italy", "Romania", "Belarus", "Kazakhstan", "Greece", "Bulgaria", "Iceland", "Hungary", "Portugal", "Austria", "Czechia", "Serbia", "Ireland", "Lithuania", "Latvia", "Croatia", "Bosnia-Herzegovina", "Slovakia", "Estonia", "Denmark", "Switzerland", "Netherlands", "Moldova", "Belgium", "Armenia", "Albania", "North-Macedonia", "Turkey", "Slovenia", "Montenegro", "Kosovo", "Cyprus", "Azerbaijan", "Luxembourg", "Georgia", "Andorra", "Malta", "Liechtenstein", "San_Marino", "Monaco", "Vatican_City", "United_Kingdom"]

## print list Europe
print(Europe)

## sort list Europe
Europe.sort()

## print list Europe

print(Europe)

## Measure the length of list Europe
length = len(Europe)

## print list Europe
print("Total length: ", length)

## print 1st element of the list Europe
print(Europe[0])
## print 11th element of the list Europe
print(Europe[10])

## print 21th element of the list Europe
print(Europe[20])

## print 31th element of the list Europe
print(Europe[30])

## print 41th element of the list Europe
print(Europe[40])

## print 51th element of the list Europe
print(Europe[50])

## print 1st element of the list Europe using negative value
print(Europe[-51])

## print -41 element of the list Europe using negative value
print(Europe[-41])

## print -31 element of the list Europe using negative value
print(Europe[-31])

## print -21 element of the list Europe using negative value
print(Europe[-21])

## print -11 element of the list Europe using negative value
print(Europe[-11])

## print -1 element of the list Europe using negative value
print(Europe[-1])

## create new list UK
UK = Europe[49]

## print the list UK
print(UK)

## Remove element United_Kingdom
Europe.remove("United_Kingdom")

## create new list Euro
Euro = Europe
## print the list Euro
print(Euro)
