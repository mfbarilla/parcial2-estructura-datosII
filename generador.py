import random
from producto import Producto

CATALOGO = {
    "Electrónica": (["Audífonos", "Teclado", "Mouse", "Monitor", "Cargador", "Bocina", "Cámara web", "Tablet", "Celular", "Smartwatch"], 40, 1500),
    "Ropa": (["Camisa", "Pantalón", "Chaqueta", "Vestido", "Zapatos", "Gorra", "Sudadera", "Falda", "Bufanda", "Calcetines"], 8, 150),
    "Libros": (["Novela", "Diccionario", "Atlas", "Libro de cocina", "Libro de historia", "Manual de Python", "Cuentos", "Biografía", "Libro de ciencias", "Poemario"], 5, 60),
    "Hogar": (["Lámpara", "Sartén", "Licuadora", "Almohada", "Cobija", "Silla", "Mesa", "Juego de tazas", "Cortinas", "Escoba"], 10, 400),
}

VARIANTES = ["Básico", "Plus", "Premium", "Mini", "Clásico", "Deluxe"]


def generar_productos(cantidad=50):
    ids = random.sample(range(1000, 10000), cantidad)
    productos = []
    for id in ids:
        categoria = random.choice(list(CATALOGO))
        nombres, minimo, maximo = CATALOGO[categoria]
        nombre = random.choice(nombres) + " " + random.choice(VARIANTES)
        precio = round(random.uniform(minimo, maximo), 2)
        stock = random.randint(0, 200)
        calificacion = round(random.uniform(1.0, 5.0), 1)
        productos.append(Producto(id, nombre, precio, categoria, stock, calificacion))
    return productos
