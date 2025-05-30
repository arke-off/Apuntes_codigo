'''
Modo
"r"	Leer (read). Error si no existe.
'''
archivo = open("xdatos.txt", 'r')       #1 abrimos el archivo en modo 'r' asegurate que coincida con el nombre del archivo que creaste

contenido = archivo.read()      #2 leemos lo escrito (con el archivo abierto)

print (contenido)       #3 imprimimos lo leido

archivo.close()     #4 cerramos el archivo