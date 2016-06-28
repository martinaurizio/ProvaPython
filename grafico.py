from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
def superficie(x,y,Z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    [X,Y]=np.meshgrid(x,y)
    ax.plot_surface(X,Y,Z)
    plt.show()
