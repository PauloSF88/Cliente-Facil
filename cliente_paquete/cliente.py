class Cliente:
    # Atributo de clase para el nombre de la página
    nombre_pagina = "CompraFácil"

    def __init__(self, nombre, email, direccion, telefono):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre} - Página: {Cliente.nombre_pagina}"

    def actualizar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion

    def actualizar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono

    # Método para mostrar la información del cliente
    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Email: {self.email}, Dirección: {self.direccion}, Teléfono: {self.telefono}"

    # Método para cambiar el nombre de la página
    @classmethod
    def cambiar_nombre_pagina(cls, nuevo_nombre):
        cls.nombre_pagina = nuevo_nombre