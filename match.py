#===== CALCULADORA =====
#1. Sumar
#2. Restar
#3. Multiplicar
#4. Dividir
#5. Salir
#------------------------
#1. Pedir al usuario que elija una opción.
#2. Si la opción es del 1 al 4:
#3. Solicitar dos números.
#4. Realizar la operación correspondiente.
#5. Mostrar el resultado.
#6. Si elige 5, mostrar "Saliendo del programa".
#7. Si elige otra opción, mostrar "Opción no válida".

def numeros():
    num1 = float(input("Escribe un número: "))
    num2 = float(input("Escribe otro número: "))
    return num1, num2

print("")
print("CALCULADORA")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")

while True:
    opcion= int(input("Elige una operación (Escribe un número del 1 al 5): "))

    match opcion:
        case 1:
            print("Elegiste sumar")
            num1, num2 = numeros()
            resultado= num1+num2
            print("El resultado de la suma de ", num1, "+", num2, "es igual a ", resultado)
        case 2:
            print("Elegiste restar")
            num1, num2 = numeros()
            resultado = num1 - num2
            print("El resultado de la resta de ", num1, "-", num2, "es igual a ", resultado)
        case 3:
            print("Elegiste multiplicar")
            num1, num2 = numeros()
            resultado = num1 * num2
            print("El resultado de la multiplicacion de ", num1, "x", num2, "es igual a ", resultado)
        case 4:
            print("Elegiste dividir")
            num1, num2 = numeros()
            resultado = num1 / num2
            print("El resultado de la division de ", num1, "/", num2, "es igual a ", resultado)
        case 5:
            print("Saliendo del programa")
            break
        case _:
            print("Opcion no valida")

