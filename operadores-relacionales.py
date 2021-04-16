# operadores relacionales

a=10
b=20
c=30
d=15.5
f=10

equal=(a==f)
print(equal)
different=a!=b
print(different)
mayorque=(d>a)
print(mayorque)
menorque=d<a
print(menorque)

operacion=d+(d==b)
print(operacion)

mayorque=(d>=a)
print(mayorque)
menorque=f<=a
print(menorque)

operacion2=(b<a) or (d<f) and (a==b) or (a>=d)
print(operacion2)

and1=True and True
print(and1)

and2=True and False
print(and2)

or1=True or False
print(or1)
or2= False or False
print(or2)

not1= not(True)
print(not1)
not2=not(False)
print(not2)
