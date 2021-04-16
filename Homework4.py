# Escribir un programa que tenga dos listas y que, a continuación, cree las siguientes listas
# (En las que no debe haber repeticiones):

list2 = [0,1,2,4,"Ari","Ale"]
list1 = [3,4,"Mari", "Marco", "Ale"]

#* Lista de palabras que aparecen en las dos listas.
print(list(set(list2 + list1)))

#* Lista de palabras que aparecen en la primera lista, pero no en la segunda
print(list(set(list2) - set(list1)))

#* Lista de palabras que aparecen en la segunda lista, pero no en la primera
print(list(set(list1) - set(list2)))

#* Lista de palabras que aparecen en ambas listas.
print(list(set(list1) & set(list2)))