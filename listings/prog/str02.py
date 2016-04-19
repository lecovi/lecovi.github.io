Python 3.4.2 (default, Oct  8 2014, 13:14:40) 
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> s = "una frase cualquiera"
>>> s[0]
'u'
>>> s[1]
'n'
>>> s[2]
'a'
>>> s[]
SyntaxError: invalid syntax
>>> s[3]
' '
>>> s[4]
'f'
>>> s[0:3]
'una'
>>> s[4:9]
'frase'
>>> s[4:10]
'frase '
>>> 
>>> 
>>> 
>>> ================================ RESTART ================================
>>> s = "una frase cualquiera"
>>> s[:3]
'una'
>>> 
>>> 
>>> 
>>> 
>>> s[10:]
'cualquiera'
>>> 
>>> 
>>> 
>>> 
>>> len(s)
20
>>> 
>>> 
>>> 
>>> 
>>> 
