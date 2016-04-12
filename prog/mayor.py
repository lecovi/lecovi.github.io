#!/usr/bin/env python3

# De dos numeros que se ingresan, informar el mayor.

num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")

if num1 > num2:
    print("El primero es mayor")
elif num2 > num1:
    print("El segundo es mayor")
else:
    print("Son iguales!")
