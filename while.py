lista=[5,27,30,1,3,2]
sal=[]
i=lista.pop()
while i>0:
    if i<10:
        sal.append(i)
        print(i)
        i=lista.pop()
    else:
        if len(lista):
            i=lista.pop()
        else:
            i=0
