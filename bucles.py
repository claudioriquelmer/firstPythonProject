#bucle for usando range()
print("BUCLE FOR CON RANGE()")
for numero in range(1, 6):
    print(numero)

#Recorrer listas
print("RECORRER LISTAS CON FOR")
animales = ["gato", "perro", "loro"]

for animal in animales:
    print("Tengo un", animal)

#Recorrer tuplas
print("RECORRER TUPLAS CON FOR")
pares = [("nombre", "Lucía"), ("edad", 28)]

for clave, valor in pares:
    print(f"{clave}: {valor}")

#Recorrer listas con enumerate()
print("RECORRER LISTAS CON ENUMARATE()")
nombres = ["Ana", "Luis", "Carlos"]

for i, nombre in enumerate(nombres):
    print(i, nombre)

#Bucle while
print("BUCLE WHILE")
contador = 1

while contador <= 5:
    print("Vuelta número", contador)
    contador += 1