'''
este fragmento de codigo calcula el promedio
de los elementos de una lista mediante un for
realiza mas pasos pero comprendiendo los valores
'''

lista = [8,6,8,10]
suma = 0
cantidad_elementos = len(lista)

for numero in lista:
    suma += numero
promedio = suma / cantidad_elementos

print (promedio)