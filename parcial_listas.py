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

def calcularPrecio(categoria,duracion):
    if categoria== "IT":
        categoria=5000
        if duracion >20:
            categoria=5000-(5000*0.10)
    elif categoria== "diseno":
        categoria=2500
        if duracion >20:
            categoria=2500-(2500*0.05)
    elif categoria == "negocios":
        categoria=7500
        if duracion >20:
            categoria=7500-(7500*0.15)
    return categoria*duracion

for i in range(len(lista)):
    lista[i][0] = random.randint(100,200)
    lista[i][1] = random.choice(["IT","diseno","negocios"])
    lista[i][3] = random.randint(10,50)
    lista[i][2] = calcularPrecio(lista[i][1],lista[i][3])

for iterando in range(10):
    print(f"{lista[iterando]}")