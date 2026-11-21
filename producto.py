class Producto:
    def __init__(self, id, nombre, precio, categoria, stock, calificacionPromedio):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
        self.calificacionPromedio = calificacionPromedio

    def __str__(self):
        return f"{self.id} | {self.nombre} | ${self.precio:.2f} | {self.categoria} | stock {self.stock} | {self.calificacionPromedio}"
