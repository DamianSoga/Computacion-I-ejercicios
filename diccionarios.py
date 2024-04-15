diccionario={
    'direccion':{
        'calle':'madero',
        'numero':'100',
        'colonia':'centro'
    },
    'telefonos':[{'telefono':'4433'},
                 {'telefono':'4444'}],
    'nombre':'carlos',
    'apellido':'garcia'
}


#print(diccionario['nombre'])
#print(diccionario['apellido'])
#print(diccionario['direccion'])
#print(diccionario['direccion']['numero'])

#for llave in diccionario.keys():
   #print(llave)
    #print(diccionario[llave])

#print(diccionario.values())

for llave in diccionario.keys():
    print(type(diccionario[llave]))
    if type(diccionario[llave])==dict:
        for ll2 in diccionario[llave]:
            print(diccionario[llave])

    elif type(diccionario[llave])==list:
        for elm in diccionario[llave]:
            print(elm)

    else:
        print(diccionario[llave])

l1=['nombre','edad']
l2=['raul','30']
x=dict(zip(l1,l2))
print(x)