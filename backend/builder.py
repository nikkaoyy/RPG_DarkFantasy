from abc import ABC, abstractmethod
from productos import Personaje
from fabricas import obtener_fabrica


#  Interfaz Builder
class PersonajeBuilder(ABC):
    """Define todos los pasos posibles para construir un Personaje."""

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_nombre(self, nombre: str):
        pass

    @abstractmethod
    def set_raza(self, raza: str):
        pass

    @abstractmethod
    def construir_cuerpo(self):
        pass

    @abstractmethod
    def construir_montura(self):
        pass

    @abstractmethod
    def construir_armadura(self):
        pass

    @abstractmethod
    def construir_arma(self):
        pass

    @abstractmethod
    def agregar_habilidad(self, habilidad: str):
        pass


#  Constructor concreto
class ConstructorPersonaje(PersonajeBuilder):
    """
    Implementa los pasos de construcción usando la Abstract Factory
    para obtener los componentes correctos según la raza.
    """

    def __init__(self):
        self._personaje: Personaje = None
        self._fabrica = None
        self.reset()

    def reset(self):
        self._personaje = Personaje()
        self._fabrica = None
        return self

    # Pasos de configuración 

    def set_nombre(self, nombre: str):
        self._personaje.nombre = nombre
        return self  # permite encadenamiento fluido

    def set_raza(self, raza: str):
        self._personaje.raza = raza.capitalize()
        self._fabrica = obtener_fabrica(raza)
        return self

    def construir_cuerpo(self):
        if not self._fabrica:
            raise RuntimeError("Debes llamar set_raza() antes de construir_cuerpo()")
        self._personaje.cuerpo = self._fabrica.crear_cuerpo()
        return self

    def construir_montura(self):
        if not self._fabrica:
            raise RuntimeError("Debes llamar set_raza() antes de construir_montura()")
        self._personaje.montura = self._fabrica.crear_montura()
        return self

    def construir_armadura(self):
        if not self._fabrica:
            raise RuntimeError("Debes llamar set_raza() antes de construir_armadura()")
        self._personaje.armadura = self._fabrica.crear_armadura()
        return self

    def construir_arma(self):
        if not self._fabrica:
            raise RuntimeError("Debes llamar set_raza() antes de construir_arma()")
        self._personaje.arma = self._fabrica.crear_arma()
        return self

    def agregar_habilidad(self, habilidad: str):
        self._personaje.habilidades.append(habilidad)
        return self

    # Obtener el producto terminado

    def get_personaje(self) -> Personaje:
        """Devuelve el Personaje construido y reinicia el builder."""
        resultado = self._personaje
        self.reset()
        return resultado


#  Director

class Director:
    """
    Define recetas de construcción reutilizables.
    El cliente asocia un builder al director y elige qué receta ejecutar.
    """

    def __init__(self, builder: PersonajeBuilder):
        self._builder = builder

    def set_builder(self, builder: PersonajeBuilder):
        self._builder = builder

    # Recetas

    def construir_guerrero(self, nombre: str, raza: str):
        """Guerrero completo: cuerpo + armadura + arma + montura."""
        (self._builder
            .reset()
            .set_nombre(nombre)
            .set_raza(raza)
            .construir_cuerpo()
            .construir_armadura()
            .construir_arma()
            .construir_montura()
            .agregar_habilidad("Golpe devastador")
            .agregar_habilidad("Resistencia"))

    def construir_explorador(self, nombre: str, raza: str):
        """Explorador ligero: cuerpo + arma + montura (sin armadura pesada)."""
        (self._builder
            .reset()
            .set_nombre(nombre)
            .set_raza(raza)
            .construir_cuerpo()
            .construir_arma()
            .construir_montura()
            .agregar_habilidad("Sigilo")
            .agregar_habilidad("Rastreo"))

    def construir_iniciado(self, nombre: str, raza: str):
        """Iniciado básico: solo cuerpo y arma."""
        (self._builder
            .reset()
            .set_nombre(nombre)
            .set_raza(raza)
            .construir_cuerpo()
            .construir_arma())