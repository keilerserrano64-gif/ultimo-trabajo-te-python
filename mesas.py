import json

ARCHIVO_MESAS = "mesas.txt"

def cargar_mesas():
    try:
        with open(ARCHIVO_MESAS, "r") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_mesas():
    with open(ARCHIVO_MESAS, "w") as archivo:
        json.dump(mesas_del_restaurante, archivo, indent=4)


mesas_del_restaurante = cargar_mesas()

def mostrar_mesas():
    print("\n--- LAS MESAS DE NUESTRO RESTAURANTE ---")
    print("Cantidad:", len(mesas_del_restaurante))
    if not mesas_del_restaurante:
        print("No hay mesas apartadas todavía.")
    else:
        for mesa in mesas_del_restaurante:
            print(f"Nombre: {mesa['nombre']} | Puestos: {mesa['puestos']} | Código: {mesa['codigo']}")

def aparta_tu_mesa():
    print("\n--- APARTA TU MESA ---")
    nombre = input("Digite el nombre de quien reserva: ")
    puestos = input("Digite el número de puestos: ")
    codigo = input("Digite el código de la mesa: ")

    nueva_mesa = {
        "nombre": nombre,
        "puestos": puestos,
        "codigo": codigo
    }
    
    mesas_del_restaurante.append(nueva_mesa)
    guardar_mesas() 
    print("¡MESA APARTADA EXITOSAMENTE!")

while True:
    print("\nESTAMOS GESTIONANDO LAS MESAS")
    print("...................................................")
    print("1. Ver mesas apartadas")
    print("2. Apartar mesa")
    print("3. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        mostrar_mesas()
    elif opcion == "2":
        aparta_tu_mesa() 
    elif opcion == "3":
        print("Cerrando el sistema... ¡Adiós!")
        break 
    else:
        print("Opción no válida, intenta de nuevo.")
