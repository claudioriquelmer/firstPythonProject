
nombre = "Ana"
edad = 25

print(nombre + str(edad))  # ✅ "Ana25"

frutas = ["manzana", "plátano", "naranja"]
edades = [18, 25, 33]
mezcla = ["texto", 42, True]

print(frutas[0])  # manzana
print(frutas[2])  # naranja


# Operadores de control
edad = 15

if edad >= 18:
    print("Puedes entrar al evento")
elif edad >= 65:
    print("Usted es de la Tercera Edad")
else:
    print("Lo siento, eres menor de edad")


    frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print("Me gusta la", fruta)


#Operadores de Comparacion

    a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True: los valores son iguales
print(a is b)  # False: no son el mismo objeto en memoria


#Operadores logicos

edad = 16
tiene_permiso = True

if edad >= 18 and tiene_permiso:
    print("Acceso permitido")
else:
    print("Acceso denegado")

#Operadores de pertenencia

usuario = {
    "nombre": "Lucía",
    "edad": 30,
    "activo": True
}

if "edad" in usuario:
    print("Edad encontrada")

if 30 in usuario.values():
    print("Hay un usuario con 30 años")

#Control de flujo Match

dia = "miércoles"

match dia:
    case "lunes":
        print("Inicio de semana")
    case "miércoles":
        print("Mitad de semana")
    case "viernes":
        print("Fin de semana cerca")
    case _:
        print("Día normal")

edad = 16

match edad:
# Aquí capturamos el valor en la variable e
    case e if e >= 18:
        print(f"Tienes {e} años. Puedes ingresar.")
    case e if e < 18:
        print(f"Tienes {e} años. No puedes ingresar.")