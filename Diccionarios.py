#Diccionarios

diccionario_vacio = { }
diccionario =  {"Azul":"Blue", "Rojo":"Red", "Verde":"Green" }

print(diccionario_vacio)
print(diccionario)
print(diccionario["Azul"])
#para agregar elemento
diccionario["Amarillo"] = "Yelow"
#para eliminar elemento
del(diccionario["Verde"])
print(diccionario)

agenda = {1:"Pepe", 2:"Jose", 3: "Alejandro"}
print(agenda[1])
print(agenda.get(4,"No existe regsitro en la agenda"))
print(agenda.keys())
print(len(agenda))
print(agenda.keys())
print(agenda.values())
agenda.clear()
print(agenda)