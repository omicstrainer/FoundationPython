#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on TUE 16/12/2020 00:11
File name: list-example11.py
@author: Abhishek Kumar
Purpose - Test2
"""
# Create list of six odd numbers 
Odd = ['1', '3', '5', '7', '9', '11']
print (Odd)
Length_Odd=len(Odd)
print (Length_Odd)
# Create list of six even numbers
Even = ['2', '4', '6', '8', '10', '12']
print (Even)
Length_Even=len(Even)
print (Length_Even)
# These two list to form 3rd one 
Numbers = Odd+Even

# Print Numbers
print (Numbers)
# Length computation of Numbers
Length_Numbers=len(Numbers)
#Print Length of Numbers
print (Length_Numbers)

#Add 19, 21, 29 at the start of the "Numbers"
Num = ['19','21','29']+Numbers 


# Print Num
print (Num)
# Length computation of Num
Length_Num=len(Num)
# Print Length of Num
print (Length_Num)
