# Hacer un programa para ingresar el radio de un circulo y
# se reporte su area y longitud de la circvunferencia

import math
r = float(input("Proporcione un valor para el Radio: " ))

area = math.pi * r**2
long = 2 * math.pi * r

print(f"El area del circulo es -> {area: .3f}\nLa longitud es -> {long: .3f}")