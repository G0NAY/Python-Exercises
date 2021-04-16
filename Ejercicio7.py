# Hacer un programa que pida 3 numeros y determine cual es el mayor 3>2>1

num1= int(input("Proporcione un numero: "))
num2= int(input("Proporcione un segundo numero: "))
num3= int(input("Proporcione un tercer numero: "))

if num1 >= num2 >= num3:
    print(f"{num1} es el mayor de los numeros")
elif num1 <= num2 >= num3:
    print(f"{num2} es el numero mayor")
elif num1 <= num2 <= num3:
    print(f"{num3} es el numero mayor")
