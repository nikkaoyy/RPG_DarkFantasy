from abc import ABC, abstractmethod
 

#  Interfaces abstractas por raza
class Humano(ABC):
    @abstractmethod
    def test(self):
        pass
 
class Orco(ABC):
    @abstractmethod
    def test(self):
        pass
 
class Elfo(ABC):
    @abstractmethod
    def test(self):
        pass
 

#  Productos concretos: Humano
class CuerpoHumano(Humano):
    def test(self):
        return "Test CuerpoHumano"
 
    def descripcion(self):
        return (
            "Stats:\n"
            "- Fuerza: 7\n- Agilidad: 7\n- Inteligencia: 7\n"
            "- Defensa: 7\n- Vida: 100\n- Ataque: 7"
        )
 
class MonturaHumano(Humano):
    def test(self):
        return "Test MonturaHumano"
 
    def descripcion(self):
        return "Montura: Caballo"
 
    def montar(self):
        return "Montando un caballo (+10 velocidad)"
 
class ArmaduraHumano(Humano):
    def test(self):
        return "Test ArmaduraHumano"
 
    def descripcion(self):
        return "Armadura: Cota de malla"
 
    def equipar(self):
        return "Equipando cota de malla, defensa +5 (Total: 12)"
 
    def desequipar(self):
        return "Desequipando cota de malla, defensa -5 (Total: 7)"
 
class ArmaHumano(Humano):
    def test(self):
        return "Test ArmaHumano"
 
    def descripcion(self, tipo_arma="espada"):
        opciones = {
            "espada": "Arma: Espada\n- Ataque: 12",
            "arco":   "Arma: Arco\n- Ataque: 10\n- Alcance: +5",
            "lanza":  "Arma: Lanza\n- Ataque: 15\n- Alcance: +10",
        }
        return opciones.get(tipo_arma, "Arma no válida")
 

#  Productos concretos: Orco
class CuerpoOrco(Orco):
    def test(self):
        return "Test CuerpoOrco"
 
    def descripcion(self):
        return (
            "Stats:\n"
            "- Fuerza: 10\n- Agilidad: 5\n- Inteligencia: 5\n"
            "- Defensa: 10\n- Vida: 200\n- Ataque: 10"
        )
 
class MonturaOrco(Orco):
    def test(self):
        return "Test MonturaOrco"
 
    def descripcion(self):
        return "Montura: Hiena"
 
    def montar(self):
        return "Montando una hiena (+15 velocidad)"
 
class ArmaduraOrco(Orco):
    def test(self):
        return "Test ArmaduraOrco"
 
    def descripcion(self):
        return "Armadura: Cuero con calaveras"
 
    def equipar(self):
        return "Equipando armadura de cuero con calaveras, defensa +10 (Total: 20)"
 
    def desequipar(self):
        return "Desequipando armadura de cuero con calaveras, defensa -10 (Total: 10)"
 
class ArmaOrco(Orco):
    def test(self):
        return "Test ArmaOrco"
 
    def descripcion(self, tipo_arma="espada"):
        opciones = {
            "espada": "Arma: Espada\n- Ataque: 15",
            "mazo":   "Arma: Mazo\n- Ataque: 18\n- Velocidad: -2",
            "lanza":  "Arma: Lanza\n- Ataque: 17\n- Alcance: +8",
        }
        return opciones.get(tipo_arma, "Arma no válida")
 
 
#  Productos concretos: Elfo 
class CuerpoElfo(Elfo):
    def test(self):
        return "Test CuerpoElfo"
 
    def descripcion(self):
        return (
            "Stats:\n"
            "- Fuerza: 7\n- Agilidad: 7\n- Inteligencia: 12\n"
            "- Defensa: 6\n- Vida: 150\n- Ataque: 7"
        )
 
class MonturaElfo(Elfo):
    def test(self):
        return "Test MonturaElfo"
 
    def descripcion(self):
        return "Montura: Unicornio"
 
    def montar(self):
        return "Montando un unicornio (+15 velocidad)"
 
class ArmaduraElfo(Elfo):
    def test(self):
        return "Test ArmaduraElfo"
 
    def descripcion(self):
        return "Armadura: Cuero decorado con hojas"
 
    def equipar(self):
        return "Equipando armadura de hojas, defensa +5 (Total: 11)"
 
    def desequipar(self):
        return "Desequipando armadura de hojas, defensa -5 (Total: 6)"
 
class ArmaElfo(Elfo):
    def test(self):
        return "Test ArmaElfo"
 
    def descripcion(self, tipo_arma="arco"):
        opciones = {
            "espada": "Arma: Espada\n- Ataque: 12",
            "arco":   "Arma: Arco\n- Ataque: 10\n- Alcance: +5",
            "bastón": "Arma: Bastón\n- Ataque: 15\n- Alcance: +10\n- Poder mágico: +4",
        }
        return opciones.get(tipo_arma, "Arma no válida")
 
 

#  Producto del Builder: Personaje
class Personaje:
    """Objeto complejo construido paso a paso por el Builder."""
 
    # Instancia vacía, el Builder va a llenar sus atributos
    def __init__(self):
        self.nombre: str = "Sin nombre"
        self.raza: str = "Desconocida"
        self.cuerpo = None
        self.montura = None
        self.armadura = None
        self.arma = None
        self.habilidades: list = []
 
    def __str__(self):
        lineas = [
            f"  Personaje: {self.nombre}",
            f"  Raza:      {self.raza}",
        ]
        if self.cuerpo:
            lineas.append(self.cuerpo.descripcion())
        if self.armadura:
            lineas.append(self.armadura.descripcion())
        if self.arma:
            lineas.append(self.arma.descripcion())
        if self.montura:
            lineas.append(self.montura.descripcion())
        if self.habilidades:
            lineas.append(f"Habilidades: {', '.join(self.habilidades)}")
        return "\n".join(lineas)
