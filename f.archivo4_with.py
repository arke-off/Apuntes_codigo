# Escribir en un archivo
with open("ejemplo.txt", "w") as archivo:
    archivo.write("Primera linea\n")
    archivo.write("Segunda linea\n")

# Leer el archivo
with open("ejemplo.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())  # .strip() elimina el salto de línea final