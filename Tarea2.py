#Ejercicio 1 
print("Nombre completo de una persona") 
N = str(input()) 
print(N.upper())
print(N.lower()) 
print(N.capitalize()) 

#Ejercicio 2
print('¿Cual es tu nombre?') 
Nombre = str(input()) 
n = len(Nombre) 
print(Nombre.upper(),' tiene',n," letras") 

#Ejercicio 3 
print("Introduce el numero completo")
num = str(input())
num = num[3:]
num = num[:-3]
print(num)

#Ejercicio 4 
F = str(input("Dame una Frase")) 
print("Dame una vocal") 
V = str(input())
print(F.replace(V,V.upper()))

#Ejercicio 5 
print("Escribe un correo sin el @ y el dominio") 
Co = str(input()) 
Co = Co.split('@')
print('Tu nuevo correo es: '+Co[0]+'@umich.mx')