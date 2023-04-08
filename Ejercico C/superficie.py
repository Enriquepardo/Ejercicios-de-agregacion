
from abc import ABC, abstractmethod

class Pared:
    def __init__(self, orientacion):
        self.orientacion = orientacion
        self.ventanas = []

    def agregar_ventana(self, ventana):
        self.ventanas.append(ventana)

    def superficie_acristalada(self):
        return sum([ventana.superficie for ventana in self.ventanas])

    

class Cristal(ABC):
    @abstractmethod
    def superficie_acristalada(self):
        pass

class Ventana(Cristal):
    def __init__(self, pared, superficie, proteccion):
        if proteccion is None:
            raise Exception("Protección obligatoria")
        self.pared = pared
        self.superficie = superficie
        self.proteccion = proteccion
        self.pared.agregar_ventana(self)

    def superficie_acristalada(self):
        return self.superficie

class Casa:
    def __init__(self, paredes):
        self.paredes = paredes

    def superficie_acristalada(self):
        return sum([pared.superficie_acristalada() for pared in self.paredes])


class ParedCortina(Pared, Cristal):
    def __init__(self, orientacion, superficie):
        super().__init__(orientacion)
        self.superficie = superficie

    def superficie_acristalada(self):
        return self.superficie


# Instanciación de las paredes 
pared_norte = Pared("NORTE") 
pared_oeste = Pared("OESTE") 
pared_sur = Pared("SUR") 
pared_este = Pared("ESTE") 
# Instanciación de las ventanas 
ventana_norte = Ventana(pared_norte, 0.5, 'proteccion') 
ventana_oeste = Ventana(pared_oeste, 1, 'proteccion') 
ventana_sur = Ventana(pared_sur, 2, 'proteccion') 
ventana_este = Ventana(pared_este, 1, 'proteccion') 
# Instanciación de la casa con las 4 paredes 
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este]) 
print(casa.superficie_acristalada()) 



casa.paredes[2] = ParedCortina("SUR", 10) 
print(casa.superficie_acristalada()) 




