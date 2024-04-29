import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('datam.csv')
df.plot(x='Poblacion',
        y='Municipio',
        kind='line')

plt.show
