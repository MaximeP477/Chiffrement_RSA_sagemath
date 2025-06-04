from copy import deepcopy
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
import time

class Courbe_Elliptique():
    
    def __init__(self,a,b):
        self.coef = (a,b)
        
    def generation_point(self,x):
        y = sqrt(x*(x-1)*(x+1))
        return (x,y),(x,-y)
    
    def graphique(self):
        a,b = self.coef
        f1 = lambda x : sqrt(x**3 + a*x + b)
        f2 = lambda x : -sqrt(x**3 + a*x + b) 
        X1,X2 = intervalle(f1, -3, 3, self)
        
        Y11 = np.array([f1(x) for x in X1])
        Y21= np.array([f2(x) for x in X1])
        Y12= np.array([f1(x) for x in X2])
        Y22= np.array([f2(x) for x in X2])

        plt.plot(X1,Y11,'b')
        plt.plot(X1,Y21,'b')
        plt.plot(X2,Y12,'b')
        plt.plot(X2,Y22,'b')
        plt.grid()
        plt.axvline(x=0,color = 'k', linewidth=1)
        plt.axhline(y=0,color = 'k', linewidth=1)
        
        plt.xlim(-3,3)
        plt.ylim(-3,3)
        
        plt.show()
        
        
class Point_Courbe_Elliptique():
    
    def __init__(self,E,C):
        x,y = C
        '''if x != 'infini':  
            while round(y**2 - x**3 - E.coef[0]*x - E.coef[1],2) !=0.0 :
                x = input("Donner un point valide")
                y = E.generation_point(x)[0]
                signe = input("Quel signe pour y")
                if signe == '-':
                    y = -y'''
        self.coo = C
        self.courbe = E        
        
    def copie(self):
        C = deepcopy(self.coo)
        E = self.courbe
        return Point_Courbe_Elliptique(E, C)
    
    def __add__(self,P2):
        E = self.courbe
        if self.coo[0] == 'infini' and P2.coo[0] != 'infini' :
            return P2.copie()
        
        elif P2.coo[0] == 'infini' and self.coo[0] != 'infini' :
            return self.copie()
        
        elif self.coo[0] == 'infini' and P2.coo[0] == 'infini' :
            return self.copie()
        
        elif self.coo[0] != P2.coo[0] :
            alpha = (P2.coo[1] - self.coo[1]) / (P2.coo[0] - self.coo[0])
            
            x3 = alpha**2 - self.coo[0] - P2.coo[0]
            y3 = alpha * (self.coo[0] - x3) - self.coo[1]
            
            return Point_Courbe_Elliptique(E,(x3,y3))
        
        elif self.coo[0] == P2.coo[0] and self.coo[1] != P2.coo[1] :
            return Point_Courbe_Elliptique(E,('infini','infini'))
        
        elif self.coo == P2.coo and self.coo[1] != 0 :
            alpha = (3*self.coo[0]**2 + self.courbe.coef[0]) / (2 * self.coo[1])
            
            x3 = alpha**2 - self.coo[0] - P2.coo[0]
            y3 = alpha * (self.coo[0] - x3) - self.coo[1]
            
            return Point_Courbe_Elliptique(E,(x3, y3))
        
        elif self.coo == P2.coo and self.coo[1] == 0:
            return Point_Courbe_Elliptique(E,('infini','infini'))
        
    def __repr__(self):
        x,y = self.coo
        return f"({x},{y})"
    
    def __neg__(self):
        x,y = self.coo
        E=self.courbe
        return Point_Courbe_Elliptique(E,(x,-y))
    
    def __sub__(self,P2):
        return self + (-P2)
    
    def __mul__(self,n):
        P = self.copie()
        if n < 0 :
            return (-P)*(-n)
        elif n == 0 :
            return Point_Courbe_Elliptique(self.courbe, ('infini','infini'))
        elif n == 1 : 
            return self.copie()
        elif n%2 == 0:
            P = (P+P)*int(n/2)
            return P
        else :
            P = P + P*(n-1)
            return P
        
    def __rmul__(self,n):
        return self * n
    
    def __eq__(self,P2):
        return self.coo == P2.coo
    
    def mul_nul(self,n):
        P = self.copie()
        Q = Point_Courbe_Elliptique(self.courbe, ('infini','infini'))
        if n < 0 :
            return (-P)*(-n)
        elif n == 0 :
            return Point_Courbe_Elliptique(self.courbe, ('infini','infini'))
        elif n == 1 : 
            return self.copie()
        else :
            while n > 0 :
                Q = Q + P
                n = n-1
            return Q
    
    
        
E = Courbe_Elliptique(-1, 0)
C1,C2 = E.generation_point(-0.8)
C3,C4 = E.generation_point(-0.5)
P1,P2 = Point_Courbe_Elliptique(E,C1), Point_Courbe_Elliptique(E,C3)
P3 = P1+P2

E2 = Courbe_Elliptique(-1, 1)


def intervalle(f,a,b,E):
    X = np.linspace(a,b,200000)
    pas = (b-a)/(200000-1)
    Y = []
    Y1 = []
    for x in X :
        try : 
            f(x)
        except :
            pass
        else :
            if len(Y) == 0:
                Y.append(x)
            elif x <= Y[-1] + pas + 0.0001 and  x >= Y[-1] + pas - 0.0001 :
                Y.append(x)
            else :
                Y1.append(x)
    return np.array(Y), np.array(Y1)
            

for a in [-2,-1,0,1]:
    for b in [-1,0,1,2]:
        E = Courbe_Elliptique(a, b)
        E.graphique()
