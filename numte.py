import re
nv = int(input('¿Cuantos numeros de telefono vas a dar? '))
cad = ''
s = ''
RE = r'\+\d{2}'
if nv < 10:
    for i in range(nv):
        cod = input('codigo del pais: ')
        num = input('numero de telefono; ')
        if len(num) == 10:
            cad = cad+cod+num+'|'
        else:
            continue #break
    cad = cad.replace('+52','')
    cad = cad.split('|')
    long = len(cad)-1
    for i in range(long+1):
        s = s+cad[long]+'|'
        long = long - 1
    print(s)