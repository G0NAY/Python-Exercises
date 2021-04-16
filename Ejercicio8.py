# Hacer un programa que pida un caracter e indique si es una vocal o no

char = input("Proporcione un caracter: ").lower()

if char == "a" or char =="e" or char =="i" or char =="o" or char =="u":
    print("El caracter es una vocal")
else:
    print("El caracter no es vocal")