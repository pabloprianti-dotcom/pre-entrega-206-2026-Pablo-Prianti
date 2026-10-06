productos = []
opciones = ""


while opciones != "5":
    print("\n")
    print("="*45)
    print("Bienvenido al sistema de gestión de productos")
    print("="*45)
    print("Opciones disponibles:")
    opciones = input("\n1. Agregar producto \n2. Mostrar productos \n3. Buscar producto por nombre \n4. Eliminar producto \n5. Salir \n\nOpcion: ").strip().lower()
    print("="*45)

    if opciones == "1":
        continuar = "si"
        while continuar == "si":
            nombre_producto = input("Nombre del Producto: " ).strip().lower()
            while nombre_producto == "":
                print("ERROR! Ingrese un nombre válido")
                nombre_producto = input("Nombre del Producto: " ).strip().lower()

                
            categoria_producto = input ("A que categoria pertence: " ).strip().lower()
            while categoria_producto == "":
                print("ERROR! Ingrese una categoria válida")
                categoria_producto = input ("A que categoria pertence: " ).strip().lower()


            precio_producto = input("Cual es su precio?: $" )            
            while not precio_producto.isdigit():
                print("ERROR! Ingrese un precio válido")
                precio_producto = input("Cual es su precio?: $" )
            precio_producto = int(precio_producto)
        
            producto_individual = [nombre_producto,categoria_producto, precio_producto]  
            productos.append(producto_individual)
            continuar = input("Desea agregar otro producto? (si/no): ").strip().lower()

    elif opciones == "2" :
        if len(productos) == 0:
            print ("No hay productos para mostrar")
        else:
            print("Productos agregados: ")
            i = 1
            for producto_individual in productos:
                print(f"{i}. Nombre: {producto_individual[0]}, Categoria: {producto_individual[1]}, Precio: {producto_individual[2]}")
                i += 1

    elif opciones == "3" :
        if len(productos) == 0:
            print ("No hay productos para buscar")
        else:
            nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip().lower()
            encontrado = False
            for producto_individual in productos:
                if nombre_buscar in producto_individual[0]:
                    print(f"Producto encontrado: Nombre: {producto_individual[0]}, Categoria: {producto_individual[1]}, Precio: {producto_individual[2]}")
                    encontrado = True
                    break
            if not encontrado:
                print("Producto no encontrado.")

    elif opciones == "4" :
        if len(productos) == 0:
            print ("No hay productos para eliminar")
        else:
            producto_eliminar = input("Ingrese el nombre del producto a eliminar:  ").strip().lower()
            encontrado = False
            for producto_individual in productos:
                if producto_individual[0] == producto_eliminar:
                    productos.remove(producto_individual)
                    print(f"Producto eliminado: Nombre: {producto_individual[0]}, Categoria: {producto_individual[1]}, Precio: {producto_individual[2]}")
                    encontrado = True
                    break
            if not encontrado:
                print("Producto no encontrado.")

    elif opciones == "5":
        print("Saliendo del programa...")
        print("="*45)
    else:
        print("Opción inválida. Por favor, elija una opción del 1 al 5.")
