#condicionales

var = float(input("How old are you? "))

if var >= 18 and  var >0 and var <= 100:
    print("tu eres mayor de edad")

elif var < 18 and  var >0:
    print("tu eres menor de edad")

#elif var < 0:
    #print(True)

else:
    print("Tu edad no es valida ")


