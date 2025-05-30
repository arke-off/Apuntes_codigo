📦 1. Operadores útiles
# Comparaciones
==	# Igualdad
!=	# Distinto
<	# Menor alfabéticamente
>	# Mayor alfabéticamente
<=	# Menor o igual alfabéticamente
>=	# Mayor o igual alfabéticamente

# Booleanos
and  # y
or   # o
not  # no (niega una condición)


🔄 2. Bucles
# Bucle for
for i in range(5):
    print(i)

# Bucle while
contador = 0
while contador < 5:
    print(contador)
    contador += 1


🔁 3. Control de flujo
# Continuar al siguiente ciclo
continue

# Romper el bucle
break


📚 4. Funciones personalizadas
def saludar(nombre):
    print(f"Hola, {nombre}. ¿Té o Python hoy?")

saludar("Arke")


🧪 5. Manejo de errores elegante
try:
    numero = int(input("Ingrese un número: "))
except ValueError:
    print("Eso no fue muy numérico, señor.")


📂 6. Importación de módulos
import math

print(math.sqrt(16))  # Raíz cuadrada


🕹️Y uno infaltable:
import random

print(random.choice(["té", "café", "mate"]))