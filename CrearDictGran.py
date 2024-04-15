matricula=['01234567L','71476342J','63823376M','98376547F']
datos=['nombre','email','telefono','descuento']
p1=['Luis González','luisgonzalez@mail.com','656343576',12.5]
p2=['Macarena Ramírez','macarena@mail.com','692839321',8.0]
p3=['Juan José Martínez','juanjo@mail.com','664888233',5.2]
p4=['Carmen Sánchez','carmen@mail.com','667677855',15.7]
Z=[p1,p2,p3,p4]
x=[]
for i in range(4):
    a=dict(zip(datos,Z[i]))
    x.append(a)
grandi=dict(zip(matricula,x))
print(grandi)