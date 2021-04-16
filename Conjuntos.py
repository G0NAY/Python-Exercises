# los conjuntos son un tipo de coleccion de elementos desordenados, dentro del conjunto no pueden exitir elemntos repitedos
#{}

lista = []
tup = ()
conjunto = set()
conjunto1 = {1,2,3}
conjunto2 = {3,4,5}

conjunto.add(5)
conjunto.add("hi")
conjunto.add(5.3)
print(conjunto)

print("La union es : ", conjunto1 | conjunto2)

print("La interseccion es : ", conjunto1 & conjunto2)

print("La diferencia es : ", conjunto1 - conjunto2)

print(5 not in conjunto)

conjunto.clear()
print(conjunto)