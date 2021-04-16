#meter en un diccionario las variables:

año = ["segundos", "minutos", "horas", "dias", "semanas", "meses"]
valaño = [31540000000, 525600, 8760, 365, 52, 12]

diccionario = dict(zip(año,valaño))
print(diccionario)

print("__________________________________________________________________________________________________________")
# declarar una funcion def persona() en la cual le debo de pedir altura, peso, nombre, instanciarlo a una variable persona

def person():
    nombre = input("Ingrese el Nombre: ")
    altura = input("Ingrese la altura: ")
    peso = input("Ingrese el peso: ")
    print("El nombre de la persona es", nombre, ", su peso es:", peso, "con una altura de:", altura)

hombre = person()
print(hombre)