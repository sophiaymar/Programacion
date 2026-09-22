def menu():
    print("")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar saldo")
    print("4. Salir")

def consultar_saldo(saldo):
    print("")
    print("Tu saldo es: ", saldo)

def depositar_dinero(cantidad, saldo):
    return saldo + cantidad

def retirar_dinero(retirar, saldo):
    if saldo >= retirar:
        return saldo - retirar
    else:
        print("FONDOS INSUFICIENTES")
        return saldo

opcion= 0
saldo= 1000

while opcion != 4:
    menu()
    opcion= int(input("Elige una opcion con número: "))
    if opcion == 1:
        print("Consultar saldo")
        consultar_saldo(saldo)
    elif opcion==2:
        print("Depositar dinero")
        cantidad= int(input("Ingresa una cantidad a depositar: "))
        saldo= depositar_dinero(cantidad, saldo)
        print("Tu saldo es: ", saldo)
    elif opcion==3:
        print("Retirar saldo")
        retirar= int(input("Ingresa una cantidad a retirar: "))
        saldo= retirar_dinero(retirar, saldo)
        print("Tu saldo es: ", saldo)
    elif opcion==4:
        print("Gracias por usar el cajero")
    else:
        print("Selecciona otra opción")
        break




