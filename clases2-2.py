from clases2 import game

hechicero = game(30, 80, "hechicero", "destello de luz")
print("Voy a llamar atributos hechicero")
print(hechicero.hitpoints)
print(hechicero.mana)
print(hechicero.vocation)
print(hechicero.habilidad)

print("-----------------")
ataque = hechicero.lanzarhechizo()
print(ataque)

print("-----------------")

espadachin= game(60, 100, "espadachin", "corta cabezas")
print("Voy a llamar atributos hechicero")
print(espadachin.hitpoints)
print(espadachin.mana)
print(espadachin.vocation)
print(espadachin.habilidad)

print("-----------------")
power = espadachin.lanzaataque()
print(power)
