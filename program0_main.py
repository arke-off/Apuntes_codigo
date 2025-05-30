def mostrar_saludo():
    print("╔══════════════════════════════╗")
    print("║ Bienvenido!                  ║")
    print("║ Programa de opciones v1.0 🧭 ║")
    print("╚══════════════════════════════╝\n")

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Saludar al mayordomo")
    print("2. Consultar la hora del té")
    print("3. Salir\n")

def ejecutar_opcion(opcion):
    match opcion:
        case "1":
            print("¡Un placer, señor! ¿Desea que le prepare Python con torta frita?")
        case "2":
            print("La hora del té es a las 17:00. Jamás debe adelantarse.")
        case "3":
            print("Hasta luego, señor Arke. Que la RAM lo acompañe.")
        case _:
            print("Disculpe, esa opción no está en el menú.")

def programa_principal():
    mostrar_saludo()
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ")
        ejecutar_opcion(opcion)
        if opcion == "3":
            break

# Ejecutar el programa
programa_principal()
