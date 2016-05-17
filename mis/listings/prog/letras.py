#

frase = "una frase cualquiera"
letras = {}

for le in frase:
    if le in letras.keys():
        letras[le] = letras[le] + 1
    else:
        letras[le] = 1

print(letras)




