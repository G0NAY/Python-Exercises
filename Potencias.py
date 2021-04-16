valor = int(input("De un valor: "))

entero = list(str(valor))

i = 0
while i < len(entero):
    entero[i] = int(entero[i])
    i += 1
print(entero)

cuadrado = []
for i in entero:
    potencia = i ** 2
    i += 1
    cuadrado.append(potencia)

cubo = []
for i in entero:
    potencia = i ** 3
    i += 1
    cubo.append(potencia)

suma = 0
for i in cuadrado:
     suma = suma+i

suma2 = 0
for i in cubo:
     suma2 +=i

print(f"El cuadrado de sus elementos es:{cuadrado}")
print(f"El cubo de sus elementos es:{cubo}")
print(f"La suma de los cuadrados de los elementos de la lista es: {suma}" )
print(f"La suma de los cuadrados de los elementos de la lista es: {suma2}" )

