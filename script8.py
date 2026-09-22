# Simulador de Electrocardiograma (ECG)

#Importar librería Tkinter para crear ventanas gráficas
import tkinter as tk
#Importar componentes de Tkinter
from tkinter import ttk
#Importar librería para hacer gráficas
import matplotlib.pyplot as plt
import math


# Función para generar y mostrar la señal de ECG
def mostrar_ecg(fc):
    # Tiempo de 0 a 4 segundos
    #Almacenar valores del tiempo
    tiempo = []
    #Almacenar valores del ECG
    señal = []

    # Número de puntos de la gráfica
    n = 400

    #Ciclo para generar la señal
    for i in range(n):
        #Generar tiempo en intervalos de 0.1 segundos
        t = i * 0.01
        #Guardar tiempo en la lista
        tiempo.append(t)

        # Señal base usando una onda senoidal
        y = 0.02 * math.sin(2 * math.pi * 5 * t)

        # Crear picos QRS repetidos según la frecuencia cardíaca
        periodo = 60 / fc   # segundos por latido
        #Calcular fase para repetir el patrón
        fase = t % periodo

        # Pico R (el más alto del ECG)
        if fase < 0.03:
            y = 1.2
        elif fase < 0.06:
            y = -0.3
        elif fase < 0.10:
            y = 0.1

        #Guardar valor de la señal
        señal.append(y)

    # Graficar
    plt.figure(figsize=(10, 4))
    plt.plot(tiempo, señal, linewidth=2)
    plt.title("Simulación de Electrocardiograma (ECG)")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Voltaje (mV)")
    plt.grid(True)
    plt.ylim(-0.5, 1.5)
    plt.show()


# Función que se ejecuta al presionar el botón
def calcular():
    # str
    nombre = entrada_nombre.get()

    # int
    edad = int(entrada_edad.get())

    # float
    peso = float(entrada_peso.get())

    # Obtener la variable que se guardara en actividad de Combobox
    actividad = combo.get()

    # Calcular frecuencia cardíaca máxima
    fc = 220 - edad

    # Mensaje según actividad
    if actividad == "Bajo":
        mensaje = "Haz ejercicio ligero."
    elif actividad == "Medio":
        mensaje = "Mantén ejercicio moderado."
    else:
        mensaje = "Tu condición física es muy buena."

    # Mostrar resultados en la ventana
    resultado.config(
        text="Hola " + nombre + "\n"
             + "Frecuencia cardíaca máxima: " + str(fc) + " bpm\n"
             + "Peso: " + str(peso) + " kg\n"
             + mensaje
    )

    # Mostrar gráfica ECG
    mostrar_ecg(fc)


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Simulador de ECG")
ventana.geometry("450x400")

# Título
tk.Label(
    ventana,
    text="Simulador de Electrocardiograma",
    font=("Arial", 16, "bold")
).pack(pady=10)

# Nombre (str)
tk.Label(ventana, text="Nombre").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

# Edad (int)
tk.Label(ventana, text="Edad").pack()
entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

# Peso (float)
tk.Label(ventana, text="Peso (kg)").pack()
entrada_peso = tk.Entry(ventana)
entrada_peso.pack()

# Nivel de actividad (str)
tk.Label(ventana, text="Nivel de actividad").pack()
combo = ttk.Combobox(
    ventana,
    values=["Bajo", "Medio", "Alto"],
    state="readonly"
)
combo.pack()

# Botón
tk.Button(
    ventana,
    text="Calcular y Mostrar ECG",
    command=calcular
).pack(pady=10)

# Área de resultados
resultado = tk.Label(
    ventana,
    text="",
    fg="blue",
    font=("Arial", 11),
    justify="left"
)
resultado.pack(pady=10)

# Mantener la ventana abierta
ventana.mainloop()
