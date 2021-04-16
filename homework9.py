# 2.un programa que simule un cajero automatico, saldo inicial=1000, con el siguiente menu:
# ingresar dinero a la cuenta./ retirar dinero de la cuenta/ salir
#utilizando clases

class cajero:
    def __init__(self, saldo, sal):
        self.saldo = saldo
        self.sal = sal

    def depositar(self):
        nuevosaldo = self.sal + self.saldo
        return(nuevosaldo)

    def retirar(self):
        nuevosaldo = self.sal - self.saldo
        return (nuevosaldo)
