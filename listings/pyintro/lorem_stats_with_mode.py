ARCHIVO = 'lorem.txt'

print('Vamos a abrir el archivo "{ARCHIVO}"')

with open(ARCHIVO, mode="rt", encoding="utf-8") as lorem_file:
    contenido = lorem_file.read()

palabras = len(contenido.split())
print(f"Tiene {palabras} palabras")
