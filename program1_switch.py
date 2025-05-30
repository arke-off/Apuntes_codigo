'''
Creacion de un programa
'''
opcion = input("Elija una opción: ")

match opcion:
    case "1":
        print("Opción 1 seleccionada.")
    case "2":
        print("Opción 2 seleccionada.")
    case _:
        print("Opción inválida.")
