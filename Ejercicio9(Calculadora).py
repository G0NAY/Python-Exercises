# Construir un programa que simule el funcionamiento de una calculadora que puede realizar las cuatro operaciones
# aritmeticas basicas (suma, resta, multiplicación y división). El usuario debe especificar la operación con el primer
# carácter del nombre de la operació.

print("Calculadora: \n S - Suma\n R - Resta\n M - Multiplicacion\n D - Division")
a = float(input("Ingrese un valor: "))
b = input("Ingrese su operacion: ").lower()
c = float(input("ingrese su segundo valor: "))

if b == "s":
    print(f"Resultado {a + c}")
elif b == "r":
    print(f"Resultado: {a - c}")
elif b == "m":
    print(f"Resultado: {a * c}")
elif b == "d":
    print(f"Resultado: {a / c}")
else:
    print("Error operacion no permitida")

print("Fin de programa ")
