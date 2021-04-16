from clases import Coche
from clases import player
'''
print(player.hit_points)
print(player.mana)
print(player.vocacion)

sorcerer = player()
sorcerer.hit_points = 40
sorcerer.mana = 80
sorcerer.vocacion = "Sorcerer"
sorcerer.habilidad = "Utevo lux!!!"

sorcerer = player(30,80,"Sorcerer", "Utevo de Lux!!")
print(sorcerer.hit_points)
print(sorcerer.mana)
print(sorcerer.vocacion)
print(sorcerer.lanzar_hechizo())

knight = player(80,20,"Knigth","Exoru")
print(knight.hit_points)
print(knight.mana)
print(knight.vocacion)
print(knight.lanzar_hechizo())
'''

miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()
#print(miCoche.chequeo_interno())

miCoche2 = Coche()
print(miCoche.arrancar(False))
miCoche2.ruedas = 2
miCoche2.estado()
#print(miCoche2.chequeo_interno())
