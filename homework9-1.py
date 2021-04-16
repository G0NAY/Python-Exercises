from homework9 import cajero

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
    caj = cajero(saldo,sal)
    print("Su saldo final es: ", caj.depositar())

elif option == 2:
    print("Su saldo inicial es: ", sal)
    saldo = float(input("Ingrese la cantidad que desea retirar: "))
    if saldo > sal:
        print(" Lo sentimos no cuenta con el saldo suficiente para realizar el retiro")
    else:
        print("El retiro se realizo de manera exitosa")
        caj = cajero(saldo, sal)
        print("Su saldo final es: ", caj.retirar())

else:
    print("Gracias por utilizar nuestro servicio")