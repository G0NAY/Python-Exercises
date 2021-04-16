conjunto = set()
conjunto1 = {1,2,3}
conjunto2 = {3,4,5,6}
conjunto3 = {1,2}

print(conjunto3.issubset(conjunto1)) #busca si hay subconjuntos
print(conjunto3.isdisjoint(conjunto2)) # valida o busca que no haya subconjuntos

con = frozenset(conjunto2) # ayuda a convertir un conjunto a tupla
print(con)