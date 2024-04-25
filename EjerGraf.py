import matplotlib.pyplot as plt
import numpy as np


def graficasub(plt,x,y,color,titulo):
    n=y(x)
    plt.plot(x,n,'-',color=color,markersize=10,linewidth=2)
    plt.set_title(titulo)
    return plt


def grafica(x,y,color,titulo):
    n=y(x)
    plt.plot(x,n,'-',color=color,markersize=10,linewidth=2)
    plt.title(titulo)
    plt.xlabel('Eje de las x')
    plt.ylabel('Eje de las y')
    return plt

fig = plt.figure()
fig.subplots_adjust(top=0.8)
ax1 = fig.add_subplot(211)



a=graficasub(ax1,np.linspace(-1,10,100),lambda x: 2*x**+3*x+8,'red','$2x^2+3x+8$')

a.show()