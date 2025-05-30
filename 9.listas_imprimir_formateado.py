'''
imprimiendo la lista formateada
significa que utilizaremos texto para mostrar
de manera ordenada y con mas detalle los
elementos de la lista, formato Pro😎
'''
lista = ['A','B','C','D','E','F','G','H','Y','J']

for iterando in range(len(lista)):  #range indica que va a iterar cierto numero de veces
    print (f"posicion {iterando} elemento {lista[iterando]}")

'''
separamos la linea del for en 3 secciones
la primera es la facil donde declaramos la variable iterando que usaremos
la segunda luego del "in" indicamos el rango o veces que vamos a iterar con range(10)
la tercera es obtener ese rango o valor numerico mediante la siguiente funcion len(lista)
la cual nos brinda la longitud de la lista.
---
por otro lado ahora descomponemos el print.
la f detras de las comillas "" indica que imprimiremos texto+valores
asi print(f"texto normal {valor1} texto normal {valor2}")

{iterando} es el valor actual de la variable del for
{lista[iterando]} el elemento de la lista en la posicion actual del for
'''