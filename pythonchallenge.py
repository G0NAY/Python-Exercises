
class Potencia():
#Clase para realizar la multiplicacion de elementos

    def __init__(self,numero):
        #Constructor de elementos iniciales
        self.numero = list(str(numero))
        self.cuadrado = []
        self.cubo = []
        self.entrada = True
        self.suma = 0

        # Bucle para llenar la lista con los elementos separados
        i = 0
        while i < len(self.numero):
            self.numero[i] = int(self.numero[i])
            i += 1

    # Metodo potencia eleva a lista a las potencias correpondientes al cuadrado y al cubo
    def potencia(self,numero):
        if(self.entrada):
            for i in self.numero:
                pot = i ** 2
                i += 1
                self.cuadrado.append(pot)
            return self.cuadrado
        elif(self.entrada == False):
             for i in self.numero:
                    pot = i ** 3
                    i += 1
                    self.cubo.append(pot)
             return self.cubo

class Sumadecuadrados(Potencia):
# Clase para sumar elementos de la lista elevados al cuadrado

    def __init__(self,numero):
        self.cuadrado = numero
        self.suma = 0

    def sumacuadrados(self,numero):
        for i in self.cuadrado:
            self.suma = self.suma + i
        return self.suma

class Sumadecubos(Potencia):
# Clase para sumar elementos de la lista elevados al cubo

    def __init__(self,numero):
        self.cubo = numero
        self.suma = 0

    def sumacubos(self,numero):
        for i in self.cubo:
            self.suma= self.suma + i
        return self.suma

#En esta parte inicia el programa
numero = int(input("De un valor: "))

bloque1 = Potencia(numero)
alcuadrado = bloque1.potencia(numero)
bloque1.entrada = False
alcubo = bloque1.potencia(numero)
bloque2 = Sumadecuadrados(alcuadrado)
sumacuadrados = bloque2.sumacuadrados(alcuadrado)
bloque3 = Sumadecubos(alcubo)
sumacubos = bloque3.sumacubos(alcubo)

print(f"La suma de los digitos elevados al cuadrado + la suma de los digitos elevados al cubo es:\n{sumacuadrados+sumacubos}")