# Hacer un programa que simule un cajero automatico con un saldo inicial de $1000 y tendrá el siguiente menú de
# Opciones: 1.- Ingresar dinero en la cuenta\n2.- Retirar dinero de la cuenta\n3.- Mostrar dinero disponible\n4.- Salir

saldo = 1000
print("1.- Ingresar dinero en la cuenta\n2.- Retirar dinero de la cuenta\n3.- Mostrar dinero disponible\n4.- Salir")
opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    add = float(input("Ingrese una cantidad a su cuenta: "))
    saldo += add
    print(f"Su saldo actual es: {saldo}")
elif opcion == 2:
    dec = float(input("Ingrese una cantidad a retirar: "))
    if dec > saldo:
        print(f"El saldo es de {saldo}, No hay fondos suficientes...")
    else:
        saldo -= dec
        print(f"Su saldo actual es: {saldo}")
elif opcion == 3:
    print(f"Su saldo actual es: {saldo}")
elif opcion == 4:
    print("gracias por utilizar el cajero")
else:
    print("Opcion invalida")