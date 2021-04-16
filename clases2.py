class game:
    def __init__(self, hitpoints, mana, vocation, habilidad): #sirve para modificar dentro de la clase
        print("Estoy entradno a player")
        self.hitpoints = hitpoints
        print(self.hitpoints)
        self.mana = mana
        self.vocation = vocation
        self.habilidad = habilidad

    #def player(self, hitpoints, mana, vocation, habilidad):
       #pass

    def lanzarhechizo(self):
        return self.habilidad

    def lanzaataque(self):
        return self.habilidad