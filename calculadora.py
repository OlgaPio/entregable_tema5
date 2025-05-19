# Calculadora básica
def calcular(num1, num2, operacion):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicacion":
        return num1 * num2
    elif operacion == "division":
        return num1 / num2 if num2 != 0 else "Error: No se puede dividir por cero"
    else:
        return "Operación no válida"

while True:
    operacion = input("Ingrese operación (suma, resta, multiplicacion, division) o 'salir' para terminar: ")
    if operacion.lower() == "salir":
        print("¡Gracias por usar la calculadora!")
        break

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    print("Resultado:", calcular(num1, num2, operacion))