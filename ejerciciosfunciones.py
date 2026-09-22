# -------------BLOQUE 1--------------------
#EJERCICIO 1

def nom():
    nombre = input("Escribe tu nombre: ")
    print(nombre)
nom()

#EJERCICIO 2

def positivo(numero):
    if numero > 0:
        print("El numero es positivo")
    else:
        print("El numero es negativo")

num= int(input("Escribe un número: "))
positivo(num)

#EJERCICIO 3

def numeros(num1, num2):
    if num1>num2:
        print("El primer numero es mayor que el segundo")
    if num2>num1:
        print("El segundo numero es mayor que el primero")
    if num1==num2:
        print("Los numeros son iguales")

numero1= int(input("Escribe un número: "))
numero2= int(input("Escribe otro número: "))
numeros(numero1, numero2)

#------------BLOQUE 2----------------
#Ejercicio 1

def cuadrado(num3):
    cuad= num3**2
    return cuad

numero3= int(input("Escribe un número: "))
resultado= cuadrado(numero3)
print("El cuadrado es: ",resultado)

#Ejercicio 2
def par(num4):
    if num4 % 2== 0:
        return "Es par"
    else:
        return "Es impar"

numero4= int(input("Escribe un número: "))
resultado2= par(numero4)
print(resultado2)

#Ejercicio 3
def mayor(num5, num6, num7):
    mayor= max(num5,num6,num7)
    return mayor

numero5= int(input("Escribe un número: "))
numero6= int(input("Escribe un número: "))
numero7= int(input("Escribe un número: "))
resultado3= mayor(numero5, numero6, numero7)
print("El mayor de los 3 es: ", resultado3)

#Ejercicio 4
def calculadora(num8, num9, operacion):
    if operacion== "+":
        return num8 + num9
    if operacion== "-":
        return num8 - num9
    if operacion== "*":
        return num8 * num9
    if operacion== "/":
        return num8 / num9
    else:
        return "Operacion no valida"

numero8= int(input("Escribe un número: "))
numero9= int(input("Escribe un número: "))
oper= input("Escribe la operación que deseas realizar:(+,-,*,/): ")
resultado4= calculadora(numero8,numero9,oper)
print("El resultado de la operacion es: ", resultado4)



