class vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelerar = False
        self.frenar = False

    def arrancar(self):
        self.enmarcha = True
        return self.enmarcha

    def acelerar(self):
        self.acelerar = True
        return self.acelerar

    def frenar(self):
        self.frenar = True
        return self.frenar

    def estado(self):
        print( "marca" , self.marca,"modelo" , self.modelo, "arrancar" , self.enmarcha, "acelerar" , self.acelerar,"frenar" ,self.frenar)


class motos(vehiculos):
    pass

class coche(vehiculos):
    pass

class visicleta(vehiculos):
    pass

class avion(vehiculos):
    pass