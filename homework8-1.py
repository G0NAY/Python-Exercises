from Homework8 import calculadora

print("1. Realizar suma")
print("2. Realizar resta")
print("3. Realizar division")
print("4. Realizar multiplicacion")

option = int(input("Selecione la operacion a realizar: "))

if option == 1:
    num = float(input("Ingrese el primer valor: "))
    num1 = float(input("Ingrese el segundo valor: "))
    calcu = calculadora(num, num1)
    print("la suma es: ",calcu.suma())

elif option == 2:
    num = float(input("Ingrese el primer valor: "))
    num1 = float(input("Ingrese el segundo valor: "))
    calcu = calculadora(num, num1)
    print("La resta de es: ",calcu.resta())

elif option == 3:
    num = float(input("Ingrese el primer valor: "))
    num1 = float(input("Ingrese el segundo valor: "))
    calcu = calculadora(num, num1)
    print("La division de es: ",calcu.division())

elif option == 4:
    num = float(input("Ingrese el primer valor: "))
    num1 = float(input("Ingrese el segundo valor: "))
    calcu = calculadora(num, num1)
    print("La multiplicacion de es: ",calcu.multiplicacion())

else:
    print("La opcion que ingreso es incorrecta")