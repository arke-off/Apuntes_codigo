
def ingresaEntero():
    while True:
        entrada = input("Ingrese un número: ")
        if entrada.isdigit():
            numero = int(entrada)
            print("Número válido:", numero)
            return  numero
        else:
            print("Eso no parece un número entero, señor.")


variable=ingresaEntero()
print(f"el valor de la variable es : {variable}")