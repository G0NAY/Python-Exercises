var =  input("Ingrese la letra que desee: ")\
#.title() convierte una cadena en titulo
#.swapcase() invierte todda una cadena
#.capitalize() primer letra a mayuscula de la cadena
#.upper() A MAYUSCULAS
#.lower() a minusculas

print(var)

if var == "a" or var == "e" or var == "i" or var == "o" or var == "u":
    print( var, " es una vocal")

else:
    print(var, " no es una vocal")