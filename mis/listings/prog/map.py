# redondea los numeros de n
# con D decimales
num = [2.25,4.110,8.55,16.8144]

ndec = int(input("cantidad de decimales: "))

# version 1 - con for
j = num
i = 0
for n in num:
    j[i] = round(n,ndec)
    i = i + 1

print(j)

# version 2 - con enumerate y for
j = num
for i,n in enumerate(num):
    j[i] = round(n,ndec)    

print(j)

# version 3 - con map y lambda
k = list(map(lambda x:round(x,ndec), num))
print(k)
