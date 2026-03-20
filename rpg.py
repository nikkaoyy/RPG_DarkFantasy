from abc import ABC, abstractmethod

# Interfaces: humano, orco, elfo
class humano(ABC):
    @abstractmethod
    def test(self):
        pass
    
class orco(ABC):
    @abstractmethod
    def test(self):
        pass
    
class elfo(ABC):
    @abstractmethod
    def test(self):
        pass

# Productos concretos: cuerpo, montura, armadura, arma

# Productos concretos para humano
class cuerpoHumano(humano):
    def test(self):
        return "Test cuerpoHumano"
    
    def descripcion(self):
        return "Stats:\n- Fuerza: 7\n- Agilidad: 7\n- Inteligencia: 7\n- Defensa: 7\n- Vida: 100\n-" \
        "Ataque: 7"

class monturaHumano(humano):
    def test(self):
        return "Test monturaHumano"
    
    def descripcion(self):
        return "Montura: Caballo"
    
    def montar(self):
        return "Montando un caballo, habilidad de movimiento activada (+10 velocidad)"

class armaduraHumano(humano):
    def test(self):
        return "Test armaduraHumano"
    
    def descripcion(self):
        return "Armadura: Cota de malla"
    
    def equipar(self):
        return "Equipando cota de malla, defensa aumentada en 5 puntos (Defensa total: 12)"
    
    def desequipar(self):
        return "Desequipando cota de malla, defensa reducida en 5 puntos (Defensa total: 7)"
    
class armaHumano(humano):
    def test(self):
        return "Test armaHumano"
    
    def descripcion(self):
        arma = input("Elige tu arma (espada, arco, lanza): ")
        if arma == "espada":
            return "Arma: Espada\n- Ataque: 12"
        elif arma == "arco":
            return "Arma: Arco\n- Ataque: 10\n- Alcance: +5"
        elif arma == "lanza":
            return "Arma: Lanza\n- Ataque: 15\n- Alcance: +10"
        else:
            return "Arma no válida"
        
# Productos concretos para orco
class cuerpoOrco(orco):
    def test(self):
        return "Test cuerpoOrco"
    
    def descripcion(self):
        return "Stats:\n- Fuerza: 10\n- Agilidad: 5\n- Inteligencia: 5\n- Defensa: 10\n- Vida: 200\n-" \
        "Ataque: 10"

class monturaOrco(orco):
    def test(self):
        return "Test monturaOrco"
    
    def descripcion(self):
        return "Montura: Hiena"
    
    def montar(self):
        return "Montando una hiena, habilidad de movimiento activada (+15 velocidad)"

class armaduraOrco(orco):
    def test(self):
        return "Test armaduraOrco"
    
    def descripcion(self):
        return "Armadura: Armadura de cuero con calaveras"
    
    def equipar(self):
        return "Equipando armadura de cuero con calaveras, defensa aumentada en 10 puntos (Defensa total: 20)"
    
    def desequipar(self):
        return "Desequipando armadura de cuero con calaveras, defensa reducida en 10 puntos (Defensa total: 10)"
    
class armaOrco(orco):
    def test(self):
        return "Test armaOrco"
    
    def descripcion(self):
        arma = input("Elige tu arma (espada, mazo, lanza): ")
        if arma == "espada":
            return "Arma: Espada\n- Ataque: 15"
        elif arma == "mazo":
            return "Arma: Mazo\n- Ataque: 18\n- Velocidad: -2"
        else:
            return "Arma no válida"
        
# Productos concretos para elfos
class cuerpoElfo(elfo):
    def test(self):
        return "Test cuerpoElfo"
    
    def descripcion(self):
        return "Stats:\n- Fuerza: 7\n- Agilidad: 7\n- Inteligencia: 12\n- Defensa: 6\n- Vida: 150\n-" \
        "Ataque: 7"

class monturaElfo(elfo):
    def test(self):
        return "Test monturaElfo"
    
    def descripcion(self):
        return "Montura: Unicornio"
    
    def montar(self):
        return "Montando un unicornio, habilidad de movimiento activada (+15 velocidad)"

class armaduraElfo(elfo):
    def test(self):
        return "Test armaduraElfo"
    
    def descripcion(self):
        return "Armadura: Armadura de cuero decorado con hojas"
    
    def equipar(self):
        return "Equipando armadura de cuero decorado con hojas, defensa aumentada en 5 puntos (Defensa total: 11)"
    
    def desequipar(self):
        return "Desequipando armadura de cuero decorado con hojas, defensa reducida en 5 puntos (Defensa total: 6)"
    
class armaElfo(elfo):
    def test(self):
        return "Test armaElfo"
    
    def descripcion(self):
        arma = input("Elige tu arma (espada, arco, bastón): ")
        if arma == "espada":
            return "Arma: Espada\n- Ataque: 12"
        elif arma == "arco":
            return "Arma: Arco\n- Ataque: 10\n- Alcance: +5"
        elif arma == "bastón":
            return "Arma: Bastón\n- Ataque: 15\n- Alcance: +10\n- Poder mágico: +4"
        else:
            return "Arma no válida"
        
class razaFactory(ABC):
    @abstractmethod
    def crearCuerpo(self):
        pass

    @abstractmethod
    def crearMontura(self):
        pass

    @abstractmethod
    def crearArmadura(self):
        pass

    @abstractmethod
    def crearArma(self):
        pass

class humanoFactory(razaFactory):
    def crearCuerpo(self):
        return cuerpoHumano()
    
    def crearMontura(self):
        return monturaHumano()
    
    def crearArmadura(self):
        return armaduraHumano()
    
    def crearArma(self):
        return armaHumano()
    
class orcoFactory(razaFactory):
    def crearCuerpo(self):
        return cuerpoOrco()
    
    def crearMontura(self):
        return monturaOrco()
    
    def crearArmadura(self):
        return armaduraOrco()
    
    def crearArma(self):
        return armaOrco()
    
class elfoFactory(razaFactory):
    def crearCuerpo(self):
        return cuerpoElfo()
    
    def crearMontura(self):
        return monturaElfo()
    
    def crearArmadura(self):
        return armaduraElfo()
    
    def crearArma(self):
        return armaElfo()
    
def crear_personaje(factory:razaFactory):
    cuerpo = factory.crearCuerpo()
    montura = factory.crearMontura()
    armadura = factory.crearArmadura()
    arma = factory.crearArma()

    print(cuerpo.descripcion())
    print(montura.descripcion())
    print(armadura.descripcion())
    print(arma.descripcion())

# Ejemplo de uso a través de elección de raza
def main():
    raza = input("Elige tu raza (humano, orco, elfo): ")
    if raza == "humano":
        factory = humanoFactory()
    elif raza == "orco":
        factory = orcoFactory()
    elif raza == "elfo":
        factory = elfoFactory()
    else:
        return "Raza inválida"
    
    crear_personaje(factory)

if __name__ == "__main__":
    main()