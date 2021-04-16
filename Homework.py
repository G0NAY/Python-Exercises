#tienes que hacer tarea:
# 1. contruir un programa que simule el funcionamiento de una calculadura; suma, resta, divisi{on y multiplicaci{on


num= float(input("Ingrese el primer valor: "))
num1 = float(input("Ingrese el segundo valor: "))

print("1. Realizar suma")
print("2. Realizar resta")
print("3. Realizar division")
print("4. Realizar multiplicacion")

option = int(input("Selecione la operacion a realizar: "))

if option == 1:
    plus= num + num1
    print("La suma de",num," y ",num1," es: ",plus)

elif option == 2:
    minus= num - num1
    print("La resta de",num," y ",num1," es: ",minus)

elif option == 3:
    between = num / num1
    print("La division de ", num, " entre ", num1, " es: ", between)

elif option == 4:
    times= num * num1
    print("La multiplicacion de",num," por ",num1," es: ",times)

else:
    print("La opcion que ingreso es incorrecta")