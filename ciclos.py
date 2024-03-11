#Caso que imprime en una sola linea
s = ''
p = 'hoy es lunes'
long = len(p) - 1
for i in range(long+1):
    s = s+p[long]
    long = long - 1
print(s)

#Se imprime  con espacios
for j in range(11,-1,-1):
    print(p[j],j)