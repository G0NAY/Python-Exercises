# el for recorre una coleccion de datos
for contador in [1,2,3,4,5, "Ari", "Alex", [1,2,3]]:
    print( "El numero es: ", contador)

coleccion = {"clave": 1, "clave2" : "Ari", "clave3": "alex"}
for contador in coleccion:
    print( contador, " es: ", coleccion[contador])



var = "variable"
i = 1
j = ""
for contenedor in var:
    print("Estoy en el ciclo: ", i)
    i += 1
    print("El valor es: ", contenedor)
    j += contenedor
    print(j)

j = 1
for i in range(0,8): # inicia en la posicion 0 hasta la posicion indicada.
                     # range(1) -> range (0,1)
    print("2. El ciclo: ",j, "Hola mundo")
    j += 1
    print(i)

var2 = list(range(1,10,3)) # crea una lista con un rango de la posicion 1 a la 10 haciendo iteraciones
                            # de 3 en 3 posiciones
print(var2)

i = 0
s = 0
for contador in var2:
    print("La pocision ",i, " es: ",contador)
    i += 1
    s += contador
    print(s)
