import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt

def calcular_fc():
    try:
        edad = int(entry_edad.get())
        peso = float(entry_peso.get())
        actividad = combo_actividad.get()


        intensidades = {
            "Bajo": 0.5,
            "Medio": 0.7,
            "Alto": 0.85
        }

        intensidad = intensidades[actividad]

        # Cálculos
        fc_max = 220 - edad
        fc_objetivo = fc_max * intensidad

        # Clasificación
        if fc_objetivo < 60:
            estado = "Bajo"
            color = "blue"
        elif 60 <= fc_objetivo <= 100:
            estado = "Normal"
            color = "green"
        else:
            estado = "Alto"
            color = "red"
            ventana.bell()  # 🔊 alerta

        # Mostrar resultado
        resultado.set(f"FC Objetivo: {fc_objetivo:.2f} bpm\nEstado: {estado}")
        label_resultado.config(fg=color)

        # Graficar
        graficar(fc_max, fc_objetivo)

    except:
        messagebox.showerror("Error", "Datos inválidos")


def graficar(fc_max, fc_objetivo):
    valores = [fc_max, fc_objetivo]
    etiquetas = ["FC Máxima", "FC Objetivo"]

    plt.figure()
    plt.bar(etiquetas, valores)
    plt.title("Frecuencia Cardíaca")
    plt.xlabel("Tipo")
    plt.ylabel("BPM")
    plt.show()


# Ventana
ventana = tk.Tk()
ventana.title("Monitor de Frecuencia Cardíaca")
ventana.geometry("400x350")

# Título
tk.Label(ventana, text="Monitor Cardíaco", font=("Arial", 16)).pack(pady=10)

# Inputs
tk.Label(ventana, text="Edad:").pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

tk.Label(ventana, text="Peso (kg):").pack()
entry_peso = tk.Entry(ventana)
entry_peso.pack()

tk.Label(ventana, text="Nivel de actividad:").pack()
combo_actividad = ttk.Combobox(ventana, values=["Bajo", "Medio", "Alto"])
combo_actividad.pack()

# Botón
tk.Button(ventana, text="Calcular", command=calcular_fc).pack(pady=10)

# Resultado
resultado = tk.StringVar()
label_resultado = tk.Label(ventana, textvariable=resultado, font=("Arial", 12))
label_resultado.pack(pady=10)

ventana.mainloop()