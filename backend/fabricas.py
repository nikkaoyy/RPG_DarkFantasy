from abc import ABC, abstractmethod
from productos import *


#  Fábrica abstracta
class RazaFactory(ABC):
    @abstractmethod
    def crear_cuerpo(self):
        pass

    @abstractmethod
    def crear_montura(self):
        pass

    @abstractmethod
    def crear_armadura(self):
        pass

    @abstractmethod
    def crear_arma(self):
        pass


#  Fábricas concretas
class HumanoFactory(RazaFactory):
    def crear_cuerpo(self):
        return CuerpoHumano()

    def crear_montura(self):
        return MonturaHumano()

    def crear_armadura(self):
        return ArmaduraHumano()

    def crear_arma(self):
        return ArmaHumano()


class OrcoFactory(RazaFactory):
    def crear_cuerpo(self):
        return CuerpoOrco()

    def crear_montura(self):
        return MonturaOrco()

    def crear_armadura(self):
        return ArmaduraOrco()

    def crear_arma(self):
        return ArmaOrco()


class ElfoFactory(RazaFactory):
    def crear_cuerpo(self):
        return CuerpoElfo()

    def crear_montura(self):
        return MonturaElfo()

    def crear_armadura(self):
        return ArmaduraElfo()

    def crear_arma(self):
        return ArmaElfo()


#  Registro de fábricas (facilita extensión)
FABRICAS: dict[str, RazaFactory] = {
    "humano": HumanoFactory(),
    "orco":   OrcoFactory(),
    "elfo":   ElfoFactory(),
}


def obtener_fabrica(raza: str) -> RazaFactory:
    fabrica = FABRICAS.get(raza.lower())
    if not fabrica:
        raise ValueError(f"Raza '{raza}' no reconocida. Opciones: {list(FABRICAS.keys())}")
    return fabrica