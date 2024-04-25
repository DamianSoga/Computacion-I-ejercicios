import matplotlib.pyplot as plt
import numpy as np
from math import e
#rango
x=np.linspace(-1,5)
x2=np.linspace(-6,2)
x3=np.linspace(-1,5)
#funcion
fx=2*x**2-8*x-11
fx2=5-4*x2-x2**2
fx3=x3*(1/(2.7182**2)*x3)
#graficar
plt.plot(x,fx,'-',color='red',markersize=10,linewidth=2)
plt.plot(x2,fx2,'-',color='blue',markersize=10,linewidth=2)
plt.plot(x3,fx3,'-',color='yellow',markersize=10,linewidth=2)
plt.title('$2x^2+3x+8$')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.show()