menu_del_restaurante = []

def mostrar_menu():
    print("menu del restaurante")
    
    print("cantidad:", len(menu_del_restaurante))
    if len(menu_del_restaurante) == 0:
        print("no hay nada en el menu pon tus platillos ha gusto")
    else:
        for platillo in menu_del_restaurante:
            print(f"Nombre: {platillo['nombre']} | Precio: ${platillo['precio']}")

def crear_platillo():
    print("crea tu propio platillo")

    print(".............................................................")

    nombre = input("Ingresa el nombre del platillo: ")
    precio = input("Ingresa el precio: ")
    
    nuevo_item = {
        "nombre": nombre,
        "precio": precio
    }
   
    menu_del_restaurante.append(nuevo_item)
    print(f"el platillo'{nombre}' ha sido agregado.")

while True:
    print("estamos gestionando los platillos")

    print ("...................................................")

    print("1. Ver platillos existentes")
    print("2. Crear un nuevo platillo")
    print("3. Salir")
    
    opcion = input("Elige una opción:  ")
    
    if opcion == "1":
        mostrar_menu()
    elif opcion == "2":
        crear_platillo()
    elif opcion == "3":
        print("Cerrando el sistema... ¡Adiós!")
        break 
    else:
        print("Opción no válida, intenta de nuevo.")
