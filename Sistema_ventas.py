# =========================================
# SISTEMA DE VENTAS PARA TIENDA DE BARRIO
# =========================================


# Funciòn para mostrar el menù principal
def mostrar_menu():

    print("\n" + "=" * 40)
    print("      SISTEMA DE VENTAS")
    print("=" * 40)

    print("1. Registrar venta")
    print("2. Mostrar productos")
    print("3. Consultar deudas")
    print("4. Ver reporte de ventas")
    print("5. Productos más vendidos")
    print("6. Buscar deuda por cliente")
    print("7. Salir")


# Funciòn para mostrar los productos disponibles
def mostrar_productos(productos):

    print("\n" + "-" * 40)
    print("      PRODUCTOS DISPONIBLES")
    print("-" * 40)

    for codigo in productos:

        nombre = productos[codigo][0]
        precio = productos[codigo][1]

        print(codigo, "-", nombre, "- S/.", precio)


# Funciòn para registrar una venta
def registrar_venta(productos, deudas, ventas):

    total_venta = 0
    continuar = "S"

    while continuar == "S":

        mostrar_productos(productos)

        codigo_texto = input("\nIngrese el código del producto: ")

        if codigo_texto.isdigit():

            codigo_producto = int(codigo_texto)

            if codigo_producto in productos:

                cantidad_texto = input("Ingrese la cantidad: ")

                if cantidad_texto.isdigit():

                    cantidad = int(cantidad_texto)

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

                    print("Debe ingresar una cantidad válida")

            else:

                print("El producto no existe")

        else:

            print("Debe ingresar un código válido")

        continuar = input("\n¿Desea agregar otro producto? (S/N): ").upper()

    if total_venta == 0:

        print("\nNo se registró ninguna venta")
        return

    print("\n" + "-" * 40)
    print("Total a pagar: S/.", round(total_venta, 2))

    tipo_pago = input("¿La compra es al crédito? (S/N): ").upper()

    if tipo_pago == "S":

        nombre_cliente = ""

        while nombre_cliente == "":

            nombre_cliente = input("Ingrese el nombre del cliente: ").strip()

            if nombre_cliente == "":

                print("Debe ingresar un nombre válido")

        deuda = [nombre_cliente, total_venta]

        deudas.append(deuda)

        print("\nDeuda registrada correctamente")

    print("\nVenta registrada correctamente")


# Funciòn para mostrar las deudas registradas
def consultar_deudas(deudas):

    print("\n" + "-" * 40)
    print("         LISTA DE DEUDAS")
    print("-" * 40)

    if len(deudas) == 0:

        print("No existen deudas registradas")

    else:

        for deuda in deudas:

            cliente = deuda[0]
            monto = deuda[1]

            print("Cliente:", cliente, "- Deuda: S/.", round(monto, 2))


# Funciòn para buscar deuda por cliente
def buscar_deuda_cliente(deudas):

    print("\n" + "-" * 40)
    print("         BUSCAR CLIENTE")
    print("-" * 40)

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

            print("\nCliente:", cliente)
            print("Deuda pendiente: S/.", round(monto, 2))

            encontrado = True

    if encontrado == False:

        print("El cliente no tiene deudas registradas")


# Funciòn para mostrar el reporte de ventas
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

    print("\n" + "-" * 40)
    print("       REPORTE DE VENTAS")
    print("-" * 40)

    print("Cantidad de ventas realizadas:", cantidad_ventas)
    print("Total vendido: S/.", round(total_general, 2))


# Funciòn para mostrar los productos más vendidos
def productos_mas_vendidos(ventas):

    print("\n" + "-" * 40)
    print("      PRODUCTOS MÁS VENDIDOS")
    print("-" * 40)

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


# Funciòn principal del sistema
def main():

    productos = {
        1: ["Coca Cola", 3.50],
        2: ["Pan", 0.50],
        3: ["Leche", 4.00],
        4: ["Galletas", 2.00],
        5: ["Arroz", 5.00],
        6: ["Azúcar", 4.50],
        7: ["Aceite", 8.00],
        8: ["Huevos", 7.50],
        9: ["Fideos", 3.00],
        10: ["Chocolate", 2.50]
    }

    deudas = []
    ventas = []

    opcion = 0

    while opcion != 7:

        mostrar_menu()

        opcion_texto = input("\nIngrese una opción: ")

        if opcion_texto.isdigit():

            opcion = int(opcion_texto)

        else:

            opcion = 0

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

            print("\nGracias por usar el sistema")

        else:

            print("\nOpción incorrecta")

main()