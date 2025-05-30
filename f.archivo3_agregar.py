'''
Modo
"a"	Agregar (append). Crea si no existe, pero no borra lo que había.
para comprobar si se agrego el nuevo texto lo siguiente es
intenta leerlo ejecutando -> f.archivo2_leer.py
'''
archivo = open("xdatos.txt", 'a')       #1 abrimos el archivo en modo 'w'

archivo.write("Este texto fue agregado al final del archivo")     #2 agregamos texto algo

archivo.close()
print ("texto agregado con exito...")