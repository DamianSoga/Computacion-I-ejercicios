def jun(pref,nom):
    for prefijo in pref:
        for nombre in nom:
            return '{}{}'.format(prefijo,nombre)

def jun2(pref,nom):
    salida=[]
    for prefijo in pref:
        for nombre in nom:
            salida.append('{}{}'.format(prefijo,nombre))
    return salida


lista = ['Carlos','Juan','Mario']
prefijos = ['1989-','2081-','1850-']
lista2 = prefijos.extend(lista)
num= [5,30,100,1,21,10]
m = sorted(num)

print(jun(prefijos,lista))
lp = (jun2(prefijos,lista))

print(prefijos.extend(lista))
print(lp.count('1989-Carlos'))
print(m)