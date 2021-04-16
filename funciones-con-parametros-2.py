def declaracion(x=5, y=6):
    suma = x + y
    return(suma)

print(declaracion())

#--------------------------------------
def diccionario(**dic):
    llave = 5
    dic["clave"] = llave
    dic["clave1"] = 5.5
    dic["clave3"] = [2, 3, 4]
    print(dic)
    return("ok")

diccionario()

#---------------------------------------
def diccionarios(**kwargs): #recibe los valores como un diccionario
    print(kwargs)
    return(kwargs)

diccionarios(a=1, b=50, z="hello")

#-----------------------------------------
def lista(*args): #recibe los valores como una tupla
    newlist = list(args)
    print(newlist)
    return(newlist)

lista("a", 1, "b","hello")

#--------------------------------------
def diccionarios(**kwargs):
    for contador in kwargs:
        mayus = "la llave es:".capitalize()
        print(mayus ,contador," y su valor es: ", kwargs[contador])

diccionarios(a=1, b=50, z="hello")

#--------------------------------------
def diccionarios(**kwargs):
    for contador in kwargs:
        mayus = 'la llave es:'+ contador +' y su valor es: '+ str(kwargs[contador])
        print(mayus.capitalize())

diccionarios(a=1, b=50, z="hello")

