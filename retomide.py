import time
import random
import matplotlib.pyplot as plt

# 1. Versión lenta (Fuerza bruta: revisa todas las parejas)
def suma_objetivo_lenta(lista, objetivo):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == objetivo:
                return True
    return False

# 2. Versión rápida (Usa un conjunto para recordar números vistos)
def suma_objetivo_rapida(lista, objetivo):
    vistos = set()
    for num in lista:
        necesario = objetivo - num
        if necesario in vistos:
            return True
        vistos.add(num)
    return False

# Tamaños de listas pedidos
tamanios = [1000, 2000, 4000, 8000]
objetivo_imposible = 9999999  # Forzamos el peor caso

tiempos_lentos = []
tiempos_rapidos = []

print("--- MIDIENDO TIEMPOS ---")
for n in tamanios:
    # Creamos una lista aleatoria de tamaño n
    lista = [random.randint(1, 10000) for _ in range(n)]

    # Medimos la versión lenta
    inicio = time.perf_counter()
    suma_objetivo_lenta(lista, objetivo_imposible)
    fin = time.perf_counter()
    tiempos_lentos.append(fin - inicio)

    # Medimos la versión rápida
    inicio = time.perf_counter()
    suma_objetivo_rapida(lista, objetivo_imposible)
    fin = time.perf_counter()
    tiempos_rapidos.append(fin - inicio)

    # Imprimimos en consola los resultados
    print(f"n = {n} -> Lenta: {tiempos_lentos[-1]:.5f}s | Rápida: {tiempos_rapidos[-1]:.5f}s")


# 4. EXPLICACIÓN CON BIG O (¿Por qué las curvas se separan?)

# • FUERZA BRUTA - O(n^2) [Curva Roja]:
#   Utiliza dos ciclos 'for' anidados. Por cada elemento, recorre prácticamente
#   toda la lista de nuevo. Su complejidad es cuadrática.
#   ¿Qué pasa con las curvas? Cuando duplicas el tamaño 'n' (por ejemplo, de
#   4,000 a 8,000), el tiempo de ejecución no se duplica, se cuadruplica.
#   Por eso la curva roja se dispara hacia arriba casi verticalmente.

# • VERSIÓN ÓPTIMA - O(n) [Curva Azul]:
#   Recorre la lista una sola vez y hace búsquedas en un conjunto (set) que toma
#   tiempo constante O(1). Su complejidad total es lineal.
#   ¿Qué pasa con las curvas? Al duplicar el tamaño 'n', el tiempo simplemente
#   se duplica de forma proporcional (2x), por lo que la curva azul se mantiene
#   prácticamente plana y muy baja en comparación.


# 3. Graficar los resultados
plt.plot(tamanios, tiempos_lentos, label="Fuerza Bruta O(n^2)", color="red", marker="o")
plt.plot(tamanios, tiempos_rapidos, label="Óptima O(n)", color="blue", marker="s")
plt.xlabel("Tamaño de la lista (n)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Reto: Mide y Grafica")
plt.legend()
plt.grid(True)
plt.show()
