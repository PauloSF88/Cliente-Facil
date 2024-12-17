class Cliente:
    def __init__(self, nombre, email, direccion, telefono):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}, Dirección: {self.direccion}, Teléfono: {self.telefono}"

    def actualizar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion
        print(f"La dirección de {self.nombre} ha sido actualizada a {self.direccion}")

    def actualizar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono
        print(f"El teléfono de {self.nombre} ha sido actualizado a {self.telefono}")