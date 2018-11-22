ARCHIVO = 'lorem.txt'

print('Vamos a abrir el archivo "{ARCHIVO}"')

lorem_file = open(ARCHIVO)
contenido = lorem_file.read()
lorem_file.close()
palabras = len(contenido.split())
print(f"Tiene {palabras} palabras")
