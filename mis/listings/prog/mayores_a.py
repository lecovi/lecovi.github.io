#!/usr/bin/env python3

# Dada una lista de números enteros y un número n generar otra lista 
# (y mostrarla) con todos los números de la lista que sean mayores a n.
#
# Ej.  
# numeros = [10, 20, 30, 40, 50, 60] 
# n = 45
#
# ---> nueva = [50, 60]

def mayores_a(lista, n):
    nueva_lista = list()  # nueva_lista = [] 
    for numero in lista:
        if numero > n:
            # agrego numero a la lista.
            nueva_lista.append(numero)

    return nueva_lista
    
numeros = [10, 20, 30, 40, 50, 60] 
n = 45

print(mayores_a(numeros, n))


numeros = [210, 120, 30, 440, 5, 60] 
n = 45

print(mayores_a(numeros, n))


# Si la lista es ordenada...

def mayores_a2(lista, n):
    nueva_lista = list()  # nueva_lista = [] 
    for numero in lista:
        if numero > n:
            indice = lista.index(numero)
            break
    return lista[indice:]
    
numeros = [10, 20, 30, 40, 50, 60] 
n = 45

print(mayores_a2(numeros, n))

numeros = [210, 120, 30, 440, 5, 60] 
n = 45

print(mayores_a2(numeros, n))


def mayores_a3(lista, n, ordenada):
    if ordenada:
        return mayores_a2(lista, n)
    else:
        return mayores_a(lista, n)


numeros = [10, 20, 30, 40, 50, 60] 
n = 45

print(mayores_a3(numeros, n, True))

numeros = [210, 120, 30, 440, 5, 60] 
n = 45

print(mayores_a3(numeros, n, False))
print(mayores_a3(numeros, n, True))

def mayores_a4(lista, n, ordenada=True):
    if ordenada:
        return mayores_a2(lista, n)
    else:
        return mayores_a(lista, n)


numeros = [10, 20, 30, 40, 50, 60] 
n = 45

print(mayores_a4(numeros, n))

numeros = [210, 120, 30, 440, 5, 60] 
n = 45

print(mayores_a4(numeros, n, False))
print(mayores_a4(numeros, n))


print(mayores_a4(ordenada=False, n=n, lista=numeros))
