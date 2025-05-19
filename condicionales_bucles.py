# Determinar si un número es par o impar
num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# Iterar sobre una lista e imprimir sus cuadrados
numeros = [1, 2, 3, 4, 5]
for n in numeros:
    print(f"El cuadrado de {n} es {n**2}")

# Bucle while hasta que el usuario ingrese "salir"
while True:
    entrada = input("Escribe algo ('salir' para terminar): ")
    if entrada.lower() == "salir":
        print("¡Hasta luego!")
        break
