import numpy as np
import mate as mt
import matplotlib.pyplot as plt
matrice = np.zeros([10,20])
print(matrice)
x = np.linspace(0,1,3)
y = np.linspace(0,1,2)
print(x)
print(y)
#plt.plot(x,y,'-o')
#plt.title("Grafico seno")
#plt.show()
Z=mt.valuta(x,y)
print(Z)