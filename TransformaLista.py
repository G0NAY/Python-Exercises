valor = int(input("De un valor: "))
print(valor)
entero = list(str(valor))
print(entero)

# a = ["1", "2", "3"]

i = 0
while i < len(entero):
    entero[i] = int(entero[i])
    i += 1

print(entero)