# -*- coding: utf-8 -*-
import numpy as np
matriz = np.array([[9,14,18,18,18,17,12,16],[17,18,16,7,18,8,15,12]])

arr1 = matriz[0,:]+5
#print(arr1)
arr2 = matriz[1,:]  ** 3
print(arr2)
#%%
class Prueba:
    def _init_ (self, P= 1):
        self.P = P
    
    def _repr_(self):
        return f"Prueba[P.{self.P}]"
    
    @property()
    def  P(self):
        return self._P
    
    @P.settera
    def P(self,val):
        if isintance(val,int) or isinstance(val,float) :
            if val!= 0 :
                self._P = val
            else:
                self.P  = val
        else:
            raise TypError("P debe ser int o float")
         #todo verififcar    
    def _add_(self,other):
        return(P=5* self.P **2 + 2*other.P ** 2)
    
    #%%


class Grafico :
    def _init_ (self,d1 = [0], d2= [0]):
        self.d1 = d1
        self.d2 = d2
        
    def ploteaGrafico(self):
        y1 = self.d1 ** 2 + self.d1 +1
        y2 = self.d2 + 3 
        plt.plot(t1,y1,'r')
        plt.plot(t2,y2,'r')
        plt.plot([1,1],[y1[-1],y2[0]],'r')
        plt.grid()
        
import numpy as np
import matplotlib.pyplot as plt

t1 = np.linspace(0,1,100)
t2 = np.linspace(1,4,100)

obj = Grafico(t1,t2)

obj.ploteaGrafico()
plt.show()
#%%
