saldo= 1000
print("Tu saldo es: ",saldo)
retirado_hoy= 0
monto= int(input("Ingresa el monto a retirar: "))

if monto % 50 != 0:
    print("MONTO NO VÁLIDO | saldo: ", saldo)
elif monto > saldo:
    print("SALDO INSUFICIENTE | saldo: ", saldo)
elif retirado_hoy + monto > 6000:
    print("LÍMITE DIARIO EXCEDIDO | saldo: ", saldo)
else:
    saldo=saldo-monto
    print("ENTREGADO | saldo: ", saldo)