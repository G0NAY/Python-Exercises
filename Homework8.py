#tienes que hacer tarea:
# 1. contruir un programa que simule el funcionamiento de una calculadura; suma, resta, divisi{on y multiplicacion
#utilizando clases

class calculadora:
    def __init__(self, num, num1):
        self.num = num
        self.num1 = num1

    def suma(self):
        plus = self.num + self.num1
        return (plus)

    def resta(self):
        minus = self.num - self.num1
        return (minus)

    def division(self):
        between = self.num / self.num1
        return (between)

    def multiplicacion(self ):
        times = self.num * self.num1
        return (times)