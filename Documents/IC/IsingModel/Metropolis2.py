#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 10:12:43 2022

@author: thales
"""

import numpy as np 
import math


class Lattice2:
    def __init__(self, size=100):
        self.size = size
        self.array = np.random.randint(0,2,size**2).reshape((size,size))
        self.M = 0
        #for item in self.array:
         #   if item == 1:
               # self.M += 1
        #     else:
        #         self.M += -1
        # self.M = self.M/self.size
        
    def step(self,T=1,B=0, J = 1):
        a = np.random.randint(0,self.size)
        b = np.random.randint(0,self.size)
        coord = (a,b)
        delta_h= self.deltaH(coord, 1, J, B)
        if(delta_h<=0):
            self.change(coord)
            return delta_h
        elif(delta_h > 0):
            P = math.exp(-delta_h/T)
            x = np.random.uniform()
            if(x < P):
                self.change(coord)
                return delta_h
            else:        
                return 0
            
    def change(self,coord):
         self.array[coord] = (self.array[coord]+1) % 2
         # if self.array[coord] == 1:
         #     self.M += 1/self.size
         return 
    
    
    def deltaH(self, coord,mode,J,B):
        x, y = coord
        
        a = 1
        if mode == 1:
            a = -1
            
        a = (x +1)%self.size
        b = (y +1)%self.size
        c = (x -1)%self.size
        d = (y -1)%self.size
        
        delta_h = -(1/2)*J*a*aux(self.array[coord])*aux(self.array[x,b])  
                           -(1/2)*J*a*aux(self.array[coord])*aux(self.array[a,y])  
                            -(1/2)*J*a*aux(self.array[coord])*aux(self.array[x,d])  
                            -(1/2)*J*a*aux(self.array[coord])*aux(self.array[c,y]) - B*aux(self.array[coord])
        
        return delta_h
        
        
        
def aux(num):
    spin0 = 0
    if num == 1:
        spin0 = 1
    else:
        spin0 = -1    
        
    return spin0
                    