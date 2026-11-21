def merge_sort(lista, antes):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio], antes)
    derecha = merge_sort(lista[medio:], antes)
    resultado = []
    i = 0
    j = 0
    while i < len(izquierda) and j < len(derecha):
        if antes(derecha[j], izquierda[i]):
            resultado.append(derecha[j])
            j += 1
        else:
            resultado.append(izquierda[i])
            i += 1
    resultado += izquierda[i:]
    resultado += derecha[j:]
    return resultado


def quick_sort(lista, antes):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    pivote = lista[medio]
    resto = lista[:medio] + lista[medio + 1:]
    izquierda = [x for x in resto if antes(x, pivote)]
    derecha = [x for x in resto if not antes(x, pivote)]
    return quick_sort(izquierda, antes) + [pivote] + quick_sort(derecha, antes)


def insertion_sort(lista, antes):
    datos = lista[:]
    for i in range(1, len(datos)):
        actual = datos[i]
        j = i - 1
        while j >= 0 and antes(actual, datos[j]):
            datos[j + 1] = datos[j]
            j -= 1
        datos[j + 1] = actual
    return datos
