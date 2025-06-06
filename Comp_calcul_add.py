import numpy as np
import matplotlib.pyplot as plt
import time

def calcul_addition_nul(x,d):
    a=0
    for i in range(d) : 
        a = a+x
    return a

def calcul_addition(x,d):
    a = 0
    if d == 0 :
        return 1
    if d == 1 : 
        return x
    while d > 0:
        if d%2 == 0 :
            x = x+x
            d = d//2
        else :
            a = a+x
            d = d-1
    return a

def comparaison_calcul_puissance():
        X = 10
        D = np.linspace(10,10**7,10,dtype=int)
        print(D)
        delta1 = []
        delta2 = []
        for d in D :
            t0 = time.time()
            calcul_addition(X, d)
            delta1.append(time.time() - t0)
        
            t1 = time.time()
            calcul_addition_nul(X, d)
            delta2.append(time.time() - t1)
        delta1 = np.array(delta1)
        delta2 = np.array(delta2)
        plt.title('Temps de calcul en fonction de la puissance')
        plt.plot(D,delta1,'r--',label = 'Calcul puissance rapide (exponentiation)')
        plt.plot(D,delta2,'b--', label = 'Calcul puissance lent')
        plt.ylabel('Temps (en sec)')
        plt.xlabel(f'Puissance de {X}')
        plt.legend()
        plt.show()
        return None
    
comparaison_calcul_puissance()