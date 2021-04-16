# Escribir un programa donde cree una lista con los siguientes personajes del Señor de los anillos y los vaya agregando
#Nombre: Aragon, Clase: Guerrero, Raza: Dúnadan del Norte
#Nombre: Legolas, Clase: Arquero, Raza: Elfo Sindar
#Nombre: Gandalf, Clase: Mago, Raza: Istar

list1 = []
list2 = []
aragon = {"Nombre": "Aragon", "Clase": "Guerrero", "Raza": "Dúnadan del Norte"}
ara = list(tuple(aragon.values()))
ar =  list(tuple(aragon.keys()))
list2.append(ar)
list1.append(ara)

legolas = {"Nombre": "Legolas", "Clase": "Arquero", "Raza": "Elfo Sindar"}
lego = list(tuple(legolas.values()))
le =  list(tuple(legolas.keys()))
list2.append(le)
list1.append(lego)

gandalf = {"Nombre": "Gandalf", "Clase": "Mago", "Raza": "Istar"}
gan = list(tuple(gandalf.values()))
gand =  list(tuple(gandalf.keys()))
list2.append(gand)
list1.append(gan)

print(list1)
print(list2)

nombres = []
nombres.append(aragon["Nombre"])
nombres.append(legolas["Nombre"])
nombres.append(gandalf["Nombre"])
print(nombres)