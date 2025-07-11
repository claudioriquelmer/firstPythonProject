#Vamos a construir una función desde cero que salude a cualquier persona por su nombre.
def saludar(nombre):
    mensaje = f"¡Hola, {nombre}! Bienvenido/a a Python"
    return mensaje

print(saludar("Lucía"))

#Funcion que reciba un precio y un porcentaje de descuento y devuelva el precio
def descuento(precio, porcentaje):
    return precio - (precio * porcentaje / 100)

print(descuento(100, 15))

#La palabra return indica que una funcion devuelve un valor al lugar donde fue llamada
def saludar(nombre):
    return f"Hola, {nombre}"

mensaje = saludar("Valentina")
print(mensaje)

#Funcion que recibe un radio y devuelva el area del circulo(A = π * r²)
import math

def area_circulo(radio):
    return math.pi * radio ** 2

print(area_circulo(5))

#Funcion que reciba un precio y un iva con valor por defecto 19.La funcion debe devolver el precio final con IVA incluido
def calcular_total(precio, iva=19):
    valor_iva = precio * iva / 100
    precio_total = precio + valor_iva
    return precio, valor_iva, precio_total

# Probamos con el IVA por defecto (19%)
base, iva, total = calcular_total(100)
print(f"Precio base: CLP {base}")
print(f"IVA (19%): CLP {iva}")
print(f"Total a pagar: CLP {total}")

# Probamos con un IVA personalizado (21%)
base, iva, total = calcular_total(100, iva=21)
print(f"\nPrecio base: € {base} ")
print(f"IVA (21%): € {iva}")
print(f"Total a pagar: € {total}")

#Funcion con args y kwargs
def formar_equipo(nombre, *miembros, **datos):
    print(f"Equipo: {nombre}")
    print("Miembros:")
    for m in miembros:
        print(f" - {m}")
    for clave, valor in datos.items():
        print(f"{clave.capitalize()}: {valor}")

formar_equipo(
    "Tigres del Sur",
    "Ana", "Luis", "Carlos",
    color="rojo",
    ciudad="Sucre"
)

#Funciones lambda
# Función tradicional
def cuadrado(n):
    return n * n

# Mismo resultado con lambda
cuadrado = lambda n: n * n

print(cuadrado(4))

#Se usan para pasar una funcion como argumento
productos = [("manzana", 3), ("banana", 2), ("naranja", 4)]

ordenado = sorted(productos, key=lambda x: x[1])
print(ordenado)

#Convertir una funcion tradicional en una lambda
def sumar_iva(precio):
    return precio * 1.19

#Version lambda
sumar_iva = lambda precio: precio * 1.19
print(sumar_iva(100))  # 119.0

#Funcion decoradora
def funcion_decoradora(funcion_como_parametro):
    def funcion_envolvedora():
        print("Ejecutando función...")
        funcion_como_parametro()
        print("Función ejecutada.")
    return funcion_envolvedora

@funcion_decoradora
def saludar():
    print("¡Hola, mundo!")

saludar()

#Decoradores con argumentos
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Llamando a {func.__name__} con args={args}, kwargs={kwargs}")
        resultado = func(*args, **kwargs)
        print("Llamada finalizada")
        return resultado
    return wrapper

@log
def sumar(a, b):
    return a + b

sumar(2, 3)