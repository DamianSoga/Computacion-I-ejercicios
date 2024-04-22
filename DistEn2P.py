import numpy as np
r=6378
p1=np.array([19.697324,101.205025])
p2=np.array([38.245463,115.468093])
dlt=p2[0]-p1[0]
dlog=p2[1]-p1[1]
a=np.square(np.sin(dlt/2))+(np.cos(p1[0])*np.cos(p2[0])*np.square(np.sin(dlog/2)))
print(a)
c=2*(np.arcsin(a))
d=r*c
print(d)