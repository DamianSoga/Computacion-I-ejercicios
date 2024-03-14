def sumar(num1,num2):
    return num1+num2
def imprime(a):
    print(a)

a = int(input())
b = int(input())
print('resultado',a+b)
resu = a+b
print('resultado',resu)
print(sumar(a,b))
res = sumar(a,b)
print(res)

def tamcad(a):
    return len(a)

def areacir(r):
    pi = 3.1416
    return (pi*(r)**2)

cad = str(input())
print(tamcad(cad))

rad = int(input())
print(areacir(rad))