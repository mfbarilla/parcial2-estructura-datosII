import random
import time
from generador import generar_productos
from ordenamiento import merge_sort, quick_sort, insertion_sort
from busqueda import busqueda_binaria, busqueda_lineal_nombre

REPETICIONES = 1000

random.seed(42)
productos = generar_productos(50)

por_precio = lambda a, b: a.precio < b.precio
por_calificacion = lambda a, b: a.calificacionPromedio > b.calificacionPromedio
numeros = lambda a, b: a < b
por_id = lambda a, b: a.id < b.id


def medir(funcion):
    mejor = None
    for _ in range(5):
        inicio = time.perf_counter()
        for _ in range(REPETICIONES):
            funcion()
        fin = time.perf_counter()
        tiempo = (fin - inicio) / REPETICIONES * 1000000
        if mejor is None or tiempo < mejor:
            mejor = tiempo
    return mejor


algoritmos = [("Merge Sort", merge_sort), ("Quick Sort", quick_sort), ("Insertion Sort", insertion_sort)]
precios = [p.precio for p in productos]

print("Productos generados:")
for p in productos:
    print(p)

print()
print("Tiempos de ordenamiento (microsegundos, promedio de", REPETICIONES, "repeticiones, mejor de 5 rondas)")
print(f"{'Algoritmo':<16}{'Precio':>10}{'Calificación':>15}{'Números':>10}")
for nombre, algoritmo in algoritmos:
    t1 = medir(lambda: algoritmo(productos, por_precio))
    t2 = medir(lambda: algoritmo(productos, por_calificacion))
    t3 = medir(lambda: algoritmo(precios, numeros))
    print(f"{nombre:<16}{t1:>10.1f}{t2:>15.1f}{t3:>10.1f}")

ordenados = merge_sort(productos, por_id)
ids = [p.id for p in ordenados]
existentes = random.sample(ids, 10)
inexistentes = random.sample([n for n in range(1000, 10000) if n not in ids], 10)

t_existentes = medir(lambda: [busqueda_binaria(ordenados, i) for i in existentes])
t_inexistentes = medir(lambda: [busqueda_binaria(ordenados, i) for i in inexistentes])

print()
print("Búsqueda binaria por id (microsegundos por 10 búsquedas)")
print("Ids que existen:", f"{t_existentes:.1f}")
print("Ids que no existen:", f"{t_inexistentes:.1f}")

con_resultado = [random.choice(p.nombre.split()) for p in random.sample(productos, 10)]
sin_resultado = ["xyz", "tractor", "helicóptero", "refrigerador", "sombrero", "zzz", "bicicleta", "guitarra", "pizza", "robot"]

t_con = medir(lambda: [busqueda_lineal_nombre(productos, t) for t in con_resultado])
t_sin = medir(lambda: [busqueda_lineal_nombre(productos, t) for t in sin_resultado])

print()
print("Búsqueda lineal por nombre (microsegundos por 10 búsquedas)")
print("Con resultados:", f"{t_con:.1f}")
print("Sin resultados:", f"{t_sin:.1f}")
print("Textos con resultados:", con_resultado)
