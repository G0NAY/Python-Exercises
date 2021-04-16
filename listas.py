#listas

list = [0,1,2,3,4,5,"a","b","c","d","e",0.4,0.7,0.1,True,False,[1,2,3]]
list2 = list[6:11]
print(list2)
print(list[16][0])

print(len(list))

list.append("Ari")
print(list)

list.append(list2) #funcion para agregar un elemnto hasta el final de la lista
print(list)

list.insert(6,"fer")#funcion para agregar un elemnto a la lista
print(list)

list.extend([list2,"ari"]) #une elementos a una lista
print(list)

list3 = list2 + list2 #concatena dos listas
print(list3)

print(list.index("fer"))#indica la pocision de un elemnto en la lista
print(list3.count("a")) #cuenta el numero de veces que un elemento se encuentra en la lista
print("ari" in list) #valida si el elemnto se encuentra en la lista

eliminate= list.index("fer")
print(list.pop(eliminate))#elimina el valor en la posicion indicada
print(list)

print(list.remove("a"))# elimina el valor de la lista
print(list)

print(list.reverse())#invierte las posiciones de la lista
print(list)

print(list.sort(reverse = True))#invierte las posiciones de la lista
print(list)


print(list.clear())# elimina todos los elemntos de una lista
print(list)

