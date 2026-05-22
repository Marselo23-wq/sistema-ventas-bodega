def mostrar_menu():
    print("\n--- SISTEMA DE VENTAS ---")
    print("1. Registrar venta")
    print("2. Mostrar productos")
    print("3. Salir")


def mostrar_productos(productos):
    print("\n--- PRODUCTOS DISPONIBLES ---")

    for codigo in productos:
        nombre = productos[codigo][0]
        precio = productos[codigo][1]

        print(codigo, "-", nombre, "- S/.", precio)


def registrar_venta(productos):
    total_venta = 0
    continuar = "S"

    while continuar == "S":
        mostrar_productos(productos)

        codigo_producto = int(input("\nIngrese el código del producto: "))

        if codigo_producto in productos:

            cantidad = int(input("Ingrese la cantidad: "))

            nombre_producto = productos[codigo_producto][0]
            precio_producto = productos[codigo_producto][1]

            subtotal = cantidad * precio_producto

            total_venta += subtotal

            print("\nProducto:", nombre_producto)
            print("Subtotal: S/.", round(subtotal, 2))

        else:
            print("El producto no existe")

        continuar = input("\n¿Desea agregar otro producto? (S/N): ").upper()

    print("\nTotal a pagar: S/.", round(total_venta, 2))


def main():

    productos = {
        1: ["Coca Cola", 3.50],
        2: ["Pan", 0.50],
        3: ["Leche", 4.00],
        4: ["Galletas", 2.00]
    }

    opcion = 0

    while opcion != 3:

        mostrar_menu()

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            registrar_venta(productos)

        elif opcion == 2:
            mostrar_productos(productos)

        elif opcion == 3:
            print("Gracias por usar el sistema")

        else:
            print("Opción incorrecta")


main()