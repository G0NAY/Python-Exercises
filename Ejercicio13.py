# Escribir un programa donde cree una lista con los siguientes personajes del Señor de los anillos
#Nombre: Aragon, Clase: Guerrero, Raza: Dúnadan del Norte
#Nombre: Legolas, Clase: Arquero, Raza: Elfo Sindar
#Nombre: Gandalf, Clase: Mago, Raza: Istar

Lord_of_the_rings = [] #Se crea una lista vacia
Personajes= {"Nombre":"Aragon", "Clase": "Guerrero", "Raza":"Dúnadan del Norte"}
Lord_of_the_rings.append(Personajes)
Personajes = {"Nombre": "Legolas", "Clase": "Arquero", "Raza": "Elfo Sindar"}
Lord_of_the_rings.append(Personajes)
Personajes = {"Nombre": "Gandalf", "Clase": "Mago", "Raza": "Istar"}
Lord_of_the_rings.append(Personajes)

print(Lord_of_the_rings)