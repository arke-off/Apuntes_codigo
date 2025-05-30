'''
agregamos un elemento al final de la lista escribiendo
el nombre de la lista y luego la funcion .append
'''

lista = ['A','B','C','D','E','F','G','H','Y','J']

lista.append('x')   #añadimos la letra 'x' al final de la lista

print(lista)

'''
ahora agregaremos un elemento pero indicando el indice o
posicion donde queremos añadir (sin reemplazar)
'''

lista.insert(5, "z") # Inserta la "z" en el índice 5 pero sin reemplazar

print(lista)