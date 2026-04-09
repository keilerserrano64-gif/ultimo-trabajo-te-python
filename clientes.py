import json


ARCHIVO = "guardado_de_clientes.txt"

def cargar_datos():
    """Carga los clientes desde el archivo al iniciar el programa."""
    try:
        with open(ARCHIVO, "r") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_datos():
    """Guarda la lista actual de clientes en el archivo txt."""
    with open(ARCHIVO, "w") as archivo:
   
        json.dump(clientes_del_restaurante, archivo, indent=4)

clientes_del_restaurante = cargar_datos()

def mostrar_clientes(): 
    print("\n--- LOS CLIENTES DEL RESTAURANTE ---")
    print("Cantidad:", len(clientes_del_restaurante))
    if not clientes_del_restaurante:
        print("No hay clientes registrados todavía.")
    else:
        for cliente in clientes_del_restaurante:
            print(f"Nombre: {cliente['nombre']} | Teléfono: {cliente['telefono']} | ID: {cliente['identificacion']} | Email: {cliente['email']}")

def apartar_cita(): 
    print("\n--- GUARDA TU INFORMACIÓN ---")
    nombre = input("Digite el nombre: ")
    telefono = input("Digite el número de teléfono: ")
    identificacion = input("Digite la identificación: ")
    email = input("Digite el email: ")

    nuevo_cliente = {
        "nombre": nombre,
        "telefono": telefono,
        "identificacion": identificacion,
        "email": email
    }
    
    clientes_del_restaurante.append(nuevo_cliente)
    guardar_datos() 
    print("¡CLIENTE GUARDADO EXITOSAMENTE!")

while True:
    print("\n...................................................")
    print("1. Ver los clientes del restaurante")
    print("2. Apartar cita")
    print("3. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        mostrar_clientes()
    elif opcion == "2":
        apartar_cita() 
    elif opcion == "3":
        print("Cerrando el sistema... ¡Adiós!")
        break 
    else:
        print("Opción no válida, intenta de nuevo.")
