def funcion2(var): # las funciones van hasta arriba
    if var >= 18 and  var >0 and var <= 100:
        return ("tu eres mayor de edad")

    elif var < 18 and  var >0:
        return("tu eres menor de edad")

    else:
        return ("Tu edad no es valida ")

var = float(input("How old are you? "))
print(funcion2(var))

#----------------------------------------------------

def suma(x,y):
    z = x + y
    return(z)

x = float(input("Introduzca el primer numero: "))
y = float(input("Introduzca el segundo numero: "))

print(suma(x,y))

#---------------------------------------------------

def declaracion(x=5, y=6):
    y = x
    x = y
    suma = x + y
    return(suma)

print(declaracion())

