import numpy as np
lista=[3,10,20]
array=np.array(lista)
print(array)
mx=[[1,2,3],[2,3,5],[3,3,0]]
mx1=np.array([[2,1,0],[2,2,1],[3,1,3]])
mx2=np.array(mx)
print(mx2.shape)
print(mx1*mx2)

lang=np.array([np.pi,np.pi/2,np.pi/4,np.pi/3])
print(np.rad2deg(lang))


angulos=np.array([3.1416,3.1416/2,3.1416/4,3.1416/3])
salida=[]
for a in angulos:
    salida.append(a*(180/3.1416))
print(salida)