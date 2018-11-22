ARCHIVO = 'lorem.txt'

print('Vamos a abrir el archivo "{ARCHIVO}"')

with open(ARCHIVO) as lorem_file:
    contenido = lorem_file.read()

palabras = len(contenido.split())
print(f"Tiene {palabras} palabras")
