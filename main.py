import numpy as np
import matplotlib.pyplot as plt
import grafico as gf
matrice = np.zeros([10,20])
print(matrice)
x = np.linspace(0,2*np.pi,20)
y = np.cos(x)
print(x)
print(y)
plt.plot(x,y,'-o')
plt.title("Grafico seno")
plt.show()
gf.funzione_prova()
