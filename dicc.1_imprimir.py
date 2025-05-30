'''
Imrpimiendo el diccionario de manera en que
haya sido creado
'''
persona = {"nombre": "Goat", 
           "edad": 20, 
           "dni": "40.999.990",
           "ciudad": "Corrientes"
           }


print("mostrando clave/valor")
for clave,valor in persona.items():
    print (clave,valor)
'''
en caso de que necesites mostrar solo el valor,
o solo la clave a continuacion te dejo los
diferentes bloques de codigo
'''
print("\nmostrando solo claves")
for iterando in persona:
    print(iterando)     #imprime solo las claves


print("\nmostrando solo valores")
for iterando in persona.values():   #imprime solo valores
    print(iterando)