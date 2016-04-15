#!/usr/bin/env python3

# Informa si el interés es mayor al 30%, sino informa el importe total.


monto = int(input("Ingrese monto: "))

interes = float(input("Ingrese interés mensual: "))

if interes > 30:
    print("El interés ingresado es incorrecto")
else:    
    monto_final = monto * (1 + interes / 100)
    print("Monto final: %08.2f" % monto_final)
    print("FIN")

