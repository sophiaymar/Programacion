# Ejemplo 1: Función para saludar
def saludar(nombre):
    print("Hola,", nombre)

# Ejemplo 2: Función para sumar dos números
def sumar(a, b):
    resultado = a + b
    return resultado

# Ejemplo 3: Función para verificar si un número es par
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


# Ejemplo 1
saludar("Sophia")

# Ejemplo 2
suma = sumar(5, 3)
print("La suma es:", suma)

# Ejemplo 3
numero = 4
if es_par(numero):
    print(numero, "es un número par")
else:
    print(numero, "es un número impar")

