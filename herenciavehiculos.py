from herencia import vehiculos, motos, coche

vehiculo = vehiculos("ford","xxx")

print(vehiculo.estado())
print(vehiculo.arrancar())
print(vehiculo.estado())

moto = motos("yamaha", "dukati")
print(moto.estado())
print(moto.arrancar())
print(moto.estado())

coches = coche("Nissan", "Versa")
print(coches.estado())