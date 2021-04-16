año = ["segundos", "minutos", "horas", "dias", "semanas", "meses"]
valaño = [31540000000, 525600, 8760, 365, 52, 12]

#split/ busca un valor dentro de un string, cuando encuentre el valor corta la cadena en esa posicion y
# la convierte en listas

var = "hola,año,nuevo"
varlist = var.split(",")
print(varlist)

#join -> contrario de split, trabaja con listas y las convierte en strings

añostr = " - ".join(año)
print(añostr)