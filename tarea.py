#Ejercicio 1
numero1= int(input("Escribe un número entero: "))
numero2= int(input("Escribe un número entero: "))

suma= numero1 + numero2
print("La suma de los números es: ", suma)
resta= numero1 - numero2
print("La resta de los números es: ", resta)
multiplicacion= numero1 * numero2
print("La multiplicacion de los números es: ", multiplicacion)
division= numero1 / numero2
print("La division de los números es: ", division)

#Ejercicio 2
base= int(input("Escribe la base de un triangulo: "))
altura= int(input("Escribe la altura de un triangulo: "))
area= (base*altura)/2
print("El area del triangulo es: ", area)

#Ejercicio 3
edad= int(input("Escribe tu edad en años: "))
edad_meses= edad*12
print("Tienes ", edad_meses, "meses")
edad_dias= edad*365
print("Tienes ", edad_dias, "dias")

#Ejercicio 4
numero= int(input("Escribe un número: "))
exponente= int(input("Escribe un exponente: "))
resultado= numero**exponente
print("El resultado de la potencia es: ", resultado)

#Ejercicio 5
alumnos= int(input("Escribe la cantidad de alumnos: "))
computadoras= int(input("Escribe la cantidad de computadoras: "))
alumnos_por_computadora= alumnos//computadoras
alumnos_sobrantes= alumnos%computadoras
print("Los alumnos por computadora son: ", alumnos_por_computadora)
print("Los alumnos sobrantes son: ", alumnos_sobrantes)

#Ejercicio 6
numero3= int(input("Escribe un número: "))
residuo3= numero3%2
if residuo3 == 0:
    print("El número es par")
else:
    print("El número es impar")

#Ejercicio 7
precio= float(input("Escribe el precio de un producto: "))
iva= precio*0.16
precio_final= precio + iva
print("El precio final del producto con IVA es de: ", precio_final)

