>>> a = open("prueba.txt","w")
>>> a.write("uno dos tres")
12
>>> a.write("hola")
4
>>> a.close()
>>> a = open("prueba.txt","w")
>>> a.write("uno dos tres\n")
13
>>> a.write("hola")
4
>>> a.close()
>>> a = open("prueba.txt","a")
>>> a.write("otra cosa")
9
>>> a.close()
>>> a = open("prueba.txt","a")
>>> a.write("\notra\ncosa mas\n")
15
>>> a.close()
>>> u = open("toto", "r")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    u = open("toto", "r")
FileNotFoundError: [Errno 2] No such file or directory: 'toto'
>>> 
>>> 
>>> u = open("prueba.txt", "r")
>>> linea = u.readline()
>>> print(linea)
uno dos tres

>>> linea = u.readline()
>>> print(linea)
holaotra cosa

>>> linea = u.readline()
>>> print(linea)
otra

>>> u.close()
>>> u = open("prueba.txt", "r")
>>> lin = u.readlines()
>>> lin
['uno dos tres\n', 'holaotra cosa\n', 'otra\n', 'cosa mas\n']
>>> lin[0] = 'hola!\n'
>>> lin
['hola!\n', 'holaotra cosa\n', 'otra\n', 'cosa mas\n']
>>> otro = open("segundo.txt","w")
>>> otro.writelines(lin)
>>> otro.close()

