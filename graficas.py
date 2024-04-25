import matplotlib.pyplot as plt
import numpy as np


def grafica(x,y,color,titulo):
    n=y(x)
    plt.plot(x,n,'-',color=color,markersize=10,linewidth=2)
    plt.title(titulo)
    plt.xlabel('Eje de las x')
    plt.ylabel('Eje de las y')
    return plt


#a=grafica(np.linspace(-6,2),lambda x: 5-4*x-x**x,'red','$5-4x-x²$')
#a.show()
a2=grafica(np.linspace(-1,5),lambda x: 2*x**x-8*x-11,'blue','$2x^2-8x-11$')
a2.show()