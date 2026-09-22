#EJERCICIO 1
for i in range(100, 89, -1):
    print(i)

#EJERCICIO 2
numero = int(input("Ingresa un número: "))
for i in range(1, 11):
    resultado= i*numero
    print(resultado)

#EJERCICIO 3
palabra = input("Ingresa una palabra: ")
cantidad= 0
for letra in palabra:
    print(letra)
    cantidad += len(letra)
print("La palabra tiene: ", cantidad, "letras")



