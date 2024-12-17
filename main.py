from cliente_paquete.cliente import Cliente

def main():
    # Crear una instancia de Cliente
    cliente1 = Cliente(nombre="Juan Pérez", email="juan.perez@example.com", direccion="Calle Falsa 123", telefono="123456789")

    # Mostrar información del cliente
    print(cliente1)

    # Actualizar dirección del cliente
    cliente1.actualizar_direccion("Avenida Siempre Viva 742")
    
    # Actualizar teléfono del cliente
    cliente1.actualizar_telefono("987654321")

    # Mostrar información actualizada del cliente
    print(cliente1)

if __name__ == "__main__":
    main()