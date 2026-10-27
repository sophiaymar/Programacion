
import csv


def contenido_csv(nombre_archivo):
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)

        columnas = next(lector)
        print("Columnas:", columnas)

        filas = []
        for fila in lector:
            filas.append(fila)

    return columnas, filas


def ordenar_lista(columnas, filas, columna_orden):
    indice = columnas.index(columna_orden)

    filas.sort(key=lambda fila: fila[indice].lower())

    return filas


def escribir_csv(nombre_archivo, columnas, filas):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)

        escritor.writerow(columnas)
        escritor.writerows(filas)


if __name__ == "__main__":
    archivos = ["pacientes_mini - pacientes_mini.csv", "pacientes - pacientes.csv"]

    for nombre_archivo in archivos:
        columnas, filas = contenido_csv(nombre_archivo)

        filas = ordenar_lista(columnas, filas, "nombre")

        nuevo_archivo = nombre_archivo.replace(".csv", "_ordenados.csv")

        escribir_csv(nuevo_archivo, columnas, filas)

        print("Archivo creado:", nuevo_archivo)


