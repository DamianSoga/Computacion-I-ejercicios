import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('/home/alumno/Downloads/datam.csv',header=0,delimiter=',',quotechar='"')

a=df['Municipio']
b=df['Poblacion']

mun=a.to_list()
pob=b.to_list()

totalpob=sum(list(map(lambda x: int(x.replace(',','')),pob)))
aporc=[int(i.replace(',',''))/totalpob for i in b[0:10]]

plt.pie(aporc,labels=a[0:10])

#fig, ax = plt.subplots()
#ax.bar(x = a[0:10], height = b[0:10])

plt.show()