'''
Operadores comunes:
==	Igualdad
!=	Distinto
'''
string1 = input("Registre un usuario: ")
string2 = input("Ingrese usuario: ")

if string1==string2:
    print("Acceso concedido")
else:
    print("Acceso denegado")


'''
formas pro de imprimir
'''
if string1==string2:
    print("\033[38;2;180;255;154mAcceso concedido. ✅\033[0m")  # Verde personalizado (#b4ff9a)
else:
    print("\033[91mAcceso denegado. ⛔\033[0m")  # Rojo