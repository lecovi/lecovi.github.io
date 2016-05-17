monto = int( input("ingrese monto: "))

# informar si el interes es mayor de 30%
interes = float(input("ingrese interes mensual: "))

if interes > 30:
    print("El interes ingresado es incorrecto")
else:    
    monto_final = monto * (1 + interes / 100)
    print("monto final: %08.2f" % monto_final)
    print("fin")

