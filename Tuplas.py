# las tuplas son inmutables y no se pueden modificar

tupla = (4,"hola", 5.5,[1,2,3,4])

print(tupla[0])
print(tupla[3][2])
print(tupla[0:3])
print(len(tupla))

print("hola" in tupla)
print(tupla[-4]) #cuenta la tupla de manera invertida

lista = list(tupla) # convierte la tupla en lista
print(lista)

tup = tuple(lista) # convierte la lista en tupla
print(tup)