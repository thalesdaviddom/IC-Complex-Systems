# -*- coding: utf-8 -*-

import numpy as np
import  matplotlib.pyplot as plt
import math




#Classe criada para simular um modelo de Ising, essa classe conta com 
#um método delta_h, que calcula a variação na energia obtida ao se mudar 
#um spin, e também um méodo step, que implementa o algoritimo de metropolis 1 vez
class Lattice:
    def __init__(self,D=1,size=100):
        self.D = D
        self.size = size
        self.array = np.random.randint(0,2,size**self.D)
             
                            
                    
            

    def step(self, B=0, T=1, J = 1):
        coord = np.random.randint(0,self.size,self.D)
        delta_h = self.deltaH(coord, 1, J, B)
        if delta_h==None:
            print()
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
    
        
    def M2(self):
        M =0
        sitesize = int(self.size**(1/2))
        for i in range(0,self.size,sitesize):
            for j in range(0,self.size,sitesize):
                m = 0
                for a in range(i,i+sitesize):
                    for b in range(j, j + sitesize):
                        pointer = self.calculator(np.array([a,b]))
                        m += self.array[pointer]
                M += (1/sitesize**2)*abs(m)
        return M
                        
        
    def calculator(self,coord):
        pointer = 0
        dimension = self.array.size
        for i in range(self.D):
            dimension = dimension // self.size
            pointer += dimension*coord[i]
        return pointer  
        
    def inv_calculator(self, number):
        exp = self.D-1
        base = self.size**exp
        coord=[]
        while exp >= 0:
            coord += [number//base]
            number = number % base
            exp -= 1
            base = self.size**exp
        return np.array(coord)
                
        
    def change(self,coord):
        pointer = self.calculator(coord)
        self.array[pointer] = (self.array[pointer] + 1)%2
        return 
            
    
    def deltaH(self,coord, mode = 0, J = 1, B = 0):
        coord_list = [[]]
        numbers = list(coord)
        pointer0 = self.calculator(coord)
            
        
        if self.array[pointer0] == 1:
            spin0 = 1
        else:
            spin0 = -1
            
        if mode == 1:
            spin0 = spin0*(-1)
            
        for i in numbers:
            aux = []
            for j in coord_list:
                a1 = j[:]
                a2 = j[:]
                a3 = j[:]
                a1 += [(i-1)%self.size]
                a2 += [(i +1)%self.size]
                a3 += [i]
                aux += a1,a2, a3
            coord_list += aux
        
        aux = []
        for item in coord_list:
            if len(item) == self.D:
                aux += [item]
        coord_list=aux
                    
        delta_h = 0
            
        for item in coord_list:
            pointer1 = self.calculator(np.array(item))
            if self.array[pointer1] == 1:
                spin1 = 1
            else:
                spin1 = -1
            parcial = (-1/2)*J*spin0*spin1 - B*spin1       
            delta_h += parcial
        
        if delta_h==None:
            print()
            
        return delta_h
                
                
#produz uma simulação de metropolis iterando o método step um determinado número de vezes             
def Simulation(n = 1000, J = 1, B = 0, T = 1, D = 1, size = 200, mode = 0):
    
    lattice = Lattice(D, size)
    H = 0
    for item in range(lattice.array.size):
        coord = lattice.inv_calculator(item)
        H += lattice.deltaH(coord, 0, J, B)
    
    xlist = np.arange(0, n)
    ylist = []
    for item in xlist:
        H = H + lattice.step(B,T,J)
        ylist += [H]
    ylist = np.array(ylist)
    
    if mode == 0:
        plt.figure(num=0, dpi =120)
        plt.plot(xlist, ylist, label ="H(x)")
    else:
        return (xlist,ylist)
        
    return       
               
                           
            
                
if __name__ == '__main__':
                   
     Simulation() 
    