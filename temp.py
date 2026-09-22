temperatura= float(input("Ingresa la temperatura: "))
frecuencia= int(input("Ingresa la frecuencia cardiaca: "))
saturacion= int(input("Ingresa la saturación de oxígeno: "))

if saturacion < 90 or frecuencia > 120:
    print("ROJO")
elif temperatura >= 39:
    print("AMARILLO")
else:
    print("VERDE")
