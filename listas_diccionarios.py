# Lista de nombres de estudiantes
estudiantes = ["Ana", "Luis", "Carlos", "María"]
for estudiante in estudiantes:
    print(f"Estudiante: {estudiante}")

# Diccionario de información de contacto
contacto = {"nombre": "Juan", "correo": "juan@email.com"}
for clave, valor in contacto.items():
    print(f"{clave}: {valor}")

# Agregar elementos a una lista y actualizar diccionario
lista = []
diccionario = {}

while True:
    opcion = input("¿Deseas agregar a la lista (1) o actualizar diccionario (2)? (salir para terminar): ")
    if opcion == "1":
        elemento = input("Ingrese un elemento para la lista: ")
        lista.append(elemento)
        print("Lista actual:", lista)
    elif opcion == "2":
        clave = input("Ingrese la clave: ")
        valor = input("Ingrese el valor: ")
        diccionario[clave] = valor
        print("Diccionario actual:", diccionario)
    elif opcion.lower() == "salir":
        break
