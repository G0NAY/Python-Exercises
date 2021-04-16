dic = {}
llave = 5
dic["clave"] = llave
dic["clave1"] = 5.5
dic["clave3"] = [2,3,4]
valor = "Hi"

dicc = {"clave": valor, "clave3": 2, "clave4": 5.5,"clave5": [1,2,3],"clave6": dic}
print(dicc["clave"])

dicc["clave2"] = valor + "world"
print(dicc)
del(dicc["clave2"])
print(dicc)

print(dicc.get("clave7", "No encontre clave 7")) # realiza la validacion por llave del diccionario / busca elementos
                                                 # si no encuentra el valor regresa string
print(dicc.keys()) #indica las claves dentro del diccionario
print(dicc.values()) #indica los valores de las claves solamente
print(dicc.items()) #pone el diccionario dentro de una tupla

var = dicc.values()
print(tuple(var))

print(len(dicc))
dicc.clear()