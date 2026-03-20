# RPG Abstract Factory

Sistema de creación de personajes RPG implementado con el patrón de diseño **Abstract Factory**.

## Descripción

Este proyecto demuestra la implementación del patrón Abstract Factory en Python, permitiendo la creación de personajes completos para un juego RPG. Cada raza (Humano, Orco, Elfo) tiene su propia familia de productos (Cuerpo, Montura, Armadura, Arma) que se crean de manera cohesiva a través de factorías especializadas.

## Características

- **Patrón Abstract Factory**: Creación de familias de objetos relacionados sin especificar sus clases concretas
- **3 Razas disponibles**:
  - 🧙 Humano: Estadísticas equilibradas
  - 💪 Orco: Alta fuerza y defensa
  - 🧝 Elfo: Inteligencia mejorada y magia

- **4 Componentes por raza**:
  - Cuerpo (Stats base del personaje)
  - Montura (Vehículo de transporte)
  - Armadura (Defensa y equipamiento)
  - Arma (Múltiples opciones según raza)

## Requisitos

- Python 3.6+

## Instalación

```bash
git clone <repository-url>
cd RPG_AbFac
```

## Uso

Ejecutar el programa:

```bash
python rpg.py
```

Se te pedirá que selecciones una raza:

```
Elige tu raza (humano, orco, elfo): humano
```

El sistema creará un personaje completo con todos sus componentes:
- Estadísticas del cuerpo
- Montura disponible
- Armadura equipada
- Selección de arma

### Ejemplo de ejecución

```
Elige tu raza (humano, orco, elfo): humano
Stats:
- Fuerza: 7
- Agilidad: 7
- Inteligencia: 7
- Defensa: 7
- Vida: 100
- Ataque: 7
Montura: Caballo
...
```

## Estructura del Proyecto

```
RPG_AbFac/
├── rpg.py           # Código principal con todas las clases
├── README.md        # Este archivo
└── LICENSE          # Licencia del proyecto
```

## Patrón Abstract Factory

El patrón utiliza:

- **Interfaces abstractas** (`humano`, `orco`, `elfo`): Definen los métodos que deben implementar
- **Productos concretos**: Clases específicas para cada componente
- **Factorías abstractas** (`razaFactory`): Define los métodos de creación
- **Factorías concretas** (`humanoFactory`, `orcoFactory`, `elfoFactory`): Implementan la creación de productos

Esta estructura garantiza que los componentes de un personaje sean cohesivos y utilizados correctamente.

## Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## Autor

- [Nicolás Martínez Pineda](https://github.com/nikkaoyy)
