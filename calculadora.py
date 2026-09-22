print("OPCIONES DE CALCULADORA")
print("1. SUMA")
print("2. RESTA")
print("3. MULTIPLICACIÓN")
print("4. DIVISIÓN")

operacion= int(input("Que operacion deseas realizar? Escribe un número del 1 al 4: "))
if operacion < 4 and operacion > 0:
    numero1= float(input("Dame un número: "))
    numero2= float(input("Dame otro número: "))
    if operacion== 1:
        print("Elegiste suma")
        resultado_suma= numero1 + numero2
        print("El resultado de la suma es: ", resultado_suma)

    if operacion== 2:
        print("Elegiste resta")
        resultado_resta = numero1 - numero2
        print("El resultado de la resta es: ", resultado_resta)

    if operacion== 3:
        print("Elegiste multiplicacion")
        resultado_multiplicacion = numero1 * numero2
        print("El resultado de la multiplicacion es: ", resultado_multiplicacion)

    if operacion== 4:
        print("Elegiste division")
        resultado_division = numero1 / numero2
        print("El resultado de la division es: ", resultado_division)
else:
    print("No elegiste un número entre el 1 y el 4, no se realizará ninguna operación")

