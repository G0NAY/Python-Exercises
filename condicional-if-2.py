var = int(input("Ingrese el primer valor: "))
var1 = int(input("Ingrese el segundo valor: "))
var2 = int(input("Ingrese el tercer valor: "))

if var >= var1 and var >= var2 :
    print(" el numero mayor es : ",var)

elif var <= var1 and var1 >= var2:
    print(" el numero mayor es : ",var1)

elif var <= var2 and var1 <= var2:
    print(" el numero mayor es : ",var2)

else:
    print("los tres valores son iguales")