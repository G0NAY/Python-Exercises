'''
def pedir_cumbion():
	#un tab de espacio (4 espacios) código con alguna operación
	print("A pedir un cumbion bien loco")



def validar_edad(age):
    if 0 < age < 100:
        print("Edad correcta")
        if age >= 18:
            print("Eres mayor de edad!!!^O^")
        else:
            print("Eres menor de edad!!! ^_^")
    else:
        print("Edad incorrecta!!! ¬_¬")

'''

def validar_entrada(age):
    if age < 13:
        print("No puedes entrar")
    elif age >= 21:
        print("Puedes entrar al bar y tambien puedes beber")
    else:
        print("Puedes entrar al bar, pero no puedes beber")

age = int(input("Digite su edad: "))
age2 = int(input("Digite su edad: "))

validar_entrada(age)
validar_entrada(age2)

print("Fin del programa...")