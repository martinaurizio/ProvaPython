import numpy as np
def funzione_di_prova():
	print("Funzione")
def valuta(x, y):
	[X, Y]=np.meshgrid(x,y)
	Z = X**2 + Y**2
	return Z