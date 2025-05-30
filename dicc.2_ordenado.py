from operator import itemgetter

productos = {
    "manzanas": 10,
    "bananas": 5,
    "peras": 8,
    "duraznos": 12
}

print("Ordenamos por clave alfabeticamente")
for clave in sorted(productos.keys()): # sorted() ordena las claves alfabeticamente
    print(clave,productos[clave])


print("\nOrdenamos por valor ascendente")
for clave, valor in sorted(productos.items(), key=itemgetter(1)): #itemgetter ordena por valor ascendente
    print(clave,valor)