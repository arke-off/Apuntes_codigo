import random
lista = [["ID_alumno","categoria","precioFinal","duracion"],
         ["ID_alumno","categoria","precioFinal","duracion"],
         ["ID_alumno","categoria","precioFinal","duracion"],
         ["ID_alumno","categoria","precioFinal","duracion"],
         ["ID_alumno","categoria","precioFinal","duracion"],
         ["ID_alumno","categoria","precioFinal","duracion"],
         ["ID_alumno","categoria","precioFinal","duracion"],
         ["ID_alumno","categoria","precioFinal","duracion"],
         ["ID_alumno","categoria","precioFinal","duracion"],
         ["ID_alumno","categoria","precioFinal","duracion"],]

def calcularPrecio(categoria):
    if categoria== "IT":
        categoria=5000
    elif categoria== "diseno":
        categoria=2500
    elif categoria == "negocios":
        categoria=7500
    return categoria

for i in range(len(lista)):
    lista[i][0] = random.randint(100,200)
    lista[i][1] = random.choice(["IT","diseno","negocios"])
    lista[i][3] = random.randint(10,50)
    lista[i][2] = calcularPrecio(lista[i][1])

for iterando in range(10):
    print(f"{lista[iterando]}\n")   