'''
a esta altura del cuatrimestre
ya no puedo explicar esto perdon
---
en caso que necesites imprimir una matriz diferente
reemplaza (tu_listaColumna) y (tu_listaFila) por (lista_columna) o (lista_fila)
'''

lista_fila = [0,1,2,3,4,5,6,7,8,9]
lista_columna = ['A','B','C','D','E','F','G','H','Y','J']

for iterandoColumna in (lista_columna): #Columna
    print(iterandoColumna,end=' ')
    for iterandoFila in (lista_fila):   #Fila
        print(iterandoFila,end=' ')
    print("\n")
