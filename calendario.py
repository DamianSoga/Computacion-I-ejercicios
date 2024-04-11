def diaspmes(nombre):
    nombre=nombre.lower()
    print(nombre)
    meses=['','enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembree','diciembre']
    con31=[1,3,5,7,8,11,12]
    con30=[4,6,10,9]
    con28=[2]
    d31=list(range(1,32))
    d30=list(range(1,31))
    d28=list(range(1,29))
    valor=meses.index(nombre)
    if valor < 1:
        return None
    else:
        if valor in con31:
            return d31
        elif valor==2:
            return d28
        else:
            return d30

def diaspmesv(lismeses):
    if type(lismeses)==list:
        l=[]
        for m in lismeses:
            n=diaspmes(m)
            l.append(n)
        return l
    else:
        return diaspmes(lismeses)



def mesbo(mes,dias):
    x=slice(0,7)
    return " ".join(list(map(str,dias[x])))

if __name__=='__main__':
    CAL=diaspmesv('febrero')
    d28=list(range(1,29))
    mesbo(CAL,d28)
    print(mesbo)




q
    




