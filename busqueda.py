def busqueda_binaria(lista, id):
    bajo = 0
    alto = len(lista) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio].id == id:
            return lista[medio]
        elif lista[medio].id < id:
            bajo = medio + 1
        else:
            alto = medio - 1
    return None


def busqueda_lineal_nombre(lista, texto):
    resultados = []
    texto = texto.lower()
    for producto in lista:
        if texto in producto.nombre.lower():
            resultados.append(producto)
    return resultados
