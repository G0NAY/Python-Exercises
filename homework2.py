# 2.un programa que simule un cajero automatico, saldo inicial=1000, con el siguiente menu:
# ingresar dinero a la cuenta./ retirar dinero de la cuenta/ salir

print("Bienvenido a su cuenta")

print("1. Ingresar dinero a la cuenta")
print("2. Retirar dinero a la cuenta")
print("3. Salir ")

sal = 1000
option = int(input("Selecione la operacion a realizar: "))

if option == 1:
    print("Su saldo inicial es: ", sal)
    saldo = float(input("Ingrese la catidad que desea depositar: "))
    print("El deposito se realizo de manera exitosa")
    print("Su saldo final es: ", sal+saldo)

elif option == 2:
    print("Su saldo inicial es: 1000")
    saldo1 = float(input("Ingrese la cantidad que desea retirar: "))
    if saldo1 > sal:
        print(" Lo sentimos no cuenta con el saldo suficiente para realizar el retiro")
    else:
        print("El retiro se realizo de manera exitosa")
        print("Su saldo final es: ", sal - saldo1)

else:
    print("Gracias por utilizar nuestro servicio")