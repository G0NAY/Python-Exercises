#Condicionales combinados

age = int(input("Digite su edad: "))

if age < age < 100:
    print("Edad correcta")
    if age >= 18:
        print("Eres mayor de edad!!!^O^")
    else:
        print("Eres menor de edad!!! ^_^")
else:
    print("Edad incorrecta!!! ¬_¬")

print("Fin del programa...")