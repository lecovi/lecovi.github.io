# mostrar la sumatoria
# de los numeros de num

num = [10, 5, 6, 2, 8, 1]

def sumar(x, y):
    return (x + y)

g = reduce(sumar, num)
print(g)
