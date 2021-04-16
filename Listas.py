# Listas
'''
lista2 = ["Lunes", "Martes", "Miercoles", "Jueves", "viernes", True, 40, [2, 3, 4, 5, ], 4.5]
print(f"La lista tiene {len(lista2)} elementos\n")

list = [1, 2, 3]

list.append(6)
print(list)

list.insert(2,6)
print(list)

list1 = [1, 2, 3, 4, 5]
list1.extend([2,6,7,8])
print(list1)

list3 =  list + list1
print(list3)

lista = [1, 2, 3, "elemento"]
print("elemento" in lista)


'''

lista = [1, 2, 3, 3, -9, -3, 10]
print(lista)
lista.sort(reverse=True)
print(lista)