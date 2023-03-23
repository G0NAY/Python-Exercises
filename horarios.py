import datetime, arrow


timenow = datetime.datetime.now() # Obtiene fecha y hora actual
print('date tieme:',timenow)
utc = arrow.get(timenow) # Obtiene fecha y hora actual
print('utc',utc)
##timenow = utc.to('America/Mexico_City').strftime('%Y-%m-%dT%H:%M')
timenow = utc.to('America/Mexico_City')
today = timenow
print('Hoy:',today)

## timenow = datetime.datetime.now() # Obtiene fecha y hora actual
print("Fecha y Hora:", timenow)  # Muestra fecha y hora
print("Fecha y Hora UTC:",timenow.utcnow())  # Muestra fecha/hora UTC
print("Día:",timenow.day)  # Muestra día
print("Mes:",timenow.month)  # Muestra mes
print("Año:",timenow.year)  # Muestra año
print("Hora:", timenow.hour)  # Muestra hora
print("Minutos:",timenow.minute)  # Muestra minuto
print("Segundos:", timenow.second)  # Muestra segundo
print("Microsegundos:",timenow.microsecond)  # Muestra microsegundo

##Valores timedelta weeks, days, hours, minutes, seconds, milliseconds y microseconds.

ayer = timenow - datetime.timedelta(days=1)
print("Ayer:", ayer)
tomorrow = timenow + datetime.timedelta(days=1)
print("Mañana",tomorrow)

hace_una_hora = timenow - datetime.timedelta(hours=1)
print("hace_una_hora:",hace_una_hora)
dentro_una_hora = timenow + datetime.timedelta(hours=1)
print("dentro_una_hora:",dentro_una_hora)