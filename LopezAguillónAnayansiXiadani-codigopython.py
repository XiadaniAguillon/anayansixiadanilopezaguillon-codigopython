#!/usr/bin/env python
# coding: utf-8

# # Ejercicio 1

# In[1]:


print(r' //\ ')
print(r'//__\ ')
print("||  ||")
print("||__||")


# # Ejercicio 2

# In[2]:


nom = input("Ingrese su nombre: ")
tel = input("Ingrese su telefono: ")
correo = input("Ingrese su correo: ")

print("\n¡BIENVENID@ " + nom + "!""\nTu numero de telefono es: " + tel + "\nTu correo es: " + correo)


# # Ejercicio 3

# In[26]:


r1 = float(input("Ingrese el valor de la resistencia 1: "))
r2 = float(input("Ingrese el valor de la resistencia 2: "))
print("El resultado es: ", (1/((1/r1)+(1/r2))))


# # Ejercicio 4

# In[23]:


matriz = []
for i in range(2):
    matriz.append([])
    for j in range(2):
        num = float(input("fila {}, columna {} : ".format(i,j)))
        matriz[i].append(num)
print("El resultado es:", (matriz[0][0]* matriz[1][1]) - (matriz[0][1]* matriz[1][0]))


# # Ejercicio 5

# In[8]:


import math
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingrese el valor de c: "))
x = (b**2)-(4*(a*c))
if x < 0:
    print("No tiene solucion")
else:
    x1 = (-b + math.sqrt(x)) / (2*a)
    x2 = (-b - math.sqrt(x)) / (2*a)
    print("EL VALOR DE X1 ES: ", x1)
    print("EL VALOR DE X2 ES: ", x2)


# # Ejercicio 6

# In[32]:


num = int(input("Ingrese un numero: "))
if num > 0:
    respuesta = "El numero es positivo"
elif num == 0:
    respuesta = "El numero es cero"
else:
    respuesta = "El numero es negativo"
print (respuesta)


# # Ejercicio 7

# In[32]:


nombre = (input("Ingrese su nombre: "))
edad = int(input("Ingrese su edad: "))
ingresos = int(input("Introduzca sus ingresos: "))
egresos = int(input("Introduzca sus egresos: "))
prestamo = int(input("Digite la cantidad del prestamo que desea hacer: "))
meses = int(input("A cuantos meses desea pagar?: "))
if(edad<18):
    print("Ops!, no puede solicitar un prestamo")
elif((prestamo/meses)<(ingresos-egresos)):
    print("SU PRESTAMO NO PUEDE PROCEDER :(")
else:
    print("¡FELICITACIONES!, PRESTAMO ACEPTADO")


# # Ejercicio 8

# In[7]:


fig = ' * '
altura = 5

for j in range (altura):
    print((fig) * (j + 1))

for i in range (len(fig)):
    for j in range (altura):
        print((fig) * altura)
        altura -= 1


# # Ejercicio 9

# In[2]:


print(input("Escribe una palabra: ")[::-1])


# # Ejercicio 10

# In[108]:


lista = [0, 1, 2, 3, 4, 5, 6]
lista.remove(3)
lista.remove(6)
print(lista)


# In[ ]:




