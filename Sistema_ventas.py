def mostrar_menu():

    print("\n--- SISTEMA DE VENTAS ---")
    print("1. Registrar venta")
    print("2. Mostrar productos")
    print("3. Consultar deudas")
    print("4. Ver reporte de ventas")
    print("5. Productos más vendidos")
    print("6. Buscar deuda por cliente")
    print("7. Salir")


def mostrar_productos(productos):

    print("\n--- PRODUCTOS DISPONIBLES ---")

    for codigo in productos:

        nombre = productos[codigo][0]
        precio = productos[codigo][1]

        print(codigo, "-", nombre, "- S/.", precio)


def registrar_venta(productos, deudas, ventas):

    total_venta = 0
    continuar = "S"

    while continuar == "S":

        mostrar_productos(productos)

        codigo_producto = int(input("\nIngrese el código del producto: "))

        if codigo_producto in productos:

            cantidad = int(input("Ingrese la cantidad: "))

            if cantidad > 0:

                nombre_producto = productos[codigo_producto][0]
                precio_producto = productos[codigo_producto][1]

                subtotal = cantidad * precio_producto

                total_venta += subtotal

                venta = [nombre_producto, cantidad]
                ventas.append(venta)

                print("\nProducto:", nombre_producto)
                print("Subtotal: S/.", round(subtotal, 2))

            else:

                print("La cantidad debe ser mayor a 0")

        else:

            print("El producto no existe")

        continuar = input("\n¿Desea agregar otro producto? (S/N): ").upper()

    print("\nTotal a pagar: S/.", round(total_venta, 2))

    tipo_pago = input("¿La compra es al crédito? (S/N): ").upper()

    if tipo_pago == "S":

        nombre_cliente = ""

        while nombre_cliente == "":

            nombre_cliente = input("Ingrese el nombre del cliente: ").strip()

            if nombre_cliente == "":

                print("Debe ingresar un nombre válido")

        deuda = [nombre_cliente, total_venta]

        deudas.append(deuda)

        print("La deuda fue registrada correctamente")


def consultar_deudas(deudas):

    print("\n--- LISTA DE DEUDAS ---")

    if len(deudas) == 0:

        print("No existen deudas registradas")

    else:

        for deuda in deudas:

            cliente = deuda[0]
            monto = deuda[1]

            print("Cliente:", cliente, "- Deuda: S/.", round(monto, 2))


def buscar_deuda_cliente(deudas):

    print("\n--- BUSCAR CLIENTE ---")

    nombre_buscar = ""

    while nombre_buscar == "":

        nombre_buscar = input("Ingrese el nombre del cliente: ").strip()

        if nombre_buscar == "":

            print("Debe ingresar un nombre válido")

    encontrado = False

    for deuda in deudas:

        cliente = deuda[0]
        monto = deuda[1]

        if cliente.lower() == nombre_buscar.lower():

            print("Cliente:", cliente)
            print("Deuda pendiente: S/.", round(monto, 2))

            encontrado = True

    if encontrado == False:

        print("El cliente no tiene deudas registradas")
        
def reporte_ventas(ventas, productos):

    total_general = 0
    cantidad_ventas = len(ventas)

    for venta in ventas:

        nombre_producto = venta[0]
        cantidad = venta[1]

        for codigo in productos:

            if productos[codigo][0] == nombre_producto:

                precio = productos[codigo][1]

                total_general += precio * cantidad

    print("\n--- REPORTE DE VENTAS ---")
    print("Cantidad de ventas realizadas:", cantidad_ventas)
    print("Total vendido: S/.", round(total_general, 2))


def productos_mas_vendidos(ventas):

    print("\n--- PRODUCTOS MÁS VENDIDOS ---")

    if len(ventas) == 0:

        print("No existen ventas registradas")

    else:

        conteo = {}

        for venta in ventas:

            nombre_producto = venta[0]
            cantidad = venta[1]

            if nombre_producto in conteo:

                conteo[nombre_producto] += cantidad

            else:

                conteo[nombre_producto] = cantidad

        for producto in conteo:

            print(producto, "- Cantidad vendida:", conteo[producto])


def main():

    productos = {
        1: ["Coca Cola", 3.50],
        2: ["Pan", 0.50],
        3: ["Leche", 4.00],
        4: ["Galletas", 2.00]
    }

    deudas = []
    ventas = []

    opcion = 0

    while opcion != 7:

        mostrar_menu()

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:

            registrar_venta(productos, deudas, ventas)

        elif opcion == 2:

            mostrar_productos(productos)

        elif opcion == 3:

            consultar_deudas(deudas)

        elif opcion == 4:

            reporte_ventas(ventas, productos)

        elif opcion == 5:

            productos_mas_vendidos(ventas)

        elif opcion == 6:

            buscar_deuda_cliente(deudas)

        elif opcion == 7:

            print("Gracias por usar el sistema")

        else:

            print("Opción incorrecta")


main()