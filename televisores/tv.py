from televisores.control import Control
from televisores.marca import Marca
class TV:
    __numTV = 0
    def __init__(self, marca, estado):
        self.__marca = marca
        self.__canal = 1
        self.__volumen = 1
        self.__precio = 500
        self.__estado = estado
        self.__control = None
        TV.__numTV += 1

    def getMarca(self):
        return self.__marca

    def setMarca(self, marca):
        if isinstance(marca, Marca):
            self.__marca = marca

    def getControl(self):
        return self.__control

    def setControl(self, control):
        if isinstance(control, Control):
            self.__control = control

    def getPrecio(self):
        return self.__precio

    def setPrecio(self, Precio):
        self.__precio = Precio

    def getVolumen(self):
        return self.__volumen

    def setVolumen(self, volumen):
        if (1 <= volumen) and (7 >= volumen) and self.__estado:
            self.__volumen = volumen

    def getCanal(self):
        return self.__canal

    def setCanal(self, canal):
        if (1 <= canal) and (120 >= canal) and self.__estado:
            self.__canal = canal

    @classmethod
    def getNumTV(cls):
        return cls.__numTV

    @classmethod
    def setNumTV(cls, num):
        cls.__numTV = num

    def turnOff(self):
        self.__estado = False

    def turnOn(self):
        self.__estado = True

    def canalUp(self):
        self.setCanal(self.__canal + 1)

    def canalDown(self):
        self.setCanal(self.__canal - 1)

    def volumenUp(self):
        self.setVolumen(self.__volumen + 1)

    def volumenDown(self):
        self.setVolumen(self.__volumen - 1)

    def getEstado(self):
        return self.__estado