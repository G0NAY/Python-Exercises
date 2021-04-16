# Bucle for

numero = [2,2,3]
for i in numero:
    print(i**2)


for i in [1,2,3,4,5]:
    print("Hola mundo")


'''


coleccion = {1:"Manzana",2:"Pera",3:"Sandia",4:"Papaya","Otro":"Pepe"}
for i in coleccion:
    print(f"{i} -> {coleccion[i]}")

coleccion = {1:"Manzana",2:"Pera",3:"Sandia",4:"Papaya","Otro":"Pepe"}
for clave, valor in coleccion.items():
    print(f"{clave} -> {valor}")

for i in range (1, 6):
    print(f"{i} Hola Mundo")

numeros = list(range(1,6))
print(numeros)


num = list(range(2,11,2))
print(num)

cuadrado = []
for i in range(11):
    potencia = i ** 2
    cuadrado.append(potencia)

print(cuadrado)
'''
cadenas = "alejandro"

for i in cadenas:
    print(f"{i}", end="")

for i in [1, 2, 3, 4, 5, "PepeToño"]:

        print(f"elemento {i}")