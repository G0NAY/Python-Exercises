# 2.un programa que simule un cajero automatico, saldo inicial=1000, con el siguiente menu:
# ingresar dinero a la cuenta./ retirar dinero de la cuenta/ salir
# con funciones

def suma(num, num1):
    plus = num + num1
    return(plus)

def resta(num, num1):
    minus = num - num1
    return(minus)

def division(num, num1):
    between = num / num1
    return(between)

def multiplicacion(num, num1):
    times = num * num1
    return(times)

i = 0
print(i)
while i < 5:

    print("1. Realizar suma")
    print("2. Realizar resta")
    print("3. Realizar division")
    print("4. Realizar multiplicacion")

    option = int(input("Selecione la operacion a realizar: "))

    if option == 1:
        num = float(input("Ingrese el primer valor: "))
        num1 = float(input("Ingrese el segundo valor: "))
        print("la suma es: ",suma(num, num1))
        otro = int(input("Desea continuar 1.Yes / 2.No:" ))
        if otro == 1:
            i = 1
        else:
            i = 5

    elif option == 2:
        num = float(input("Ingrese el primer valor: "))
        num1 = float(input("Ingrese el segundo valor: "))
        print("La resta de es: ",resta(num, num1))
        otro = int(input("Desea continuar 1.Yes / 2.No:"))
        if otro == 1:
            i = 1
        else:
            i = 5

    elif option == 3:
        num = float(input("Ingrese el primer valor: "))
        num1 = float(input("Ingrese el segundo valor: "))
        print("La division de es: ",division(num, num1))
        otro = int(input("Desea continuar 1.Yes / 2.No:"))
        if otro == 1:
            i = 1
        else:
            i = 5

    elif option == 4:
        num = float(input("Ingrese el primer valor: "))
        num1 = float(input("Ingrese el segundo valor: "))
        print("La multiplicacion de es: ",multiplicacion(num, num1))
        otro = int(input("Desea continuar 1.Yes / 2.No:"))
        if otro == 1:
            i = 1
        else:
            i = 5

    else:
        print("La opcion que ingreso es incorrecta")

    print("llegue hasta el final")