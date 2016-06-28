import numpy as np
import matplotlib.pyplot as plt
import grafico as gf
matrice = np.zeros([10,20])
print(matrice)
x = np.linspace(0,2*np.pi,20)
y = np.linspace(0,1,20)
Z=np.zeros((20,20))
print(x)
print(y)

gf.superficie(x,y,Z)
