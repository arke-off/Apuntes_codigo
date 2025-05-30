def ingresar_string():
    while True:
        nombre = input("Ingrese su nombre: ").strip()
        if nombre:
            print("Bienvenido, señor", nombre)
            return nombre
        else:
            print("El campo no puede estar vacío.")

nuevoNombre = ingresar_string()
print(f"el nuevo nombre es : {nuevoNombre}")