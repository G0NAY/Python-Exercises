var = int(input("Ingrese el primer valor "))
var1 = int(input("Ingrese el segundo valor "))

if var % 2 == 0 and var1 % 2 == 0:
    print("Los dos numeros ingresados son pares ")

if var % 2 == 0 and var1 % 2 != 0:
    print(var, " es par y ", var1, " es impar")

if var % 2 != 0 and var1 % 2 == 0:
    print(var, " es impar y ", var1, " es par")
else:
    print("Los dos numeros ingresados son impares ")