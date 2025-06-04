from copy import deepcopy
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

class Courbe_Elliptique_2():
    
    def __init__(self,a,b,n):
        self.coef = (a,b)
        self.modulo = n
        
    def graphique(self):
        a,b = self.coef
        n = self.modulo
        
        X = [i for i in range(0,n)]
        Y = [i for i in range(0,n)]
        L = []
    
        for x in X :
            for y in Y :
                if y**2 % n == (x**3 + a*x + b)%n :
                    L.append((x,y))
                    
        for C in L:
            x,y = C
            plt.plot(x,y,'bo',markersize = 2)
            
        plt.grid()
        plt.show()

        
class Point_Courbe_Elliptique():
    
    def __init__(self,E,C):
        x,y = C
        n = E.modulo
        if x != 'infini':  
            if round((y**2 - (x**3 + E.coef[0]*x + E.coef[1]))%n,6) !=0.0 :
                print("Erreur de point")
        self.coo = C
        self.courbe = E        
        
    def copie(self):
        C = deepcopy(self.coo)
        E = self.courbe
        return Point_Courbe_Elliptique(E, C)
    
    def __add__(self,P2):
        E = self.courbe
        n = E.modulo
        if self.coo[0] == 'infini' and P2.coo[0] != 'infini' :
            return P2.copie()
        
        elif P2.coo[0] == 'infini' and self.coo[0] != 'infini' :
            return self.copie()
        
        elif self.coo[0] == 'infini' and P2.coo[0] == 'infini' :
            return self.copie()
        
        elif self.coo[0] != P2.coo[0] :
            inv_mod = pow((P2.coo[0] - self.coo[0]),-1,n)
            alpha = ((P2.coo[1] - self.coo[1])*inv_mod)%n
            
            x3 = int((alpha**2 - self.coo[0] - P2.coo[0]))%n
            y3 = int((alpha * (self.coo[0] - x3) - self.coo[1]))%n
            
            return Point_Courbe_Elliptique(E,(x3,y3))
        
        elif self.coo[0] == P2.coo[0] and self.coo[1] != P2.coo[1] :
            return Point_Courbe_Elliptique(E,('infini','infini'))
        
        elif self.coo == P2.coo and self.coo[1] != 0 :
            inv_mod = pow((2 * self.coo[1]),-1,n)
            alpha = ((3*self.coo[0]**2 + self.courbe.coef[0])*inv_mod) % n
            
            x3 = int((alpha**2 - self.coo[0] - P2.coo[0]))%n
            y3 = int((alpha * (self.coo[0] - x3) - self.coo[1]))%n
            
            return Point_Courbe_Elliptique(E,(x3, y3))
        
        elif self.coo == P2.coo and self.coo[1] == 0:
            return Point_Courbe_Elliptique(E,('infini','infini'))
        
    def __repr__(self):
        x,y = self.coo
        return f"({x},{y})"
    
    def __neg__(self):
        x,y = self.coo
        E=self.courbe
        n = E.modulo
        return Point_Courbe_Elliptique(E,(x,-y%n))
    
    def __sub__(self,P2):
        return self + (-P2)
    
    def __mul__(self,k):
        P = self.copie()
        E = self.courbe
        n = E.modulo
        k = k%n
        
        if k == 0 :
            return Point_Courbe_Elliptique(self.courbe, ('infini','infini'))
        
        elif k == 1 : 
            return self.copie()
            
        elif k%2 == 0:
            P = (P+P)*int(k/2)
            return P
        
        else :
            P = P + P*(k-1)
            return P
        
    def __rmul__(self,n):
        return self * n
    
    def __eq__(self,P2):
        return self.coo == P2.coo
    
    def appartient(self):
        E = self.courbe
        n = E.modulo
        x,y = self.coo
        return y**2%n == (x**3 + E.coef[0]*x + E.coef[1])%n
    
    
        
E = Courbe_Elliptique_2(-1, 1,527)



