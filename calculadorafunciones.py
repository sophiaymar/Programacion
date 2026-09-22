import math


def menu():
    print("")
    print("1. SUMA")
    print("2. RESTA")
    print("3. MULTIPLICACION")
    print("4. DIVISION")
    print("5. POTENCIA")
    print("6. RAIZ CUADRADA")
    print("7. SALIR")

def suma(num1,num2):
    return num1 + num2
def resta(num1,num2):
    return num1 - num2
def multiplicacion(num1,num2):
    return num1 * num2
def division(num1,num2):
    return num1 / num2
def potencia(num1,num2):
    return num1 ** num2
def raiz(num1):
    if num1<=0:
        print("El número no tiene raíz real")
        return False
    else:
        return math.sqrt(num1)

opcion= 0
while opcion != 7:
    menu()
    opcion= int(input("Escribe la operacion que deseas realizar: "))
    if opcion==1:
        num1 = float(input("Escribe un número: "))
        num2 = float(input("Escribe otro número: "))
        resultado= suma(num1,num2)
        print(num1, "+", num2, "=", resultado)
    if opcion==2:
        num1 = float(input("Escribe un número: "))
        num2 = float(input("Escribe otro número: "))
        resultado=resta(num1,num2)
        print(num1, "-", num2, "=", resultado)
    if opcion==3:
        num1 = float(input("Escribe un número: "))
        num2 = float(input("Escribe otro número: "))
        resultado=multiplicacion(num1,num2)
        print(num1, "x",num2, "=" ,resultado)
    if opcion==4:
        num1 = float(input("Escribe un número: "))
        num2 = float(input("Escribe otro número: "))
        resultado=division(num1,num2)
        print(num1, "/",num2, "=" ,resultado)
    if opcion==5:
        num1 = float(input("Escribe un número: "))
        num2 = float(input("Escribe otro número: "))
        resultado=potencia(num1,num2)
        print(num1, "**",num2, "=" ,resultado)
    if opcion==6:
        num1 = float(input("Escribe un número: "))
        resultado=raiz(num1)
        print(num1, "raiz =" ,resultado)
    if opcion==7:
        print("SALIR")
        break
else:
    print("OPCION INVALIDA")




