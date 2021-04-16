#Hacer un programa que pida 2 numeros y se de cuenta cuál de ellos es par, o si ambos lo son

num1= int(input("Proporcione un numero: "))
num2= int(input("Proporcione un segundo numero: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos son pares")
elif num1 % 2 == 0 and num2 % 2 != 0:
    print("El primer numero es par")
elif num1 % 2 != 0 and num2 % 2 == 0:
    print("El segundo numero es par")
else:
    print("Ambos son impres")

print("Fin de programa...")