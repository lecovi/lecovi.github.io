#!/usr/bin/env python3

def palindroma(s):                   
    largo = len(s)
    m = largo // 2
    if largo % 2 == 1:
        n = m 
    else:
        n = m - 1        
    return s[0:m] == s[len(s):n:-1]

def palindroma2(s):
    largo = len(s)
    m = n = largo // 2    
    if largo % 2 == 0:
        n = n - 1
        
    return s[0:m] == s[len(s):n:-1]

# si se ejecuta el programa
# hacer lo de abajo
# si se importa, no
if __name__ == '__main__': 
    print(palindroma("abcba"))
    print(palindroma("abba"))
    print(palindroma("1234321"))
    print(palindroma("abcdefg"))
    print(palindroma("ata ata"))

    print(palindroma2("abcba"))
    print(palindroma2("abba"))
    print(palindroma2("1234321"))
    print(palindroma2("abcdefg"))

