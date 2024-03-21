def mesbo(mes,dias):
    x=slice(0,7)
    return " ".join(list(map(str,dias[x])))


con31=[1,3,5,7,8,11,12]
con30=[4,6,10,9]
d31=list(range(1,32))
d30=list(range(1,31))
d28=list(range(1,29))
meses=['','enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembree','diciembre']

for mes in range(1,13):
    if con30.count(mes):
       print('{}-{}'.format(meses[mes],d30)) 
    elif con31.count(mes):
        print('{}-{}'.format(meses[mes],d31))
    else:
        print('{}-{}'.format(meses[mes],d28))

print(mesbo(mes,d28))