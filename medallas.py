import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
sports={
    'medalla':[100,15,123,90,87,83],
    'periodo':[2010,2011,2012,2013,2014,2015]
}
df=pd.DataFrame(sports)
df.plot(x='periodo',
        y='medalla',
        kind='line')

plt.show
