'''
Operadores comunes:
Operador	Significado
==	Igualdad
!=	Distinto
<	Menor alfabéticamente
>	Mayor alfabéticamente
<=	Menor o igual alfabéticamente
>=	Mayor o igual alfabéticamente

# Booleanos
and  # y
or   # o
not  # no (niega una condición)
'''

string1 = input("Registre un usuario: ")
string2 = input("Ingrese usuario: ")

if string1==string2:
    print("Acceso concedido")
else:
    print("Acceso denegado")