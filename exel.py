import pandas as pd

df=pd.read_excel('material\\exelpausar.xls')
#la cordenada esta dada primero por el eje de los numero (siempre dadas por -2) 
#y despues las letras (dadas por +1)
celda=df.iloc[10,4]
celda2=df.iloc[10,5]
print(type(celda))