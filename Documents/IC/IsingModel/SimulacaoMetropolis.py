#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 12:38:35 2022

@author: thales

Esse arquivo produz alguns gráficos de progressão de um modelo usando a class Lattice

"""
import Metropolis
import matplotlib.pyplot as plt
import numpy as np
def Main():
    
    #Primeiro criamos um gráfico simples para se ter noção do comportamento do modelo
    #unidimensional com tamamnho 200 e temperatura 1 (sem campo magnético)
    fig, ax1 = plt.subplots()
    xlist1,ylist1 = Metropolis.Simulation(1000,1, 0, 1,1, 200,1)
    ax1.plot(xlist1,ylist1, label = "H(x)")
    ax1.set_title("Ising Model base plot example ")
    ax1.set_xlabel("Number of steps" )
    ax1.set_ylabel("Energy level")
    ax1.legend()
    
    
    #vejamos como a magnetificação é alterada com o tempo 
    lattice = Metropolis.Lattice(1, 200)
    
    xlist = np.arange(0, 10000)
    ylist = []
    T = 1
    for item in xlist:
        lattice.step(0,1,1)
        ylist += [lattice.M]
    ylist = np.array(ylist)
    
    fig, axm = plt.subplots(figsize=(5,3))
    xlistM,ylistM = (xlist,ylist)
    axm.plot(xlistM,ylistM, label = "M")
    axm.set_title("M evolution with steps ")
    axm.set_xlabel("Number of steps",  )
    axm.set_ylabel("M")
    axm.legend()
    
    #Analisemos a variação do comportamento do modelo com a temperatura, para isso
    #comparamos a progressão de um modelo mantido à temperatura 1 e à temperatura 10
    fig, ax2 = plt.subplots()
    xlist2,ylist2 = Metropolis.Simulation(1000,1, 0, 1,1, 200,1)
    xlist3,ylist3 = Metropolis.Simulation(1000,1, 0, 10,1, 200,1)
    ax2.plot(xlist2,ylist2, label = "H(x) with T=1")
    ax2.plot(xlist3,ylist3, label = "H(x) with T = 10")
    ax2.set_title("Comparing Temperature")
    ax2.set_xlabel("Number of steps" )
    ax2.set_ylabel("Energy level")
    ax2.legend()
    
    #Um gráfico com disparidade maior de temperatura
    fig, ax3 = plt.subplots()
    xlist4,ylist4 = Metropolis.Simulation(10000,1, 0, 1,1, 200,1)
    xlist5,ylist5 = Metropolis.Simulation(10000,1, 0, 100,1, 200,1)
    ax3.plot(xlist4,ylist4, label = "H(x) with T=1")
    ax3.plot(xlist5,ylist5, label = "H(x) with T = 100")
    ax3.set_title("Base plot")
    ax3.set_xlabel("Comparing Temperature(T)" )
    ax3.set_ylabel("Energy level")
    ax3.legend()
    
    
    #podemos também variar a temperatura ao longo da simulação
    lattice = Metropolis.Lattice(1, 200)
    H = 0
    for item in range(lattice.array.size):
        coord = lattice.inv_calculator(item)
        H += lattice.deltaH(coord, 0, 1, 0)
    
    xlist = np.arange(0, 10000)
    tlist = np.arange(1,101,0.01)
    ylist = []
    T = 1
    for item in xlist:
        H = H + lattice.step(0,T,1)
        T += 0.1
        ylist += [H]
    ylist = np.array(ylist)
    
    fig, ax4 = plt.subplots(figsize=(5,3))
    ax5 = ax4.twinx()
    xlist6,ylist6 = (xlist,ylist)
    xlist7,ylist7 =(xlist,tlist)
    ax4.plot(xlist6,ylist6, label = "H(x)", color ="b")
    ax5.plot(xlist7,ylist7, label = "Temperature", color ="r")
    ax4.set_title("System where Temperaturure evolves with steps")
    ax4.set_xlabel("Number of steps",  )
    ax4.set_ylabel("Energy level")
    ax5.set_ylabel("Temperature")
    ax5.legend()
    ax4.legend()
    
    
    #Vamos agora comparar a progressão de dois sistemas de mesma temperatura 
    #e campo magnético diferentes
    fig, ax6 = plt.subplots()
    xlist9,ylist9 = Metropolis.Simulation(100,1, 10, 100,1, 200,1)
    xlist8,ylist8 = Metropolis.Simulation(100,1, 0, 100,1, 200,1)
    ax6.plot(xlist8,ylist8, label = "H(x) com T=100 e B =0")
    ax6.plot(xlist9,ylist9, label = "H(x) com T = 100 e B = 10")
    ax6.set_title("Comparing Systems with different magnetic fields (B)")
    ax6.set_xlabel("Number of steps" )
    ax6.set_ylabel("Energy level")
    ax6.legend()
    
    
    #um sistema que muda seu campo magnético com o tempo
    lattice = Metropolis.Lattice(1, 200)
    H = 0
    for item in range(lattice.array.size):
        coord = lattice.inv_calculator(item)
        H += lattice.deltaH(coord, 0, 1, 0)
    
    xlist = np.arange(0, 10000)
    blist = np.arange(0,20,0.002)
    ylist = []
    B = 0
    for item in xlist:
        H = H + lattice.step(B,100,1)
        B += 0.1
        ylist += [H]
    ylist = np.array(ylist)
    
    fig, ax7 = plt.subplots(figsize=(5,3))
    ax8 = ax7.twinx()
    xlist10,ylist10 = (xlist,ylist)
    xlist11,ylist11 =(xlist,blist)
    ax7.plot(xlist10,ylist10, label = "H(x)", color ="b")
    ax8.plot(xlist11,ylist11, label = "Magnetic Field (B)", color ="r")
    ax7.set_title("Magnetic field growing with time")
    ax7.set_xlabel("Number of steps",  )
    ax7.set_ylabel("Energy level")
    ax8.set_ylabel("Temperatura")
    ax8.legend()
    ax7.legend()

    #por último fazemos alguns gráficos em dimensôes maiores
    #d=2
    fig, ax9 = plt.subplots()
    xlist1,ylist1 = Metropolis.Simulation(1000,1, 0, 1,2, 200,1)
    ax9.plot(xlist1,ylist1, label = "H(x)")
    ax9.set_title("Ising Model with 2 dimensions")
    ax9.set_xlabel("Number of steps" )
    ax9.set_ylabel("Energy level")
    ax9.legend()
    
    #d=3
    # fig, ax10 = plt.subplots()
    # xlist1,ylist1 = Metropolis.Simulation(1000,1, 0, 1,3, 200,1)
    # ax10.plot(xlist1,ylist1, label = "H(x)")
    # ax10.set_title("Ising Model with 3 dimensions ")
    # ax10.set_xlabel("Number of steps" )
    # ax10.set_ylabel("Energy level")
    # ax10.legend()
    
    
    return 

if __name__ == "__main__":
    Main()