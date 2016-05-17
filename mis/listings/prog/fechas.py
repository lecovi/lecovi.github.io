>>> import datetime
>>> fecha_hoy = datetime.datetime.now()
>>> print(fecha_hoy)
2016-05-16 19:47:12.338413
>>> print(fecha_hoy.month)
5
>>> print(fecha_hoy.year)
2016
>>> print(fecha_hoy.day)
16
>>> print(fecha_hoy.second)
12
>>> print(fecha_hoy.minute)
47
>>> print(fecha_hoy.hour)
19
>>> print(fecha_hoy.day,fecha_hoy.month )
16 5
>>> print(fecha_hoy.weekday())
0
>>> fecha = datetime.datetime(1810,5,25)
>>> fecha
datetime.datetime(1810, 5, 25, 0, 0)
>>> fecha.weekday()
4
>>> dif = (fecha_hoy - fecha)
>>> dif.days
75232
>>> dif.seconds
71232
>>> dif.microseconds
338413
>>> fecha = datetime.datetime(1810)
>>> fecha = datetime.datetime(2016,5,15)
>>> fecha.weekday()
6
>>> 
