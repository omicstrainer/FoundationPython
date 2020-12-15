#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 15/12 Tuesday 22:22:12 2020
Filename: list-example6.py
@author: Abhishek Kumar
"""
# Three elements - EU Country
Europe = ["Germany", "Austria", "UK"]
# Four elements - Vertebrates
Vertebrates = ["Cow", "Chichen", "Fugu", "Xenopus"]
# Combining two lists
Vert_Euro = Vertebrates + Europe
# Printing Vert_Euro
print(Vert_Euro)
#Sorting Vert_Euro
Vert_Euro.sort()
# Printing Sorted Vert_Euro
print(Vert_Euro)
#delete UK
del(Vert_Euro[2])
print(Vert_Euro)
# max Vert_Euro
Maxi = max(Vert_Euro)
print(Maxi)
# min Vert_Euro
Mini = min(Vert_Euro)
print(Mini)
