#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:19:06 2022

@author: thales
"""
A,B,C = "a","b","c"
x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))

if x < y and x < z:
    A = x
    if y < z:
        B = y
        C = z
    else: 
        C = y
        B = z
        
if (x < y and x > z) or (x < y and x > z) :
    B = x
    if y < z:
        A = y
        C = z 
    else:
        C = y
        A = z
        
        
        
if x > y and x > z:
    C = x
    if y < z:
        A = y
        B= z
    else:
        B = z
        A = y
    
print(A,B,C)
