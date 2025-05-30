'''funcion1
esta funcion obtiene la longitud de la lista e imprime ese valor
tambien podes guardar en una variable el valor
'''
lista = ['A','B','C','D','E','F','G','H','Y','J']

print("mostramos longitud de la cadena")
print(len(lista))   

#para guardar descomenta la linea de abajo
#variable=len(lista)


'''funcion2
Generando valores aleatorios, el siguiente codigo
genera 17 elementos, entre un rango de (1 y 35)
'''
import random as rand

lista=[rand.randint(1, 35) for i in range(17)]

print("mostramos lista aleatoria generada")
print (lista)