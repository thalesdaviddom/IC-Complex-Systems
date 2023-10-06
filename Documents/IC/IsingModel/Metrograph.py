#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 17:21:11 2022

@author: thales
"""
import matplotlib.pyplot as plt 
import numpy as np
import Metropolis as Metro
import math

def TakeAPic(lattice, path):
    Array = np.resize(lattice.array,(lattice.size,lattice.size))
    plt.pcolor(Array)
    plt.savefig(path)
    plt.show()
    return



def main():
    lattice = Metro.Lattice(2,100)
    TakeAPic(lattice, "fig")
    for i in range(1000000):
        lattice.step(0,1,100)
        if i%10000 ==0:
            TakeAPic(lattice,"fig")
    TakeAPic(lattice, "fig")
    
    
    a=100
    b=100000
    y = []
    for i in range(a):
        lattice = Metro.Lattice(2,100)
        for j in range (b):
            lattice.step(0,a+1,100)
        y +=[lattice.M2()]
    y = np.array(y)
    x = np.array(range(a))
    
    fig, ax1 = plt.subplots()
    ax1.plot(x,y,label = "m(T) x T")
    ax1.set_title("Magnetization versus temperature ")
    ax1.set_xlabel("Temperature(T)" )
    ax1.set_ylabel("Magnetization(m)")
    ax1.legend()
           

    return 

if __name__== "__main__":
    main()