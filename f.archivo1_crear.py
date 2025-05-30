'''
Modo	Descripción
"w"	Escribir (write). Crea o sobrescribe el archivo.
"r"	Leer (read). Error si no existe.
"a"	Agregar (append). Crea si no existe, pero no borra lo que había.
"x"	Crear (exclusive creation). Falla si ya existe.
"t"	Texto (text). Por defecto.
'''
archivo = open("xdatos.txt", 'w')       #1 abrimos o creamos e archivo en modo 'w'

archivo.write("Hola, probamos escribir en un archivo y despues leerlo. ")     #2 escribimos algo

archivo.close()     #3 cerramos el archivo
print ("archivo creado y escrito con exito...")     #avisamos al usuario