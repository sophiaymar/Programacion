print("1. Saludar")
print("2. Despedir")
print("3. Salir")

opcion= input("Escribe la operacion a realizar: "). lower()

match opcion:
    case "saludar":
        print("HOLA")
    case "despedir":
        print("BYE")
    case "salir":
        print("CERRANDO PROGRAMA")
    case _:
        print("Error, tecleaste una tecla incorrecta")
